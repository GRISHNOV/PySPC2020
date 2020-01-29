import os
import hashlib
import time
import random
#from tqdm import tqdm

import s_box_lib

# TODO: MODULES <- check modules existence

KEY = 'test' # temporary
S_BOX = s_box_lib.s_box_generator('בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ') # temporary

def get_sha512(data: str) -> bytes:
    hash = bytes(hashlib.sha512(data.encode()).hexdigest(), 'utf-8')
    return hash


def get_xor_cipher(data: bytes, gamma: bytes) -> bytes:
    result = bytes([i ^ j for i, j in zip(data, gamma)])
    return result


def encrypt_file(fd_input, fd_output, key: str, iv: int) -> int:
    iv = get_sha512(str(iv))
    gamma = get_sha512(key)
    fd_output.write(get_xor_cipher(iv, gamma)) # header metadata
    gamma += iv

    #formatted_data = bytes()

    while True:
        data = fd_input.read(128)
        if len(data) == 0:
            return 0
        if len(data) == 128:
            #for iterator in data:
            #    iterator = str(hex(iterator))
            #    iterator = iterator[2:]
            #    if len(iterator) == 1:
            #        iterator = '0'+ iterator
            #    formatted_data += bytes(iterator.encode())
            # data = s_box_lib.substitute_data_block(data, S_BOX)
            #fd_output.write(get_xor_cipher(s_box_lib.substitute_data_block(formatted_data, S_BOX), gamma))
            fd_output.write(get_xor_cipher(data, gamma))
            gamma = get_sha512(str(gamma))
        if len(data) < 128:
            fd_output.write(get_xor_cipher(data, gamma[0:len(data)]))


def decrypt_file(fd_input, fd_output, key: str) -> int:
    gamma = get_sha512(key)
    iv = get_xor_cipher(fd_input.read(128), gamma)
    gamma += iv

    while True:
        data = fd_input.read(128)
        if len(data) == 0:
            return 0
        if len(data) == 128:
            #data = s_box_lib.resubstitute_data_block(data, S_BOX)
            fd_output.write(get_xor_cipher(data, gamma))
            gamma = get_sha512(str(gamma))
        if len(data) < 128:
            fd_output.write(get_xor_cipher(data, gamma[0:len(data)]))


if __name__ == "__main__":

    print("__START__\n")

    input_filename = input("Input filename:")
    output_filename = input("Output filename:")

    # TODO: FILES <- check file existence

    fd_input = open(input_filename, "rb")
    #size = os.path.getsize(input_filename)
    fd_output = open(output_filename, "wb")

    # TODO: KEY <- user input
    # TODO: IV <- get with good entropy

    iv = time.time_ns()
    gamma = get_sha512(KEY)

    encrypt_file(fd_input, fd_output, KEY, iv) # TODO: process return code

    fd_input.close()
    fd_output.close()

    input()

    input_filename = input("Input filename:")
    output_filename = input("Output filename:")

    fd_input = open(input_filename, "rb")
    #size = os.path.getsize(input_filename)
    fd_output = open(output_filename, "wb")

    decrypt_file(fd_input, fd_output, KEY) # TODO: process return code

    fd_input.close()
    fd_output.close()

    print("\n__STOP__")
    input()