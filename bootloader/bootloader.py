class Bootloader:
    def __init__(self):
        """Initialize the Bootloader."""
        print("Bootloader: Starting system initialization...")

    def check_system(self):
        """Simulate system checks before loading the kernel."""
        print("Bootloader: Checking system integrity...")
        # Simulate checks
        checks_passed = True
        if checks_passed:
            print("Bootloader: System checks passed.")
        else:
            print("Bootloader: System checks failed. Halting.")
            exit(1)

    def load_kernel(self):
        """Simulate loading the kernel into memory."""
        print("Bootloader: Loading the Kernel into memory...")
        kernel_loaded = True
        if kernel_loaded:
            print("Bootloader: Kernel successfully loaded.")
            return True
        else:
            print("Bootloader: Kernel loading failed. Halting.")
            return False

    def start(self):
        """Simulate the boot process."""
        print("Bootloader: Starting boot process...")
        self.check_system()
        return self.load_kernel()
