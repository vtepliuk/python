"""
Adding some functionalities for analyzer program
"""
def count_lines(text):
    """
    Count amount of non-empty lines in a text.
    """
    lines = text.split('\n')
    not_empty_lines = [line for line in lines if line.strip() != ""]
    return len(not_empty_lines)

def count_words(text):
    """
    Count amount of words in a text.
    """
    words = text.split()
    return len(words)

def count_letters(text):
    """
    Count amount of letters in a text.
    """
    letters = [char for char in text if char.isalpha()]
    return len(letters)

def get_word_count(item):
    """
    Sort words by frequency and alphabetically.
    """
    return -item[1], item[0]

def get_letter_count(item):
    """
    Sort letters by frequency and alphabetically.
    """
    return -item[1], item[0]


def word_frequency(text):
    """
    Analyze word frequency.
    """
    # Convert text to lowercase and remove punctuation manually
    text = text.lower()
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
    words = text.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Sort by frequency first, then alphabetically from Z to A
    sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
    total_words = len(words)

    return [(word, count, round((count / total_words) * 100, 1)) for word, count in sorted_word_count[:7]]


def letter_frequency(text):
    """
    Analyze letter frequency.
    """
    # Convert text to lowercase and remove non-alphabetic characters manually
    text = text.lower()
    letters = [char for char in text if char.isalpha()]
    letter_count = {}
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    sorted_letter_count = sorted(letter_count.items(), key=lambda item: (-item[1], item[0]))
    total_letters = len(letters)
    return [(letter, count, round((count / total_letters) * 100, 1)) for letter, count in sorted_letter_count[:7]]
