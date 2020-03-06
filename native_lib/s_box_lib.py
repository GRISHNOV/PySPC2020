from .crypto_lib import *


def s_box_generator(iv: str) -> list:
    """
    Creating an s-box (16x16) using a string as the initialization vector.
    """
    s_box = list()
    iteration_string = get_sha512(iv)
    while True:
        if len(s_box) == 256:
            break
        else:
            iteration_string = get_sha512(str(iteration_string))
            for i in range(0, 127, 2):
                iteration_symbol = str(chr(iteration_string[i]))+str(chr(iteration_string[i+1]))
                if iteration_symbol not in s_box:
                    s_box.append(iteration_symbol)
                if len(s_box) == 256:
                    break
    return s_box


def substitute_data_block(data_block: bytes, s_box: list) -> bytes:
    """
    Application of s-box to replace the data.
    """
    data_block_code_mask = list()
    data_block_substitution_list_result = list()
    data_block_substitution_result = bytes()
    for i in range(0,len(data_block),2):
        data_symbols = str(chr(data_block[i]))+str(chr(data_block[i+1]))
        data_block_code_mask.append(int(data_symbols, 16))
    for i in data_block_code_mask:
        data_block_substitution_list_result.append(s_box[i])
    for i in data_block_substitution_list_result:
        data_block_substitution_result += bytes(i.encode())
    return data_block_substitution_result


def resubstitute_data_block(data_block: bytes, s_box: list) -> bytes:
    """
    Reverse function to the s-box replacement function.
    """
    data_block_symbols_list = list()
    data_block_resubstitution_list = list()
    data_block_resubstitution_result = bytes()
    for i in range(0,len(data_block),2):
        data_symbols = str(chr(data_block[i]))+str(chr(data_block[i+1]))
        data_block_symbols_list.append(data_symbols)
    for i in data_block_symbols_list:
        data_block_resubstitution_list.append(hex(s_box.index(i)))
    for i in data_block_resubstitution_list:
        iterator = str(i[2:])
        if len(iterator) == 1:
            iterator = '0' + iterator
        data_block_resubstitution_result += bytes(iterator.encode())
    return data_block_resubstitution_result


if __name__ == "__main__":
    pass
