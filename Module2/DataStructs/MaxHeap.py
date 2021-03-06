'''
MaxHeap class, referenced CodDevX, March 16, 2022

public functions : push, peek pop

pop - Same as extract max; looks for element in 1 position and pulls it off. 
      After extracting max value, swaps lowest position in front, then performs bubble down as needed.

peek - As expected, only shows top element in 1 position

push - Pushes an element to the back of the heap, then performs _floatUp as needed


private functions: swap, _floatUp, _bubbleDown, _str__
'''

class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0] # start elements at index 1 for maxheap

        for item in items:
            self.heap.append(item)
            self._floatUp(len(self.heap) - 1)

#~~~~~~~~~~~~~~~~~~Public Functions~~~~~~~~~~~~~~~~~~~~~~~~#
    def push(self, data):
        self.heap.append(data)
        self._floatUp(len(self.heap)-1)

    def peek(self):
        if self.heap[1]: 
            # if top item present, return it
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self._swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self._bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

#~~~~~~~~~~~~~~~~~~Private Functions~~~~~~~~~~~~~~~~~~~~~~~~#

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _floatUp(self, index):
        parent = index//2
        if index <= 1:
            return 
        elif self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self._floatUp(parent)


    def _bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._bubbleDown(largest)

    def __str__(self):
        return str(self.heap)
