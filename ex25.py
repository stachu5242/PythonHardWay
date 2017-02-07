def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words
def sort_words(words):
    """Sort the words."""
    return sorted(words)
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
def print_last_word(words):
    """Prints the last wordd"""
    word = words.pop(-1)
    return word
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_sentence(words)
def print_firts_and_last(sentence):
    "Pint the first and the last word of the sentence"
    words= break_words(sentence)
    print_first_word(words)
    print_last_word(words)
def print_first_and_last_sorted(sentence):
    """Sort the worrds then prints the firts and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
