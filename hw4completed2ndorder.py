import random
import numpy as np

#add the punctuation correctly in the array
def add_p(text):
    p = '.-!?'
    arr = text.split()
    for i in range(len(arr)-1):
        if arr[i][len(arr[i])-1] in p and len(arr[i])-1>0:
            arr.insert(i+1, arr[i][len(arr[i])-1])
            arr[i] = arr[i][0:len(arr[i])-1]
    return arr

#build the label matrix
def matrix_label(text):
    TML = []
    arr = add_p(text)
    for e in arr:
        listt = []
        for k in arr:
            listt.append((e,k))
        TML.append(listt)
    return TML

#build the transition matrix
def transition_matrix(TML, text):
    TM = []
    array = list(zip(add_p(text)[0:-1],punc_handle(text)[1:]))
    for i in range(len(TML)):
        listt = []
        for e in TML[i]:
            if e in array:
                listt.append(1)
            else:
                listt.append(0)
        TM.append(listt)
    for i in range(len(TM)):
        total = sum(TM[i])
        if total != 0:    
            for c in range(len(TM[i])):
                TM[i][c] /= total
    return TM

#convert from (a,b) to ['a b']
def convert(TML):
    listt = []
    for w in TML:
        print(TML)
        print(w)
        t = []
        for a,b in w:
            t.append(str(a) + ' ' + str(b))
        listt.append(t)
    return listt

#generate the text
def random_walk(TM, TML, text):
    sentence = ''
    TMLd = convert(TML)
    i = 0
    r = random.choice(range(len(TMLd)))
    word = ' '
    change = ''
    while change != '.':
        while sum(TM[r])!=1:
            r = random.choice(range(len(TMLd)))
        word = np.random.choice(TMLd[r], replace = False, p =TM[r])
        if len(sentence)==0:
            sentence +=word + ' '
        else:
            arr = word.split()
            sentence += arr[1] + ' '
        change = word.split()[len(word.split())-1]
        for u in range(len(TML)):
           for a,b in TML[u]:
               if change == a:
                    r = u
                    break
    sentence = sentence.replace('.', '')
    sentence = sentence.strip()
    sentence = sentence + '.'
    print(sentence)

text = input('')
random_walk(transition_matrix(matrix_label(text),text),matrix_label(text), text)
