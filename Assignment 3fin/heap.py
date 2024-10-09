class Heap:
    '''
    Class to implement a heap with a general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two
            arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a given comparison function.
            The comparison function determines the priority in the heap.
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        self.comparison_function = comparison_function
        self.heap = init_array
       
        self.build_heap()
        

    def build_heap(self):
        '''
        buliding heap in n 
        '''
        n = len(self.heap)
        for i in range(n//2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, index):
        '''
        Helper function to maintain heap propertty in log n 
        '''
        right = 2 * index + 2
        left = 2 * index + 1
        smallest = index

        # find smallest of a ,b ,c and swap that element with and maintain heap order 
        if left < len(self.heap) and self.comparison_function(self.heap[left], self.heap[smallest]):
            smallest = left
        if right < len(self.heap) and self.comparison_function(self.heap[right], self.heap[smallest]):
            smallest = right

        
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)


    def insert(self, value):
        
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        '''
        Helper functioon to maintainthe heap 
        A
        '''
        parent = (index - 1) // 2
        # Swap with parent if the current element has higher priority.
        if index > 0 and self.comparison_function(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    def extract(self):
        
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap the root witth the lastelement and pop 
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        
        return root

    def top(self):
       
        if len(self.heap) > 0:
            return self.heap[0]
        return None
