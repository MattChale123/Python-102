user_input = input('Please enter a sentence. ')

def word_histogram(string):
    counts = {}
    words = string.split(' ')
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

words = word_histogram(user_input)

def sorting_histogram(words):
    for word in sorted(words, key=words.get, reverse=True):
        print(word, words[word])
    return(words)
sorting_histogram(words)