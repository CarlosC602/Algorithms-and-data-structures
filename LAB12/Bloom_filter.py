import math
import time

def import_text(path):
    with open(path, encoding='utf-8') as f:
        text = f.readlines()
    return ' '.join(text).lower()

S = import_text("lotr.txt")

def Hash(word, q):
    hash = 0
    for i in range(len(word)):
        hash = (hash * 256 + ord(word[i])) % q
    return hash

def Bloom_filter(text, samples, P = 0.001, n = 20):
    t_start = time.perf_counter()

    b = (-n * math.log(P)) / (math.log(2)**2)
    b = math.ceil(b)
    k = (b / n) * math.log(2)
    k = math.ceil(k)

    bloom = [0] * b
    counter = dict.fromkeys(samples, 0)
    comparisons = 0
    colyssions = 0
    d = 256

    all_primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 
                  151, 157, 163, 167, 173, 179, 181, 191, 193, 197]
    q = all_primes[:k]

    for s in samples:
        for Q in q:
            HASH = Hash(s, Q) % b
            bloom[HASH] = 1

    h_list = [] 
    N = len(samples[0])
    for Q in q:
        h = 1
        for _ in range(N - 1): 
            h = (h * d) % Q
        h_list.append(h)

    current_hashes = [] 
    first_window = text[0:N] 
    for Q in q:
        current_hashes.append(Hash(first_window, Q))

    for i in range(len(text) - N + 1):
        possible_hit = True

        for current_hash in current_hashes:
            idx = current_hash % b
            if bloom[idx] == 0:
                possible_hit = False
                break
        if possible_hit:
            word = text[i : i + N]
            pattern_found = False
            for s in samples:
                comparisons += 1
                if word == s:
                    counter[word] += 1
                    pattern_found = True
                    break

            if not pattern_found:
                colyssions += 1
        
        if i < len(text) - N:
            new_hashes = []
            for old_hash, Q, H in zip(current_hashes, q, h_list):
                new_hash = (d * (old_hash - ord(text[i]) * H) + ord(text[i + N])) % Q
                if new_hash < 0:
                    while new_hash < 0:
                        new_hash += Q
                new_hashes.append(new_hash)
            current_hashes = new_hashes

    t_stop = time.perf_counter()
    t = t_stop - t_start
    return (counter, t, comparisons, colyssions)


samples = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']

counter, tim, comp, colyssions = Bloom_filter(S, samples)
print(f'{counter};{comp};{colyssions};{tim}')