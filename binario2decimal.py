import unittest
def binario2decimal(numero_binario):
   decimal = int(numero_binario, 2)

   return decimal


class TestNumeracion(unittest.TestCase):
    def test_binario2decimal92(self):
        result = binario2decimal('01011100')
        self.assertEqual(result, 92)

    def test_binario2decimal15(self):
        result = binario2decimal('1111')
        self.assertEqual(result, 15)

    def test_binario2decimal99(self):
        result = binario2decimal('1100011')
        self.assertEqual(result, 99)        

if __name__ == '__main__':
    unittest.main()