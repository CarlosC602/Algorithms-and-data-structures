def build_suffix_tree(text):
    text = text + "$"
    root = {}
    
    for i in range(len(text)):
        current = root
        for j in range(i, len(text)):
            char = text[j]
            if char not in current:
                current[char] = {}
            current = current[char]
            
    compress_tree(root)
    
    return root, text


def compress_tree(node):
    for key in list(node.keys()):
        child = node[key]
        compress_tree(child)
        
        if len(child) == 1:
            child_key = list(child.keys())[0]
            new_key = key + child_key
            node[new_key] = child[child_key]
            del node[key]


def print_tree(node, prefix=""):
    for key, child in node.items():
        print(prefix + "├── " + key)
        print_tree(child, prefix + "│   ")


def search_in_tree(node, pattern):
    if not pattern:
        return True
        
    for edge in node.keys():
        if edge.startswith(pattern):
            return True
        elif pattern.startswith(edge):
            return search_in_tree(node[edge], pattern[len(edge):])
            
    return False


def build_suffix_array(text):
    text = text + "$"
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort()
    sa = [s[1] for s in suffixes]
    return text, sa


def binary_search_sa(text, sa, pattern):
    l, r = 0, len(sa) - 1
    
    while l <= r:
        mid = (l + r) // 2
        suffix = text[sa[mid]:]
        
        if suffix.startswith(pattern):
            return True
            
        if pattern < suffix:
            r = mid - 1
        else:
            l = mid + 1
            
    return False


def build_lcp_array(text, sa):
    lcp = [0] * len(sa)
    for i in range(1, len(sa)):
        s1 = text[sa[i-1]:]
        s2 = text[sa[i]:]
        match_len = 0
        while match_len < len(s1) and match_len < len(s2) and s1[match_len] == s2[match_len]:
            match_len += 1
        lcp[i] = match_len
    return lcp


def longest_prefix(word1, word2):
    combined_text = word1 + "$" + word2 + "#"
    
    suffixes = [(combined_text[i:], i) for i in range(len(combined_text))]
    suffixes.sort()
    sa = [s[1] for s in suffixes]
    lcp = build_lcp_array(combined_text, sa)
    
    max_len = 0
    best_str = ""
    len1 = len(word1)
    
    for i in range(1, len(sa)):
        if lcp[i] > max_len:
            idx1 = sa[i-1]
            idx2 = sa[i]
            
            is_from_different_words = (idx1 < len1 and idx2 > len1) or (idx2 < len1 and idx1 > len1)
            
            if is_from_different_words:
                max_len = lcp[i]
                best_str = combined_text[idx1 : idx1+max_len]
                
    return best_str

if __name__ == '__main__':
    slowo = "banana"
    wzorce = ["na", "ana", "nana", "ananas"]

    print("1)Drzewo sufiksowe:")
    drzewo_root, text_z_dolarem = build_suffix_tree(slowo)
    
    print(f"Drzewo sufiksowe dla '{text_z_dolarem}':")
    print_tree(drzewo_root)
    
    print("\nWyszukiwanie w drzewie:")
    for w in wzorce:
        wynik = search_in_tree(drzewo_root, w)
        print(f"Czy '{w}' występuje? -> {wynik}")
        

    print("2)Tablica sufiksowa:")

    text_z_dolarem_sa, sa = build_suffix_array(slowo)
    print(f"Tablica sufiksowa dla '{slowo}': {sa}")
    
    print("\nWyszukiwanie binarne w tablicy:")
    for w in wzorce:
        wynik = binary_search_sa(text_z_dolarem_sa, sa, w)
        print(f"Czy '{w}' występuje? -> {wynik}")


    print("3)Tablica LCP:")
    w1 = "banana"
    w2 = "ananas"
    lcs_result = longest_prefix(w1, w2)
    print(f"Najdłuższy wspólny podciąg dla '{w1}' oraz '{w2}' to: '{lcs_result}'")