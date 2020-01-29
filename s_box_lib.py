#import tqdm
import os
import hashlib

def get_sha512(data: str) -> bytes:
    hash = bytes(hashlib.sha512(data.encode()).hexdigest(), 'utf-8')
    return hash


def s_box_generator(iv: str) -> list:
    s_box = list()
    iteration_string = get_sha512(iv)

    while(True):
        if len(s_box) == 256:
            break
        else:
            iteration_string = get_sha512(str(iteration_string))
            for i in range(0,127,2):
                iteration_symbol = str(chr(iteration_string[i]))+str(chr(iteration_string[i+1]))
                if iteration_symbol not in s_box:
                    s_box.append(iteration_symbol)
                if len(s_box) == 256:
                    break

    return s_box


def substitute_data_block(data_block: bytes, s_box: list) -> bytes:
    data_block_code_mask = list()
    data_block_substitution_list_result = list()
    data_block_substitution_result = bytes()

    for i in range(0,len(data_block),2):
        data_symbols = str(chr(data_block[i]))+str(chr(data_block[i+1]))
        data_block_code_mask.append(int(data_symbols,16))
    #print(data_block_code_mask)

    for i in data_block_code_mask:
        data_block_substitution_list_result.append(s_box[i])
    #print(data_block_substitution_list_result)

    for i in data_block_substitution_list_result:
        data_block_substitution_result+=bytes(i.encode())
    
    return data_block_substitution_result


def resubstitute_data_block(data_block: bytes, s_box: list) -> bytes:
    data_block_symbols_list = list()
    data_block_resubstitution_list = list()
    data_block_resubstitution_result = bytes()


    for i in range(0,len(data_block),2):
        data_symbols = str(chr(data_block[i]))+str(chr(data_block[i+1]))
        data_block_symbols_list.append(data_symbols)
    #print(data_block_symbols_list)

    for i in data_block_symbols_list:
        data_block_resubstitution_list.append(hex(s_box.index(i)))
    #print(data_block_resubstitution_list)

    for i in data_block_resubstitution_list:
        iterator = str(i[2:])
        if len(iterator) == 1:
            iterator = '0' + iterator
        data_block_resubstitution_result += bytes(iterator.encode())

    return data_block_resubstitution_result


if __name__ == "__main__":
    
    print("\nSTART\n")

    iv = 'בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ'
    s_box = s_box_generator(iv)
    
    print()
    print(s_box)

    print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")

    data_block = "test"
    data_block = get_sha512(str(data_block))
    print(data_block)

    data_block_substitution_result = substitute_data_block(data_block, s_box)
    
    print(data_block_substitution_result)

    print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")

    data_block = data_block_substitution_result
    print(data_block)

    data_block_resubstitution_result = resubstitute_data_block(data_block,s_box)

    print(data_block_resubstitution_result)

    print("\nSTOP\n")
    input()