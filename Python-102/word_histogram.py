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
        
        def sorting_histogram(word_histogram):
            for word in sorted(words):
                print()
        return words



print(sorting_histogram())
        