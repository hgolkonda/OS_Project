from kernel.kernel import Kernel

# Initialize the kernel
kernel = Kernel()

# Test process management
kernel.manage_processes("create", "Process1")
kernel.manage_processes("create", "Process2")
kernel.display_process_table()

kernel.manage_processes("terminate", "Process1")
kernel.display_process_table()

# Test memory management
kernel.allocate_memory("Process2", 100)
kernel.display_memory_usage()

kernel.deallocate_memory("Process2")
kernel.display_memory_usage()
