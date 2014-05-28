# coding=utf-8

# Funciones
def unario(n):
    """
    Pasa el número dado a unario, con un 0 al final

    :rtype : str
    :param n: Un número
    :return: El número dado en unario
    """
    return '1' * (n - 1) + '0'


def binario(n):
    """
    Pasa el número dado a binario

    :rtype : str
    :param n: Un número
    :return: El número en binario
    """
    return bin(n)[2:]


def integer(s):
    """
    Dado una string con un número en binario, devuelve el integer correspondiente.
    No se comprueba si la cadena es válida.

    :rtype : int
    :param s: Una binario en formato string
    :return: El número en integer
    """
    s = s[::-1]
    num = 0
    for i in xrange(len(s)):
        num += 2 ** i if s[i] == '1' else 0
    return num

def split_bytes(string):
    """
    Dado una string con un número en binario, devuelve una lista de strings de tamaño 8 (un byte)

    :rtype : list
    :param string: Un número en binario
    :return: La string dividida en strings de 8 carácteres
    """
    string = string[::-1]
    lst = []
    numbers = range(len(string)+1)[::8]
    for n, m in zip(numbers[:-1], numbers[1:]):
        lst.append(string[n:m][::-1])
    return lst[::-1]
