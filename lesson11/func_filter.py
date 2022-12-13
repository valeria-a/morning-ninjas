def filter_upper_words(word):
    return not word.isupper()

filter(filter_upper_words, ["hello", 'hi', "WORLD", "yes"])
filter_obj = filter(filter_upper_words, ["hello", 'hi', "WORLD", "yes"])
print(list(filter_obj))


filter_obj = filter(str.islower, ["hello", 'hi', "WORLD", "yes"])
print(set(filter_obj))


