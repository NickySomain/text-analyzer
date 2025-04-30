import unittest
from main import count_pos_tags

class TestPOSCounter(unittest.TestCase):
    def test_count_pos_tags(self):
        test_text = "This is a beautiful day. She runs quickly."
        result = count_pos_tags(test_text)
        
        # Проверяем, что функция возвращает словарь с правильными ключами
        self.assertIn('adjectives', result)
        self.assertIn('adverbs', result)
        self.assertIn('verbs', result)
        
        # Проверяем, что значения являются целыми числами
        self.assertIsInstance(result['adjectives'], int)
        self.assertIsInstance(result['adverbs'], int)
        self.assertIsInstance(result['verbs'], int)
        
        # Проверяем, что в тексте найдено хотя бы одно прилагательное и глагол
        self.assertGreaterEqual(result['adjectives'], 1)
        self.assertGreaterEqual(result['verbs'], 1)

if __name__ == '__main__':
    unittest.main()
