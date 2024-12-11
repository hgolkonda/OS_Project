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
            file_list = []
            print(f"Contents of '{self.current_directory}':")
            for item in os.listdir(self.current_directory):
                file_list.append(item)
                item_path = os.path.join(self.current_directory, item)
                if os.path.isfile(item_path):
                    size = os.path.getsize(item_path)
                    print(f"- File: {item} ({size} bytes)")
                elif os.path.isdir(item_path):
                    print(f"- Directory: {item}")
            return file_list
        except Exception as e:
            print(f"Error listing files: {e}")
            return []

    def make_directory(self, dir_name):
        """Create a new directory."""
        try:
            path = os.path.join(self.current_directory, dir_name)
            os.mkdir(path)
            print(f"Directory '{dir_name}' created.")
        except FileExistsError:
            print(f"Error: Directory '{dir_name}' already exists.")
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
        except FileExistsError:
            print(f"Error: File '{filename}' already exists.")
        except Exception as e:
            print(f"Error creating file '{filename}': {e}")

    def write_file(self, filename, content):
        """Write content to a file."""
        try:
            file_path = os.path.join(self.current_directory, filename)
            with open(file_path, "w") as file:
                file.write(content)
            print(f"Content written to '{filename}'.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' does not exist.")
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

    def move(self, source, destination):
        """Move a file or directory to a new location."""
        try:
            source_path = os.path.join(self.current_directory, source)
            destination_path = os.path.join(self.current_directory, destination)

            if not os.path.exists(source_path):
                print(f"Error: Source '{source}' does not exist.")
                return

            # If the destination is a directory, append the source name
            if os.path.isdir(destination_path):
                destination_path = os.path.join(destination_path, os.path.basename(source_path))

            shutil.move(source_path, destination_path)
            print(f"Moved '{source}' to '{destination}'.")
        except Exception as e:
            print(f"Error moving '{source}' to '{destination}': {e}")

    def rename(self, old_name, new_name):
        """Rename a file or directory."""
        try:
            old_path = os.path.join(self.current_directory, old_name)
            new_path = os.path.join(self.current_directory, new_name)

            if not os.path.exists(old_path):
                print(f"Error: Path '{old_name}' does not exist.")
                return

            os.rename(old_path, new_path)
            print(f"Renamed '{old_name}' to '{new_name}'.")
        except Exception as e:
            print(f"Error renaming '{old_name}' to '{new_name}': {e}")
