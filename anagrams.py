def anagrams(word,words):
    li = []
    res = []
    li2= []
    for ch in word:
        if ch not in li:
            li += ch
    for i in range(len(words)):
        for ch2 in words[i]:
            if ch2 not in li2:
                li2 +=ch2
        if set(li2) == set(li) and len(words[i])==len(word) :
            res.append(words[i])
        i += 1
        li2 = []
    return res

print(anagrams('abba', ['bbaa', 'abcd', 'bbaa', 'dada']))