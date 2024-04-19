from io import StringIO
import unittest

"""Para hacer que las pruebas corra importamos sys"""
import sys
from unittest.mock import patch
sys.path.append("src")


from console.huffman_menu import HuffmanMenu
from logica.huffman_cleanCode import HuffmanCoding


class TestHuffmanCoding(unittest.TestCase):
    
    SPECIAL_CHARACTER_TEST = "!@#$%^&*()"
    WORD_TEST = "abracadabra"
    REPEATED_CHARACTERS_TEST = "aaaaabbbbccccc"
    
    def test_encode_normal_text(self):
        """Prueba normal: Comprime un texto normal y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.WORD_TEST)
        expected_result = "110111001100110010110110001101101111110011011100110011001011011"
        self.assertEqual(encoded, expected_result)

    def test_decode_normal_text(self):
        """Prueba normal: Descomprime un texto normal y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.WORD_TEST)
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, self.WORD_TEST)

    def test_encode_special_characters(self):
        """Prueba normal: Comprime un texto con caracteres especiales y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.SPECIAL_CHARACTER_TEST)
        expected_result = "0101000001111010011010010101100111000101110101010100101110010101001000"
        self.assertEqual(encoded, expected_result)

    def test_decode_special_characters(self):
        """Prueba normal: Descomprime un texto con caracteres especiales y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.SPECIAL_CHARACTER_TEST)
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, self.SPECIAL_CHARACTER_TEST)

    def test_encode_repeated_characters(self):
        """Prueba normal: Comprime un texto con caracteres repetidos y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.REPEATED_CHARACTERS_TEST)
        expected_result = "11011110111101111011110111001100100110010011001001100000110000110000110000110000110"
        self.assertEqual(encoded, expected_result)

    def test_decode_repeated_characters(self):
        """Prueba normal: Descomprime un texto con caracteres repetidos y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.REPEATED_CHARACTERS_TEST)
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, self.REPEATED_CHARACTERS_TEST)

    def test_none_text(self):
        """Prueba excepcional: Intenta comprimir un texto que es None y verifica la excepción"""
        with self.assertRaises(ValueError):
            coding = HuffmanCoding()
            coding.encode(None)

    def test_empty_text(self):
        """Prueba excepcional: Descomprime un texto con texto vacío y verifica la excepción"""
        with self.assertRaises(ValueError):
            coding = HuffmanCoding()
            coding.decode("")
            
    def test_encode_invalid_text_type(self):
        """Prueba excepcional: Intenta comprimir un texto que no es de tipo string y verifica la excepción"""
        coding = HuffmanCoding()
        with self.assertRaises(TypeError):
            coding.encode(123)

    def test_decode_long_text(self):
        """Prueba de error: Descomprime un texto largo y verifica que el resultado sea igual al texto original"""
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        coding = HuffmanCoding()
        encoded = coding.encode(text)
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, text)

    def test_decode_invalid_character_in_encoded_text(self):
        """Prueba de error: Intenta descomprimir un texto codificado con caracteres inválidos y verifica la excepción"""
        coding = HuffmanCoding()
        with self.assertRaises(ValueError):
            coding.decode("1010abc10101")
    
    def test_encode_invalid_text_length(self):
        """Prueba de error: Intenta comprimir un texto muy corto y verifica la excepción"""
        coding = HuffmanCoding()
        with self.assertRaises(ValueError):
            coding.encode("a")

    def test_decode_invalid_encoded_data_format(self):
        """Prueba de error: Intenta descomprimir datos codificados con formato incorrecto y verifica la excepción"""
        coding = HuffmanCoding()
        with self.assertRaises(ValueError):
            coding.decode("1a0b1c0d1a0b1c0d")
    
    def test_encode_decode_simple_text(self):
        hc = HuffmanCoding()
        text = "hello"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

    def test_encode_decode_special_characters(self):
        hc = HuffmanCoding()
        text = "!@#$%^&*"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

    def test_encode_decode_long_text(self):
        hc = HuffmanCoding()
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

    def test_encode_decode_single_character(self):
        hc = HuffmanCoding()
        text = "aaaaaaa"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

    def test_encode_decode_text(self):
        hc = HuffmanCoding()
        text = "hello world"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

    def test_encode_decode_special_characters(self):
        hc = HuffmanCoding()
        text = "!@#$%^&*()"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)
        
    def test_encode_decode_mixed_case_characters(self):
        hc = HuffmanCoding()
        text = "AbCdEfGhIjKlMnOpQrStUvWxYz"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

if __name__ == '__main__':
    unittest.main()



