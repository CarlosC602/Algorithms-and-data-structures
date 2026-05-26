import time

def import_text(path):
    with open(path, encoding='utf-8') as f:
        text = f.readlines()
    return ' '.join(text).lower()

S = import_text("lotr.txt")
W = "time."

def naive_method(text, sample):
    t_start = time.perf_counter()
    counter = 0
    indexes = []
    comparisons = 0
    for i in range(len(text) - len(sample) + 1):
        letter_counter = 0
        for j in range(len(sample)):
            comparisons += 1
            if text[i + j] == sample[j]:
                letter_counter += 1
            else:
                break
        if letter_counter == len(sample):
            indexes.append(i)
            counter += 1
    t_stop = time.perf_counter()
    t = t_stop - t_start
    return (counter, t, indexes, comparisons)

counter, tim, ind, comp = naive_method(S, W)
print(f'{counter};{comp};{tim}')


def Hash(word):
    hash = 0
    for i in range(len(word)):
        hash = (hash * 256 + ord(word[i])) % 101
    return hash

def Rabin_Karp_method(text, sample):
    t_start = time.perf_counter()
    hash = Hash(sample)
    counter = 0
    indexes = []
    comparisons = 0
    colyssions = 0
    for i in range(len(text) - len(sample) + 1):
        word = text[i : i + len(sample)]
        hash_text = Hash(word)
        comparisons += 1
        if hash_text == hash:
            if word == sample:
                counter += 1
                indexes.append(i)
            else:
                colyssions += 1
    t_stop = time.perf_counter()
    t = t_stop - t_start
    return (counter, t, indexes, comparisons, colyssions)

counter, tim, ind, comp, colyssions = Rabin_Karp_method(S, W)
print(f'{counter};{comp};{colyssions};{tim}')


def Rabin_Karp_mod(text, sample):
    t_start = time.perf_counter()
    hash = Hash(sample)
    counter = 0
    indexes = []
    comparisons = 0
    colyssions = 0
    d = 256
    q = 101

    h = 1
    for _ in range(len(sample) - 1): 
        h = (h*d) % q 

    word = text[0 : len(sample)]
    hash_text = Hash(word)

    for i in range(len(text) - len(sample) + 1):
        comparisons += 1
        if hash_text == hash:
            word = text[i : i + len(sample)]
            if word == sample:
                counter += 1
                indexes.append(i)
            else:
                colyssions += 1
        if i < len(text) - len(sample):
            hash_text = (d * (hash_text - ord(text[i]) * h) + ord(text[i + len(sample)])) % q
        if hash_text < 0:
            while hash_text < 0:
                hash_text += q
    t_stop = time.perf_counter()
    t = t_stop - t_start
    return (counter, t, indexes, comparisons, colyssions)

counter, tim, ind, comp, colyssions = Rabin_Karp_mod(S, W)
print(f'{counter};{comp};{colyssions};{tim}')
