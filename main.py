from bootloader.bootloader import Bootloader
from kernel.kernel import Kernel
from shell import Shell
from file_system import FileSystem
from process_manager import ProcessManager
from memory_manager import MemoryManager
from interrupt_handler import InterruptHandler  # Import InterruptHandler
import threading
import time


if __name__ == "__main__":
    # Bootloader
    bootloader = Bootloader()

    # Boot the OS
    if bootloader.start():
        try:
            # Initialize Kernel
            kernel = Kernel()

            # Initialize File System
            file_system = FileSystem()

            # Initialize Memory Manager
            total_memory = 512  # Example: 512 MB
            memory_manager = MemoryManager(total_memory)
            print("MemoryManager: Initialized with 512MB total memory.")

            # Initialize Process Manager with memory management
            process_manager = ProcessManager(total_memory)

            # Load saved state
            process_manager.load_state()

            # Initialize Interrupt Handler
            interrupt_handler = InterruptHandler()

            # Register Timer Interrupt
            def timer_handler():
                print("Timer Interrupt: A periodic task executed.")

            interrupt_handler.register_interrupt("timer", timer_handler)

            # Register I/O Interrupt
            def io_handler(filepath):
                print(f"I/O Interrupt: File '{filepath}' was created!")

            interrupt_handler.register_interrupt("file_created", io_handler)

            # Start Interrupt Handler
            interrupt_handler.start()

            # Simulate File Creation (I/O Interrupt)
            def simulate_file_creation():
                """Simulate a file being created after a delay."""
                time.sleep(10)  # Wait 10 seconds
                filepath = "test_interrupt_file.txt"
                with open(filepath, "w") as file:
                    file.write("This is a test file for interrupts.")
                interrupt_handler.trigger_interrupt("file_created", filepath)

            threading.Thread(target=simulate_file_creation, daemon=True).start()

            # Optionally Change Timer Interval
            interrupt_handler.set_timer_interval(5)  # Timer interrupt every 5 seconds

            # Start Shell
            shell = Shell(kernel, file_system, process_manager)
            shell.start()

        except KeyboardInterrupt:
            print("\nOS: Received shutdown signal. Shutting down gracefully...")

        finally:
            # Save state on shutdown
            process_manager.save_state()

            # Stop Interrupt Handler
            interrupt_handler.stop()
            print("OS: Shut down complete.")
    else:
        print("System halted due to bootloader failure.")
