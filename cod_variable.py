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
