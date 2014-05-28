def encode_single_vb(n):
    byts = []
    while True:
        byts.append(n % 128)
        if n < 128:
            break
        n //= 128
    byts = byts[::-1]
    byts[-1] += 128
    return [bin(n)[2:] for n in byts]


def encode_vb(numbers):
    bytestream = []
    for n in numbers:
        bytestream.extend(encode_single_vb(n))
    return bytestream


def decode_vb(bytestream):
    byts = utils.split_bytes(bytestream)

    lst = []
    aux = ''
    for byte in byts:
        if byte[0] == '0':
            print byte
            aux += byte[1:]
        else:
            print byte
            aux += byte[1:]
            number = utils.integer(aux)
            lst.append(number)
            aux = ''
    return lst
