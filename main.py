from native_lib.gui_lib import *

# TODO: MODULES <- check modules existence

if __name__ == "__main__":
    print("\n__START PROGRAM__")
    print("INFO: Open GUI")
    root = Tk()
    app_service_sector = AppMainWindow(root)
    root.mainloop()
    # root.destroy()
    print("INFO: Close GUI")
    print("__STOP PROGRAM__\n")
