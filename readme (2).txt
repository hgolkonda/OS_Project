
# Automation OS

## Overview
**Automation OS** is a lightweight and modular operating system designed to simplify task automation and management. It provides a command-line interface for managing repetitive tasks, handling files, managing memory dynamically, and responding to system events using interrupt handling.

## Features
### 1. **Task Management**
- Add, remove, list, and schedule tasks.
- Pause and resume tasks.
- Export and import tasks to/from JSON files.

### 2. **Memory Management**
- Dynamically allocate and deallocate memory for tasks.
- Display memory usage (allocated and free memory).

### 3. **File System Operations**
- Create, read, write, and delete files.
- List files and directories.
- Move and rename files or directories.

### 4. **Interrupt Handling**
- Handle timer interrupts for periodic tasks.
- Handle I/O interrupts for events like file creation.
- Log interrupt activities for auditing.

### 5. **Persistent State**
- Automatically save and restore tasks between system restarts.

### 6. **Interactive Shell**
- User-friendly command-line interface.
- Commands include `add`, `remove`, `list_files`, `rename`, `move`, `memory`, and more.

## Installation Steps

### Prerequisites
- **Python 3.8+** must be installed.
- Basic familiarity with using the command-line interface.

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Automation-OS.git
   cd Automation-OS
   ```

2. **Set Up the Environment**:
   - Ensure required modules are available:
     ```bash
     pip install -r requirements.txt
     ```
   - (Optional) Create a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Run the Project**:
   ```bash
   python3 main.py
   ```

## Functions Implemented

### **Task Management**
- **Command**: `add <task_name> <interval_in_seconds> <memory_in_mb>`
  - Adds a periodic task with a specified interval and memory requirement.
  - Example:
    ```
    OS> add backup_script.sh 60 50
    ```

- **Command**: `schedule <task_name> <time>`
  - Schedules a task to run at a specific time.
  - Example:
    ```
    OS> schedule cleanup_logs 14:30
    ```

- **Command**: `pause_task <task_name>` and `resume_task <task_name>`
  - Pauses or resumes a task.

- **Command**: `list`
  - Lists all active tasks with their intervals or scheduled times.

### **Memory Management**
- **Command**: `memory`
  - Displays memory usage:
    ```
    Total: 512MB, Allocated: 100MB, Free: 412MB
    ```

### **File System**
- **Command**: `create_file <filename>`
  - Creates a new empty file.

- **Command**: `write_file <filename> <content>`
  - Writes content to the specified file.

- **Command**: `read_file <filename>`
  - Reads and displays the content of a file.

- **Command**: `rename <old_name> <new_name>`
  - Renames a file or directory.

- **Command**: `move <source> <destination>`
  - Moves a file or directory to a new location.

- **Command**: `list_files`
  - Lists all files and directories in the current directory.

### **Interrupt Handling**
- Timer Interrupt: Executes periodic tasks.
- I/O Interrupt: Responds to file creation events.
- Logged in `interrupts.log` for auditing.

## Usage Examples
1. **Add and Schedule Tasks**:
   ```bash
   OS> add task1 30 20
   OS> schedule task2 15:00
   ```

2. **File Operations**:
   ```bash
   OS> create_file notes.txt
   OS> write_file notes.txt "Meeting at 3 PM."
   OS> read_file notes.txt
   OS> rename notes.txt meeting_notes.txt
   OS> move meeting_notes.txt project_folder/
   ```

3. **View Memory Usage**:
   ```bash
   OS> memory
   Total: 512MB, Allocated: 50MB, Free: 462MB
   ```

4. **Handle Interrupts**:
   - Timer interrupts automatically run every 5 seconds (default).
   - Simulated file creation triggers I/O interrupt:
     ```bash
     File 'test_interrupt.txt' created.
     I/O Interrupt: File 'test_interrupt.txt' was created!
     ```

## Contribution
Feel free to contribute to this project by submitting issues or feature requests in the GitHub repository.

## License
This project is licensed under the MIT License.
