import unittest

def decimal2binario(decimal):
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2

        return binario

class Test_numeracion(unittest.TestCase):
    def test_decimal2binario(decimal):



if __name__ == '__main__':
    unittest.main()