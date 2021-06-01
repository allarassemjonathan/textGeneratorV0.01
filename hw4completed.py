from collections import defaultdict
import random

def markov_chain():
    f = open(r'C:\Users\ALLARASSEMJJ20\Achilles\Frankeshtein.txt', encoding = 'utf-8')
    text = f.read()
    forb = '''±¬¤¸£×¥¿*¶¼¦¹¯§¾´ª½¢¡®…³=²º¨0123456789!→°‘()[]{};:'“”"«»\,+<>/?@#$%^&*_~©'''
    for l in text:
        if l in forb:
            text = text.replace(l, ' ')
            
    arr = text.split()
    p = '.-!?'
    for i in range(len(arr)-1):
        if arr[i][len(arr[i])-1] in p and len(arr[i])-1>0:
            arr.insert(i+1, arr[i][len(arr[i])-1])
            arr[i] = arr[i][0:len(arr[i])-1]
        
    dico = defaultdict(list)
    for a,b in zip(arr[0:-1],arr[1:]):
        dico[a].append(b)
    return dico

def textGenerator():
    s = ''
    array = []
    dic = markov_chain()
    arr = list(dic.keys())
    start = []
    
    for e in arr:
        if e == e.capitalize():
            start.append(e)
    word = ''
    while word != '.':
        if len(array) == 0:
                word = random.choice(start)
                s += word + ' '
                array.append(word)
        else:
                word = random.choice(dic[array[len(array)-1]])
                s += word + ' '
                array.append(word)
    return s

print(textGenerator())
