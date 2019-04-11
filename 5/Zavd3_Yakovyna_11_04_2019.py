def sorting(sentence):
    words = sentence.split()
    for i in range(len(words)):
        for j in range(len(words) - i - 1):
            if words[j].lower() > words[j + 1].lower():
                words[j], words[j + 1] = words[j + 1], words[j]
    return words

s = sorting("Drink vodka and nothing more")
print(s)