import nltk

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

def main():
    print("Программа для подсчета частей речи в тексте")
    print("Пока не реализовано чтение из файла")

if __name__ == "__main__":
    main()
