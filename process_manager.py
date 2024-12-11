import time
import json
from threading import Thread, Lock
from datetime import datetime
from memory_manager import MemoryManager


class ProcessManager:
    STATE_FILE = "task_state.json"

    def __init__(self, total_memory=512):
        """Initialize the process manager."""
        self.task_queue = []  # List to store periodic tasks
        self.scheduled_tasks = []  # List to store scheduled tasks (cron-like)
        self.lock = Lock()    # Lock for thread safety
        self.running = False  # Flag for automatic mode
        self.memory_manager = MemoryManager(total_memory)  # Initialize Memory Manager
        print("ProcessManager: Initialized.")

    def add_task(self, task_name, interval, memory_size):
        """Add a periodic task to the queue."""
        with self.lock:
            if not self.memory_manager.allocate_memory(task_name, memory_size):
                print(f"ProcessManager: Failed to add task '{task_name}' due to insufficient memory.")
                return
            task = {"name": task_name, "interval": interval, "next_run": time.time() + interval}
            self.task_queue.append(task)
            print(f"ProcessManager: Added periodic task '{task_name}' with interval {interval} seconds.")

    def schedule_task(self, task_name, time_str):
        """Schedule a task to run at a specific time."""
        try:
            scheduled_time = datetime.strptime(time_str, "%H:%M").time()
            with self.lock:
                task = {"name": task_name, "scheduled_time": scheduled_time}
                self.scheduled_tasks.append(task)
            print(f"ProcessManager: Scheduled task '{task_name}' to run at {time_str}.")
        except ValueError:
            print("ProcessManager: Invalid time format. Use HH:MM.")

    def remove_task(self, task_name):
        """Remove a task from the queue."""
        with self.lock:
            self.task_queue = [task for task in self.task_queue if task["name"] != task_name]
            self.scheduled_tasks = [task for task in self.scheduled_tasks if task["name"] != task_name]
            self.memory_manager.deallocate_memory(task_name)
            print(f"ProcessManager: Removed task '{task_name}'.")

    def list_tasks(self):
        """List all tasks in the queue."""
        with self.lock:
            if not self.task_queue and not self.scheduled_tasks:
                print("ProcessManager: No tasks are currently scheduled.")
                return

            print("ProcessManager: Scheduled Tasks:")
            for task in self.task_queue:
                next_run_time = datetime.fromtimestamp(task["next_run"]).strftime("%Y-%m-%d %H:%M:%S")
                print(f"- Periodic Task: {task['name']} (runs every {task['interval']} seconds, next run at {next_run_time})")
            for task in self.scheduled_tasks:
                print(f"- Scheduled Task: {task['name']} (runs at {task['scheduled_time']})")

    def log_task_execution(self, task_name, status="success"):
        """Log task execution results with status."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] Task '{task_name}' executed with status: {status}\n"
        with open("task_log.txt", "a") as log_file:
            log_file.write(log_message)
        print(f"ProcessManager: Logged execution of task '{task_name}' with status: {status}.")

    def scheduler(self):
        """Run all periodic and scheduled tasks."""
        current_time = datetime.now().time()
        with self.lock:
            # Run periodic tasks
            for task in self.task_queue[:]:
                if time.time() >= task["next_run"]:
                    print(f"ProcessManager: Running periodic task '{task['name']}'...")
                    self.log_task_execution(task["name"])
                    task["next_run"] = time.time() + task["interval"]

            # Run scheduled tasks
            for task in self.scheduled_tasks[:]:
                if task["scheduled_time"] <= current_time:
                    print(f"ProcessManager: Running scheduled task '{task['name']}'...")
                    self.log_task_execution(task["name"])
                    self.scheduled_tasks.remove(task)

    def save_state(self):
        """Save tasks to a file."""
        with self.lock:
            state = {
                "task_queue": self.task_queue,
                "scheduled_tasks": self.scheduled_tasks
            }
        with open(self.STATE_FILE, "w") as file:
            json.dump(state, file, indent=4)
        print("ProcessManager: Task state saved.")

    def load_state(self):
        """Load tasks from a file."""
        try:
            with open(self.STATE_FILE, "r") as file:
                state = json.load(file)
            with self.lock:
                self.task_queue = state.get("task_queue", [])
                self.scheduled_tasks = state.get("scheduled_tasks", [])
            print("ProcessManager: Task state loaded.")
        except FileNotFoundError:
            print("ProcessManager: No saved state found.")
        except json.JSONDecodeError:
            print("ProcessManager: Error loading saved state.")

    def start_auto(self):
        """Start automatic task scheduling."""
        if not self.running:
            self.running = True
            self.start_scheduler()
            print("ProcessManager: Automatic scheduling started.")

    def stop_auto(self):
        """Stop automatic task scheduling."""
        self.running = False
        print("ProcessManager: Automatic scheduling stopped.")

    def start_scheduler(self):
        """Start the scheduler in a separate thread."""
        scheduler_thread = Thread(target=self._automatic_scheduler, daemon=True)
        scheduler_thread.start()
        print("ProcessManager: Scheduler thread started.")

    def _automatic_scheduler(self):
        """Internal method to run tasks automatically in the background."""
        while self.running:
            self.scheduler()
            time.sleep(1)  # Sleep to allow other processes
