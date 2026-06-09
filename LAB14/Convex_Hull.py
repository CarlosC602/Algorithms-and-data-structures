from functools import cmp_to_key

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def orientation(A, B, C):
    orient = (B.y - A.y) * (C.x - B.x) - (C.y - B.y) * (B.x - A.x)
    if orient > 0:
        return 'right'
    elif orient < 0:
        return 'left'
    else:
        return 'line'


def distance(A, B):
    return (B.x - A.x)**2 + (B.y - A.y)**2
    
def Jarvis(points):
    left_point = points[0]
    if len(points) < 3:
        return None
    for point in points:
        if point.x < left_point.x:
            left_point = point
        elif point.x == left_point.x:
            if point.y < left_point.y:
                left_point = point
    p = left_point
    q = points[points.index(p) + 1]
    hull = []
    while True:
        hull.append(p)
        for r in points:
            orient = orientation(p,q,r)
            if orient == 'left':
                q = r
            elif orient == 'line' and distance(p,r) > distance(p,q):
                q = r
        p = q
        
        if p == left_point:
            break
    return hull


def Graham(points):
    down_point = points[0]
    if len(points) < 3:   
        return None
    for point in points:
        if point.y < down_point.y:
            down_point = point
        elif point.y == down_point.y:
            if point.x < down_point.x:
                down_point = point
    P0 = down_point
    points[points.index(P0)], points[0] = points[0], points[points.index(P0)]

    def compare(A, B):
        orient = orientation(P0, A, B)
        if orient == 'left':
            return -1   
        elif orient == 'right':
            return 1   
        else:
            if distance(P0, A) <= distance(P0, B):
                return -1
            else:
                return 1

    points_sorted = sorted(points[1:], key=cmp_to_key(compare))
    points_sorted = [P0] + points_sorted

    filtered = [points_sorted[0]]
    i = 1
    while i < len(points_sorted):
        j = i
        while j + 1 < len(points_sorted) and orientation(P0, points_sorted[j], points_sorted[j+1]) == 'line':
            j += 1
        filtered.append(points_sorted[j])
        i = j + 1

    if len(filtered) < 3:
        return None

    stack = [filtered[0], filtered[1], filtered[2]]

    for i in range(3, len(filtered)):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], filtered[i]) != 'left':
            stack.pop()
        stack.append(filtered[i])

    return stack
            


if __name__ == "__main__":
    zbior_1 = [point(0, 3), point(0, 0), point(0, 1), point(3, 0), point(3, 3)]
    zbior_2 = [point(0, 3), point(0, 1), point(0, 0), point(3, 0), point(3, 3)]
    
    print("TEST PUNKTÓW WSPÓŁLINIOWYCH")
    print("Zbiór 1:", Jarvis(zbior_1))
    print("Zbiór 2:", Jarvis(zbior_2))

    zbior_3 = [
        point(2, 2), point(4, 3), point(5, 4), point(0, 3), 
        point(0, 2), point(0, 0), point(2, 1), point(2, 0), point(4, 0)
    ]
    
    print("\nWYNIK DLA OSTATNIEGO ZBIORU")
    print("Otoczka wypukła:", Jarvis(zbior_3))

    print("\nWYNIK GRAHAM")
    zbior_graham = [point(0, 3), point(1, 1), point(2, 2), point(4, 4),
                    point(0, 0), point(1, 2), point(3, 1), point(3, 3)]
    print("Otoczka wypukła:", Graham(zbior_graham))