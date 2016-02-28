import heapq


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
