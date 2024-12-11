import threading
import time


class InterruptHandler:
    def __init__(self):
        """Initialize the interrupt handler."""
        self.interrupts = {}  # Dictionary to store interrupt types and their handlers
        self.running = False  # Flag to control the interrupt loop
        self.lock = threading.Lock()  # Thread safety
        self.timer_interval = 5  # Default timer interval in seconds

    def register_interrupt(self, interrupt_type, handler):
        """Register a handler for a specific interrupt type."""
        with self.lock:
            self.interrupts[interrupt_type] = handler
            print(f"InterruptHandler: Registered interrupt '{interrupt_type}'.")

    def trigger_interrupt(self, interrupt_type, *args, **kwargs):
        """Trigger an interrupt and call the associated handler."""
        with self.lock:
            if interrupt_type in self.interrupts:
                print(f"InterruptHandler: Handling interrupt '{interrupt_type}'...")
                self.interrupts[interrupt_type](*args, **kwargs)
            else:
                print(f"InterruptHandler: Unknown interrupt '{interrupt_type}'.")

    def start(self):
        """Start the interrupt loop in a separate thread."""
        if not self.running:
            self.running = True
            threading.Thread(target=self._interrupt_loop, daemon=True).start()
            print("InterruptHandler: Interrupt loop started.")

    def stop(self):
        """Stop the interrupt loop."""
        self.running = False
        print("InterruptHandler: Interrupt loop stopped.")

    def _interrupt_loop(self):
        """Internal loop to trigger timer interrupts periodically."""
        while self.running:
            time.sleep(self.timer_interval)  # Wait for the timer interval
            self.trigger_interrupt("timer")

    def set_timer_interval(self, interval):
        """Set a new interval for timer interrupts."""
        with self.lock:
            if interval > 0:
                self.timer_interval = interval
                print(f"InterruptHandler: Timer interval set to {self.timer_interval} seconds.")
            else:
                print("InterruptHandler: Invalid interval. Must be greater than 0.")
