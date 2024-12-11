class Shell:
    def __init__(self, kernel, file_system, process_manager):
        self.kernel = kernel
        self.file_system = file_system
        self.process_manager = process_manager

    def start(self):
        """Start the shell interface."""
        print("Shell: Command-line interface started.")
        print("Type 'help' for a list of available commands.")
        while True:
            command = input("OS> ").strip().split()
            if not command:
                continue

            action = command[0].lower()

            # Task-related commands
            if action == "add" and len(command) == 4:
                try:
                    task_name = command[1]
                    interval = int(command[2])
                    memory_size = int(command[3])
                    self.process_manager.add_task(task_name, interval, memory_size)
                except ValueError:
                    print("Shell: Invalid interval or memory size. Please enter valid numbers.")
            elif action == "schedule" and len(command) == 3:
                task_name = command[1]
                time_str = command[2]
                self.process_manager.schedule_task(task_name, time_str)
            elif action == "remove" and len(command) == 2:
                task_name = command[1]
                self.process_manager.remove_task(task_name)
            elif action == "list":
                self.process_manager.list_tasks()
            elif action == "move" and len(command) == 3:
                source = command[1]
                destination = command[2]
                self.file_system.move(source, destination)
            elif action == "rename" and len(command) == 3:
                old_name = command[1]
                new_name = command[2]
                self.file_system.rename(old_name, new_name)

            elif action == "run":
                self.process_manager.scheduler()
            elif action == "memory":
                self.process_manager.memory_manager.show_memory_usage()
            elif action == "export_tasks" and len(command) == 2:
                filename = command[1]
                self.process_manager.export_tasks(filename)
            elif action == "import_tasks" and len(command) == 2:
                filename = command[1]
                self.process_manager.import_tasks(filename)
            elif action == "pause_task" and len(command) == 2:
                task_name = command[1]
                self.process_manager.pause_task(task_name)
            elif action == "resume_task" and len(command) == 2:
                task_name = command[1]
                self.process_manager.resume_task(task_name)
            elif action == "start_auto":
                self.process_manager.start_auto()
            elif action == "stop_auto":
                self.process_manager.stop_auto()

            # File system commands
            elif action == "create_file" and len(command) == 2:
                filename = command[1]
                self.file_system.create_file(filename)
            elif action == "write_file" and len(command) >= 3:
                filename = command[1]
                content = " ".join(command[2:])  # Combine all content after the filename
                self.file_system.write_file(filename, content)
            elif action == "read_file" and len(command) == 2:
                filename = command[1]
                self.file_system.read_file(filename)
            elif action == "list_files":
                self.file_system.list_files()
            elif action == "delete" and len(command) == 2:
                path = command[1]
                self.file_system.delete(path)
            elif action == "make_directory" and len(command) == 2:
                dir_name = command[1]
                self.file_system.make_directory(dir_name)
            elif action == "change_directory" and len(command) == 2:
                dir_name = command[1]
                self.file_system.change_directory(dir_name)

            # Help command
            elif action == "help":
                self.show_help()

            # Exit command
            elif action == "exit":
                print("Shell: Exiting...")
                break

            # Invalid command handling
            else:
                print("Shell: Invalid command or arguments. Type 'help' for assistance.")

    def show_help(self):
        """Display available commands and their usage."""
        print("Available Commands:")
        print("- add <task_name> <interval> <memory>: Add a periodic task.")
        print("- schedule <task_name> <HH:MM>: Schedule a task to run at a specific time.")
        print("- remove <task_name>: Remove a task.")
        print("- list: List all tasks (periodic and scheduled).")
        print("- run: Run all periodic tasks immediately.")
        print("- memory: Display memory usage.")
        print("- export_tasks <filename>: Export all tasks to a file.")
        print("- import_tasks <filename>: Import tasks from a file.")
        print("- pause_task <task_name>: Pause a specific task.")
        print("- resume_task <task_name>: Resume a paused task.")
        print("- start_auto: Start automatic scheduling.")
        print("- stop_auto: Stop automatic scheduling.")
        print("- create_file <filename>: Create an empty file.")
        print("- write_file <filename> <content>: Write content to a file.")
        print("- read_file <filename>: Read the content of a file.")
        print("- list_files: List all files in the current directory.")
        print("- delete <path>: Delete a file or directory.")
        print("- make_directory <dir_name>: Create a new directory.")
        print("- change_directory <dir_name>: Change to a specific directory.")
        print("- help: Display this help message.")
        print("- exit: Exit the shell.")
