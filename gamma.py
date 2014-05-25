def encode_gamma(n):
    # Pasamos el número a binario
    offset = utils.binario(n)
    # y le quitamos el primer dígito
    offset = offset[1:]  

    # Pasamos a unario la longitud del offset + 1
    length = len(offset)+1   
    length = utils.unario(length)
    
    return length, offset


def decode_gamma(code):
    nums = []
    while code.find('0') > 0:
        # Buscamos el primer cero
        indx = code.find('0')

        # Cogemos desde el principio hasta el primer cero
        length = code[:indx]
        # El número de '1' nos indica el tamaño del offset
        size = len(length)

        # Cogemos desde después del primer cero, hasta 'offset' bits
        offset = code[indx+1:indx+1+size]
        # Le añadimos un '1' a la izquierda
        offset = '1' + offset
        # Y lo pasamos a decimal.
        num = utils.integer(offset)

        nums.append(num)
        code = code[2*size+1:]
    return nums
