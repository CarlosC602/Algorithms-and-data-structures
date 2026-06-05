import time
import numpy as np

def recursive_cost(P, T, i, j):
    insert_cost = 0
    switch_cost = 0
    delete_cost = 0

    if i == 0:
        return j

    if j == 0:
        return i

    delete_cost = 1 + recursive_cost(P, T, i-1, j)
    insert_cost = 1 + recursive_cost(P, T, i, j-1)

    if P[i-1] == T[j-1]:
        switch_cost = 0
    else:
        switch_cost = 1

    switch_cost += recursive_cost(P, T, i-1, j-1)

    return min(insert_cost, switch_cost, delete_cost)

def PD_cost(P, T):
    insert_cost = 0
    switch_cost = 0
    diff_cost = 0
    delete_cost = 0

    D = np.zeros((len(P), len(T)))

    M = np.zeros((len(P), len(T)), dtype=str)

    for i in range(len(P)):
        D[i,0] = i
        M[i,0] = 'D'

    for j in range(len(T)):
        D[0, j] = j
        M[0, j] = 'I'

    M[0,0] = 'X'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            delete_cost = D[i-1][j] + 1
            insert_cost = D[i][j-1] + 1

            if P[i] == T[j]:
                diff_cost = 0
            else:
                diff_cost = 1

            switch_cost = diff_cost + D[i-1][j-1]
            
            min_cost = min(delete_cost, insert_cost, switch_cost)

            D[i][j] = min_cost

            if min_cost == switch_cost:
                if P[i] == T[j]:
                    M[i][j] = 'M'
                else:
                    M[i][j] = 'R'
            elif min_cost == delete_cost:
                M[i][j] = 'D'
            elif min_cost == insert_cost:
                M[i][j] = 'I'
    
    cost_res = D[len(P)-1, len(T)-1]
    return (cost_res, M)

def PD_cost_v2(P, T):
    insert_cost = 0
    switch_cost = 0
    diff_cost = 0
    delete_cost = 0

    D = np.zeros((len(P), len(T)))

    M = np.zeros((len(P), len(T)), dtype=str)

    for i in range(len(P)):
        D[i,0] = i
        M[i,0] = 'D'

    for j in range(len(T)):
        D[0, j] = 0
        M[0, j] = 'X'

    M[0,0] = 'X'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            delete_cost = D[i-1][j] + 1
            insert_cost = D[i][j-1] + 1

            if P[i] == T[j]:
                diff_cost = 0
            else:
                diff_cost = 1

            switch_cost = diff_cost + D[i-1][j-1]
            
            min_cost = min(delete_cost, insert_cost, switch_cost)

            D[i][j] = min_cost

            if min_cost == switch_cost:
                if P[i] == T[j]:
                    M[i][j] = 'M'
                else:
                    M[i][j] = 'R'
            elif min_cost == delete_cost:
                M[i][j] = 'D'
            elif min_cost == insert_cost:
                M[i][j] = 'I'
    
    last_row = D[len(P)-1, :]
    cost_res = np.min(last_row)
    idx = np.argmin(last_row)
    return (cost_res, M, idx)


def find_path(P, T, M):
    i = len(P) - 1
    j = len(T) - 1
    path = []
    while M[i][j] != 'X':
        path.append(M[i][j])
        if M[i][j] == 'M' or M[i][j] == 'R':
            i -= 1
            j -= 1
        elif M[i][j] == 'D':
            i -= 1
        elif M[i][j] == 'I':
            j -= 1 
    path.reverse()
    path = "".join(path)
    return path

def find_path_v2(P, T, M, idx):
    i = len(P) - 1
    j = idx 
    while M[i][j] != 'X':
        if M[i][j] == 'M' or M[i][j] == 'R':
            i -= 1
            j -= 1
        elif M[i][j] == 'D':
            i -= 1
        elif M[i][j] == 'I':
            j -= 1 
    return j

def PD_lcs(P, T):
    D = np.zeros((len(P), len(T)))
    M = np.zeros((len(P), len(T)), dtype=str)

    for i in range(len(P)):
        D[i,0] = i
        M[i,0] = 'D'

    for j in range(len(T)):
        D[0, j] = j
        M[0, j] = 'I'

    M[0,0] = 'X'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            delete_cost = D[i-1][j] + 1
            insert_cost = D[i][j-1] + 1

            if P[i] == T[j]:
                diff_cost = 0
            else:
                diff_cost = 999999  

            switch_cost = diff_cost + D[i-1][j-1]
            
            min_cost = min(delete_cost, insert_cost, switch_cost)
            D[i][j] = min_cost

            if min_cost == switch_cost:
                M[i][j] = 'M'  
            elif min_cost == delete_cost:
                M[i][j] = 'D'
            elif min_cost == insert_cost:
                M[i][j] = 'I'
    
    return D[len(P)-1, len(T)-1], M

def get_lcs(P, T, M):
    i = len(P) - 1
    j = len(T) - 1
    lcs_result = []
    
    while M[i][j] != 'X':
        if M[i][j] == 'M':
            lcs_result.append(P[i])
            i -= 1
            j -= 1
        elif M[i][j] == 'D':
            i -= 1
        elif M[i][j] == 'I':
            j -= 1
            
    lcs_result.reverse()
    return "".join(lcs_result)


if __name__ == '__main__':
    P = ' kot'
    T = ' koń'
    t_start = time.perf_counter()
    res = recursive_cost(P, T, len(P), len(T))
    t_stop = time.perf_counter()
    t = t_stop - t_start
    print(f"Wyraz{P} można zmienić w wyraz{T} kosztem {res} w czasie {t}")
    
    P = ' kot'
    T = ' pies'
    t_start = time.perf_counter()
    res = recursive_cost(P, T, len(P), len(T))
    t_stop = time.perf_counter()
    t = t_stop - t_start
    print(f"Wyraz{P} można zmienić w wyraz{T} kosztem {res} w czasie{t}")

    P_bus = ' biały autobus'
    T_bus = ' czarny autokar'
    cost_bus, _ = PD_cost(P_bus, T_bus)
    print(f"Koszt zamiany bus: {int(cost_bus)}")

    P = ' thou shalt not'
    T = ' you should not'
    _, M = PD_cost(P, T)
    path = find_path(P, T, M)
    print(f"Wyraz{P} można zmienić w wyraz{T} zamianami {path}")

    T_sub = ' mokeyssbanana'
    
    P_sub1 = ' ban'
    cost1, M1, idx1 = PD_cost_v2(P_sub1, T_sub)
    start1 = find_path_v2(P_sub1, T_sub, M1, idx1)
    print(f"{start1}, {int(cost1)}")

    P_sub2 = ' bin'
    cost2, M2, idx2 = PD_cost_v2(P_sub2, T_sub)
    start2 = find_path_v2(P_sub2, T_sub, M2, idx2)
    print(f"{start2}, {int(cost2)}")


    P_lcs = ' democrat'
    T_lcs = ' republican'
    _, M_lcs = PD_lcs(P_lcs, T_lcs)
    shared_sequence = get_lcs(P_lcs, T_lcs, M_lcs)
    print(shared_sequence)

    T_lis = ' 243517698'
    P_lis = "".join(sorted(T_lis))
    _, M_lis = PD_lcs(P_lis, T_lis)
    monotonic_sequence = get_lcs(P_lis, T_lis, M_lis)
    print(f"Najdłuższa podsekwencja monotoniczna to: {monotonic_sequence}")