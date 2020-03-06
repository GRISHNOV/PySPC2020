import time
from tkinter import *
from native_lib.s_box_lib import *
from native_lib.crypto_lib import *

# TODO: MODULES <- check modules existence

KEY = 'test'  # temporary example
S_BOX = s_box_generator('בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ')  # temporary example


if __name__ == "__main__":
    print("__START__\n")
    input_filename = input("Input filename:")
    output_filename = input("Output filename:")
    # TODO: FILES <- check file existence
    fd_input = open(input_filename, "rb")
    fd_output = open(output_filename, "wb")
    # TODO: KEY <- user input
    # TODO: IV <- get with good entropy
    iv = time.time_ns()
    gamma = get_sha512(KEY)
    encrypt_file(fd_input, fd_output, KEY, iv)  # TODO: process return code
    fd_input.close()
    fd_output.close()
    input()
    input_filename = input("Input filename:")
    output_filename = input("Output filename:")
    fd_input = open(input_filename, "rb")
    fd_output = open(output_filename, "wb")
    decrypt_file(fd_input, fd_output, KEY)  # TODO: process return code
    fd_input.close()
    fd_output.close()
    print("\n__STOP__")
    input()