class HuffPQ:
    """
    The Huffman Priority Queue is implemented with a minimum heap 
    that uses a Python list to store the heap elements in a 
    complete binary tree. Each heap element is a HuffTree.
    To get help in coding these methods, please review the MinHeap
    class in Lesson 7 slides.  The methods are a little different, 
    since the slides assume that the heap elements are integers, 
    where as, in this case, they are Comparable HuffTrees. Also,
    the slides use a heap_size instance variable, where as you must 
    use the length of the list instead. You may also look at the 
    heap used in Project 1, which stored Comparable Person objects.  
    """ 
    def __init__(self):
        """
        Create an empty priority queue from a Python list.
        Do not add any more instance variables.
        """
        
        self._pq = [] 
        
    def __len__(self):
        """
        Return the number of elements (HuffTrees) in the queue
        """
        
        return len(self._pq)
        
    def heapify(self, index):
        """
        Restore the Min Heap order starting with the HuffTree 
        at the given index in the pq list.  This involves swapping
        the given HuffTree with whichever of its HuffTree children 
        has a smaller value using the compare method, if either of 
        them are smaller.  Then recursively calling heapify passing 
        in the index of the smallest HuffTree element.  
        """
        
        left_index = self.get_left_child(index)
        right_index = self.get_right_child(index)
        smallest = index

        if (left_index < len(self)) and \
             self._pq[left_index].compare(self._pq[index]) < 0:
            smallest = left_index

        if (right_index < len(self)) and \
             self._pq[right_index].compare(self._pq[smallest]) < 0:
            smallest = right_index

        if smallest != index:
            temp = self._pq[index]
            self._pq[index] = self._pq[smallest]
            self._pq[smallest] = temp

            self.heapify(smallest)
                
    def get_parent(self, index):
        """
        Return the parent index of the tree at the given index
        """
        
        return (index-1) // 2
  
    
    def get_left_child(self, index):
        """
        Return the left child index of the tree at the given index
        """
        
        return 2*index + 1
        
    
    def get_right_child(self, index):
        """
        Return the right child index of the tree at the given index
        """
        
        return 2*index + 2
         
    
    def dequeue(self):
        """
        Remove the heap root HuffTree (which has the minimum value).
        This is the HuffTree at the top of the heap at element 0.
        This dequeuing of the root involves replacing the root element
        with the last element in the heap at index len(heap) -1
        Then calling heapify with index 0 to restore the heap order.
        Please review the extract_min method from the slides.

        """
        
        if len(self) == 0:
            return None

        if len(self) == 1:
            root = self._pq[0]
            self._pq = []
            return root

        root = self._pq[0]
        self._pq[0] = self._pq.pop()

        self.heapify(0)
        return root
    

    def enqueue(self, tree): 
        """
        Inserts a new HuffTree element into the heap at the end of 
        the heap pq list. Set the index variable equal to the index 
        of that element. Then restore the heap order.  This is done 
        in a loop by swapping the HuffTree element at that index with 
        its parent, if the parent HuffTree element is larger, stopping 
        when the smallest element is at the top of the heap or when 
        the heap order is restored, when the parent HuffTree is 
        smaller than its childern.  Please review the insert_elem 
        method from the slides for help.  
        """ 
        
        self._pq.append(tree)
        index = len(self) - 1

        while (index != 0) and \
              (self._pq[self.get_parent(index)].compare(self._pq[index]) > 0):

            temp = self._pq[index]
            self._pq[index] = self._pq[self.get_parent(index)]
            self._pq[self.get_parent(index)] = temp

            index = self.get_parent(index)
            
    
    def peek(self):
        """
        Returns the tree with minimum value (root HuffTree),
        without removing it
        """ 
        
        return self._pq[0]
