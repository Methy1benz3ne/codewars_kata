def spin_words(sentence):
    '''detect if longer than 5 letters'''
    counter=0
    i = 0
    res=''
    words=''
    for ch in sentence:

        words += ch

        if ch == ' ':
            if counter <= 5:
                word2= words
                counter = 0
                words = ''
                res += word2
            else :
                words2 = words[::-1]
                res += words2
                counter=0
                words=''
        i += 1
        counter += 1
    return res

print(spin_words("We3o 222221111"))