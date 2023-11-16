class Heap():
    '''
    position of parent:      floor(i/2) (provided i >= 2)
    position of left child:  2i (provided 2i <= n)
    position of right child: 2i + 1 (provided 2i + 1 <= n)
    '''
    def __init__(self):
        self.heap = []

    def insert(self, item):
        # Insert at the end of the heap
        self.heap.append(item)
        
        # No need to do anything if this is the first element added to heap
        if len(self.heap) == 1:
            return
        
        # Bubble up, comparing against parent and swapping if parent < item
        i = len(self.heap) - 1
        while i > 1:
            if self.heap[(i // 2)] > self.heap[i]:
                self.heap[(i // 2)], self.heap[i] = self.heap[i], self.heap[(i // 2)]
                i = i // 2
            else:
                return
            
    def extract_min(self):
        if len(self.heap) == 1:
            return(self.heap.pop())
        
        # Store the min value
        tmp = self.heap[0]

        # Move last element to first position and bubble down, restoring balance
        self.heap[0] = self.heap.pop()
        i = 1
        while (i * 2) <= len(self.heap):
            if ((i * 2) + 1) > len(self.heap):
                if(self.heap[i - 1] > self.heap[(i * 2) - 1]):
                    self.heap[i - 1], self.heap[(i * 2) - 1] = self.heap[(i * 2) - 1], self.heap[i - 1]
                    i = i * 2
                else: 
                    break

            else:
                if self.heap[(i * 2) - 1] < self.heap[i * 2]:
                    if (self.heap[i - 1] > self.heap[(i * 2) - 1]):
                        self.heap[i - 1], self.heap[(i * 2) - 1] = self.heap[(i * 2) - 1], self.heap[i - 1]
                        i = i * 2
                    else: 
                        break
                else:
                    if (self.heap[i - 1] > self.heap[i * 2]):
                        self.heap[i - 1], self.heap[i * 2] = self.heap[i * 2], self.heap[i - 1]
                        i = (i * 2) + 1
                    else: 
                        break
        
        return tmp


if __name__ == "__main__":
    h = Heap()
    h.insert(1)
    h.insert(4)
    h.insert(5)
    h.insert(6)
    h.insert(2)
    h.insert(7)
    h.insert(11)
    h.insert(13)
    h.insert(10)
    h.insert(12)
    h.insert(9)
    print(h.heap)
    print(h.extract_min())
    print(h.heap)