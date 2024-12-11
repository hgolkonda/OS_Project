from bootloader.bootloader import Bootloader

bootloader = Bootloader()
if bootloader.start():
    print("Bootloader test completed successfully!")
else:
    print("Bootloader test failed.")
