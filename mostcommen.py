from collections import Counter
import re
from string import punctuation
def top_3_words(text):
    newword = []
    # text1 = text.split()
    for p in punctuation:
        if p != "'" :
            text = text.replace(p,' ')

    # text1 = re.sub(r"..", '', text)
    for word in text.split():
        if not (word == "\'" or word == "\'\'" or word =="'''") :
            newword.append(word.lower())
        # else:
        #     for ch in word:
        #         if not ch.isalnum():
        #             del ch
        #     newword.append(word.lower())
    res = count_most_commen(newword)
    return res



def count_most_commen(text):
    res = []
    res2 = []
    # s = "\tsdfsdf\rsdfdsfd\r"



    for i in set(text):
        i.strip()
        res.append([i,text.count(i)])
    res.sort(key= lambda x:x[1],reverse = True)
    if len(res) <= 3 :
        res1 = res
    else :
        res1 = res[0:3]
    for i in range(len(res1)):
        res2.append(res1[i][0])
    return res2

    # return

print(top_3_words("//wont won't won't '''"))
