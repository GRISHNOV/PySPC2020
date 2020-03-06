import hashlib


def get_sha512(data: str) -> bytes:
    """
    Calculating the SHA512 hash from a UTF - 8 encoded data string.
    Returns a value as a byte list.
    """
    return bytes(hashlib.sha512(data.encode()).hexdigest(), 'utf-8')


def get_xor_cipher(data: bytes, gamma: bytes) -> bytes:
    """
    Implementation of The Vernam stream cipher .
    Adds (mod 2) a byte list to the gamma byte list.
    """
    return bytes([i ^ j for i, j in zip(data, gamma)])


def encrypt_file(fd_input, fd_output, key: str, iv: int) -> int:
    """
    Encrypting a file on disk.
    Returns the result code.
    """
    iv = get_sha512(str(iv))
    gamma = get_sha512(key)
    fd_output.write(get_xor_cipher(iv, gamma)) # header metadata
    gamma += iv
    while True:
        data = fd_input.read(128)
        if len(data) == 0:
            return 0
        if len(data) == 128:
            fd_output.write(get_xor_cipher(data, gamma))
            gamma = get_sha512(str(gamma))
        if len(data) < 128:
            fd_output.write(get_xor_cipher(data, gamma[0:len(data)]))


def decrypt_file(fd_input, fd_output, key: str) -> int:
    """
    Decrypting a file on disk.
    Returns the result code.
    """
    gamma = get_sha512(key)
    iv = get_xor_cipher(fd_input.read(128), gamma)
    gamma += iv
    while True:
        data = fd_input.read(128)
        if len(data) == 0:
            return 0
        if len(data) == 128:
            fd_output.write(get_xor_cipher(data, gamma))
            gamma = get_sha512(str(gamma))
        if len(data) < 128:
            fd_output.write(get_xor_cipher(data, gamma[0:len(data)]))


if __name__ == "__main__":
    pass
