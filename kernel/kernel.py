class Kernel:
    def __init__(self):
        """Initialize the Kernel."""
        self.process_table = []  # List to store process names
        self.memory = {}         # Dictionary to manage memory allocations
        print("Kernel: Initialized.")

    def manage_processes(self, action, process_name=None):
        """Manage process creation and termination."""
        if action == "create":
            if process_name not in self.process_table:
                self.process_table.append(process_name)
                print(f"Kernel: Process '{process_name}' created.")
            else:
                print(f"Kernel: Process '{process_name}' already exists.")
        elif action == "terminate":
            if process_name in self.process_table:
                self.process_table.remove(process_name)
                print(f"Kernel: Process '{process_name}' terminated.")
            else:
                print(f"Kernel: Process '{process_name}' not found.")

    def allocate_memory(self, process_name, size):
        """Allocate memory to a process."""
        if process_name in self.process_table:
            self.memory[process_name] = size
            print(f"Kernel: Allocated {size}MB to '{process_name}'.")
        else:
            print(f"Kernel: Cannot allocate memory. Process '{process_name}' does not exist.")

    def deallocate_memory(self, process_name):
        """Deallocate memory from a process."""
        if process_name in self.memory:
            print(f"Kernel: Deallocated memory from '{process_name}'.")
            del self.memory[process_name]
        else:
            print(f"Kernel: No memory to deallocate for '{process_name}'.")

    def display_process_table(self):
        """Display all active processes."""
        print("Kernel: Active Processes:")
        for process in self.process_table:
            print(f"- {process}")

    def display_memory_usage(self):
        """Display current memory allocations."""
        print("Kernel: Memory Usage:")
        for process, size in self.memory.items():
            print(f"- {process}: {size}MB")
