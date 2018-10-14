import string
def pig_it(text):
    words = text.split()
    word1 = ''
    for word in words :
        if word not in string.punctuation:
            word1 += word[1:]+word[0]+'ay'+ ' '
        else :
            word1 += word+ ' '
    # res =  join()
    res = word1
    return word1[:-1]

print(pig_it('This is my string !'))

