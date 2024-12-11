import os
import shutil

class FileSystem:
    def __init__(self):
        """Initialize the file system."""
        self.current_directory = os.getcwd()
        print(f"FileSystem: Current directory set to {self.current_directory}")

    def list_files(self):
        """List all files and directories in the current directory."""
        try:
            print(f"Contents of '{self.current_directory}':")
            for item in os.listdir(self.current_directory):
                item_path = os.path.join(self.current_directory, item)
                if os.path.isfile(item_path):
                    size = os.path.getsize(item_path)
                    print(f"- File: {item} ({size} bytes)")
                elif os.path.isdir(item_path):
                    print(f"- Directory: {item}")
        except Exception as e:
            print(f"Error listing files: {e}")

    def make_directory(self, dir_name):
        """Create a new directory."""
        try:
            path = os.path.join(self.current_directory, dir_name)
            os.mkdir(path)
            print(f"Directory '{dir_name}' created.")
        except Exception as e:
            print(f"Error creating directory '{dir_name}': {e}")

    def delete(self, path):
        """Delete a file or directory."""
        try:
            full_path = os.path.join(self.current_directory, path)
            if os.path.isfile(full_path):
                os.remove(full_path)
                print(f"Deleted file: {path}")
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)
                print(f"Deleted directory: {path}")
            else:
                print(f"Path '{path}' does not exist.")
        except Exception as e:
            print(f"Error deleting '{path}': {e}")

    def change_directory(self, dir_name):
        """Change to a different directory."""
        try:
            new_dir = os.path.join(self.current_directory, dir_name)
            os.chdir(new_dir)
            self.current_directory = os.getcwd()
            print(f"Changed directory to {self.current_directory}.")
        except FileNotFoundError:
            print(f"Directory '{dir_name}' not found.")
        except Exception as e:
            print(f"Error changing directory: {e}")

    def create_file(self, filename):
        """Create an empty file."""
        try:
            file_path = os.path.join(self.current_directory, filename)
            with open(file_path, "w") as file:
                print(f"File '{filename}' created.")
        except Exception as e:
            print(f"Error creating file '{filename}': {e}")

    def write_file(self, filename, content):
        """Write content to a file."""
        try:
            file_path = os.path.join(self.current_directory, filename)
            with open(file_path, "w") as file:
                file.write(content)
            print(f"Content written to '{filename}'.")
        except Exception as e:
            print(f"Error writing to file '{filename}': {e}")

    def read_file(self, filename):
        """Read content from a file."""
        try:
            file_path = os.path.join(self.current_directory, filename)
            with open(file_path, "r") as file:
                content = file.read()
            print(f"Content of '{filename}':\n{content}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")
