import nltk
import sys

# Скачиваем необходимые ресурсы NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def count_pos_tags(text):
    """
    Функция для подсчета частей речи в тексте
    """
    # Токенизация текста
    tokens = nltk.word_tokenize(text)
    
    # POS-теггинг
    tagged_tokens = nltk.pos_tag(tokens)
    
    # Счетчики для разных частей речи
    adjectives = 0
    adverbs = 0
    verbs = 0
    
    # Подсчет частей речи
    for word, tag in tagged_tokens:
        if tag.startswith('JJ'):  # Прилагательные (JJ, JJR, JJS)
            adjectives += 1
        elif tag.startswith('RB'):  # Наречия (RB, RBR, RBS)
            adverbs += 1
        elif tag.startswith('VB'):  # Глаголы (VB, VBD, VBG, VBN, VBP, VBZ)
            verbs += 1
    
    return {
        'adjectives': adjectives,
        'adverbs': adverbs,
        'verbs': verbs
    }

def read_file(file_path):
    """
    Функция для чтения текста из файла
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Использование: python main.py <путь_к_файлу>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    text = read_file(file_path)
    
    results = count_pos_tags(text)
    
    print(f"Статистика частей речи в тексте:")
    print(f"Прилагательных: {results['adjectives']}")
    print(f"Наречий: {results['adverbs']}")
    print(f"Глаголов: {results['verbs']}")
    print(f"Всего проанализировано частей речи: {sum(results.values())}")

if __name__ == "__main__":
    main()
