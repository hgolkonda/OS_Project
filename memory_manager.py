class MemoryManager:
    def __init__(self, total_memory):
        self.total_memory = total_memory  # Total available memory (in MB)
        self.allocated_memory = {}       # Tracks memory allocation by task

    def allocate_memory(self, task_name, memory_size):
        """Allocate memory for a task."""
        current_usage = sum(self.allocated_memory.values())
        if current_usage + memory_size > self.total_memory:
            print(f"MemoryManager: Not enough memory to allocate for '{task_name}'.")
            return False
        self.allocated_memory[task_name] = memory_size
        print(f"MemoryManager: Allocated {memory_size}MB for '{task_name}'.")
        return True

    def deallocate_memory(self, task_name):
        """Deallocate memory for a task."""
        if task_name in self.allocated_memory:
            print(f"MemoryManager: Deallocated {self.allocated_memory[task_name]}MB from '{task_name}'.")
            del self.allocated_memory[task_name]
        else:
            print(f"MemoryManager: Task '{task_name}' not found in allocated memory.")

    def show_memory_usage(self):
        """Show memory usage."""
        current_usage = sum(self.allocated_memory.values())
        print(f"MemoryManager: Total Memory: {self.total_memory}MB")
        print(f"MemoryManager: Allocated Memory: {current_usage}MB")
        print(f"MemoryManager: Free Memory: {self.total_memory - current_usage}MB")
        print("MemoryManager: Task Memory Allocation:")
        for task, size in self.allocated_memory.items():
            print(f"  - {task}: {size}MB")
