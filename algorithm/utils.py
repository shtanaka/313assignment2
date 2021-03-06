import heapq

INF = 1234567


def look_choice(l, c):
    for i in range(0, len(l)):
        if l[i] == c:
            return i
    return None


def generate(l):
    k = []
    for i in l:
        k.append(i)
    return k


def all_inf(l):
    r = True
    for i in l:
        if i < INF:
            r = False
            return r
    return r


def get_max(l):
    bigger = -1
    r = -1
    for i in range(0, len(l)):
        if bigger < l[i]:
            if l[i] < INF:
                bigger = l[i]
                r = i
    return r


def is_present(heap, value):
    for i in heap:
        if i[0] == value:
            return True
    return False


def get_min(heap):
    smallest = 1234567
    mini = -1
    for i in range(0, len(heap)):
        if heap[i][1] < smallest:
            mini = i
            smallest = heap[i][1]
    r = heap.pop(mini)
    heapq.heapify(heap)
    return r, heap


def set_value(pos, value, heap):
    for i in range(0, len(heap)):
        if heap[i][0] == pos:
            h = (heap[i][0], value)
            heap[i] = h
            heapq.heapify(heap)
            return heap
    return heap
