class LinkedList:
    def __init__(self):
        # Create empty LinkedList
        self.head = None

    def invert(self):
        curElement = self.head
        while curElement.next != None:
            curElement.previous, curElement.next = curElement.next, curElement.previous
            curElement = curElement.previous
        curElement.previous, curElement.next = curElement.next, curElement.previous
        self.head = curElement

    def printAll(self):
        curElement = self.head
        while curElement != None:
            print (curElement.value)
            curElement = curElement.next

    def append(self, element):
        if not isinstance(element, LinkedListElement):
            newelement = LinkedListElement(element)
            self.append(newelement)
        else:
            if self.head == None:
                self.head = element
            else:
                curElement = self.head
                while curElement.next != None:
                    curElement = curElement.next
                curElement.insert(element)

    def prepend(self, element):
        if not isinstance(element, LinkedListElement):
            newelement = LinkedListElement(element)
            self.prepend(newelement)
        else:
            if self.head == None:
                self.head = element
            else:
                self.head.previous = element
                element.next = self.head
                self.head =element

    def insert(self, element, pos):
        """
            Insert an element into this list

            element: The element to insert
            pos: The position to insert (0 being the start)
            return: The modified LinkedList
            raise: IndexError if pos is outside of the list
        """
        #check if element is an instance of LinkedListElement
        if not isinstance(element, LinkedListElement):
            #if not create a ListedLinkElement with the elemant as value
            newelement = LinkedListElement(element)
            #call self
            self.insert(newelement, pos)
        else:
            #check if the elemnet already is in a list
            if element.next != None or element.previous != None:
                raise RuntimeError("element seems to be in another linked list")
            #check if new element is inserted at first position
            if pos == 0:
                #check if there is already a first element
                if self.head == None:
                    #if not set element as first element
                    self.head = element
                else:
                    #set previous-pointer of the next element
                    self.head.previous = element
                    #set next-pointer of the new element
                    element.next = self.head
                    #set head-pointer of the List
                    self.head = element
            else:
                #set up a counter for the index
                counter = 0
                #set up variable for the element at that index
                curElement = self.head
                #loop to find the element with the given index
                while counter + 1 != pos:
                    #check for index error
                    if curElement.next == None:
                        raise IndexError("index out of range")
                    #go to next element/index
                    curElement = curElement.next
                    counter += 1
                #insert new element
                curElement.insert(element)

    def remove(self, pos):
        """
            Remove an element from this list

            pos: The position of the element to remove
            returns: The modified LinkedList
            raise: IndexError if pos is outside of the list
        """
        if self.head == None:
            raise IndexError("index out of range")
        else:
            #set up variable for the element
            curElement = self.head
            #set up counter for index
            counter = 0
            #if first element is removed
            if pos == 0:
                #make sure there is a next element
                if curElement.next != None:
                    #remove the previous-pointer on the next element and set the neww head
                    curElement.next.previous = None
                    self.head = curElement.next
                else:
                    #if there is no next element, remove the head
                    self.head = None
                #clear the removed element
                curElement.next = None
            else:
            #loop to find the element at pos
                while counter != pos:
                    #check for index error
                    if curElement.next == None:
                        raise IndexError("index out of range")
                    #go to the next element an increase the counter
                    curElement = curElement.next
                    counter += 1
                #call the element function to remove itself from the list
                curElement.remove(self)

    def find(self, value):
        """
            Find an element in this list

            value: The value of the element to find
            returns: The position of the first occurrence of such an element or -1 if not found
        """
        #check if List is empty
        if self.head == None:
            return -1
        else:
            #set up variable for element
            curElement = self.head
            #set up counter
            counter = 0
            #loop to find element with value
            while curElement.value != value and curElement.next != None:
                curElement = curElement.next
                counter += 1
            #check if the value is found
            if curElement.value == value:
                #returns the index
                return counter
            else:
                #return -1 -> value not in list
                return -1

    def __getitem__(self, pos):
        """
            Return an element at a specific position in the list

            pos: The position of the element to return (0 being the first)
            return: The element 
            raise: IndexError if pos is outside of the list
        """
        #check if List is empty
        if self.head == None:
            raise IndexError("index out of range")
        else:
            #set up variable for element
            curElement = self.head
            #set up counter
            counter = 0
            while counter != pos:
                #check for index error
                if curElement.next == None:
                    raise IndexError("index out of range")
                #go to the next element an increase the counter
                curElement = curElement.next
                counter += 1
            return curElement

class LinkedListElement:
    # Pointer to next element in LinkedList
    next = None
    
    # Pointer to previous element in LinkedList
    previous = None

    def __init__(self, value):
        # Create a new LinkedListElement with value "value"
        self.value = value

    def remove(self, list):
        """
            Remove this item from a LinkedList
        """
        if list.find(self.value) == -1:
            raise RuntimeError("element not removed from list - element was not part of that list")
        if self.previous == None:
            #if the element is the head of the list, set a new one
            list.head = self.next
            self.next.previous = None

        if self.next != None:
            #set the previous-pointer of the next element
            self.next.previous = self.previous
        else:
            self.previous.next = None
        if self.previous != None:
            #set the next-pointer of the last element
            self.previous.next = self.next

        self.previous = None
        self.next = None

    def insert(self, element):
        """
            Insert an element after this element

            element: The element to insert
        """
        if self.next != None:
            #set the previous-pointer of the element after the new element
            self.next.previous = element
            #set the next-pointer as the new element's next-pointer
            element.next = self.next
        #set the previous-pointer of the new elemnet
        element.previous = self
        #set the next-pointer to the new elemnet
        self.next = element


if __name__ == "__main__":
    # Create a new LinkedList
    l = LinkedList()

    # Create a new LinkedListElement
    e1 = LinkedListElement(23)
    assert e1.value == 23, "LinkedListElement e1 does have the wrong value."

    # Insert LinkedListElement to beginning of l
    l.insert(e1, 0)
    assert l.find(23) >= 0, "Cannot find element with value '23' in l"
    assert l[0] == e1, "Element l[0] is not e1"

    # Insert another LinkedListElement at the start
    e2 = LinkedListElement(42)
    l.insert(e2, 0)
    assert l.find(42) >= 0, "Cannot find element with value '42' in l"
    assert l[0] == e2, "Element l[0] is not e2"
    assert l[1] == e1, "Element l[1] is not e1"

    # Remove e1 from LinkedList
    e1.remove(l)
    assert l.find(42) >= 0, "Cannot find element with value '42' in l"
    assert l.find(23) < 0, "Element with value '23' is still in l"
    assert l[0] == e2, "Element l[0] is not e2"
    try:
        assert l[1] == e1
    except IndexError:
        pass
    else:
        raise RuntimeError("Reading out of bounds should raise IndexError!")
    

    m = LinkedList()
    e3 = LinkedListElement(42)
    e4 = LinkedListElement(98)
    e5 = LinkedListElement(12)
    e6 = LinkedListElement(1)
    e7 = LinkedListElement(77)

    m.insert(e3, 0)
    m.insert(e4, 1)
    m.insert(e5, 2)
    try:
        l.insert(e4, 1)
    except RuntimeError:
        print("Element not inserted - already in a list")
    else:
        raise RuntimeError("element shouldn't be inserted!")
    m.remove(1)
    l.insert(e4, 0)
    m.insert(e6, 2)
    e3.insert(e7)
    e3.remove(m)
    try:
        e2.remove(m)
    except RuntimeError:
        print("good Job, element wasn't in the list")
    else:
        raise RuntimeError("you can't remove an element from a list where it isn't part of")
    
    k = LinkedList()
    k.insert(4, 0)
    k.append(8)
    k.insert(55, 2)
    k.prepend(546)
    k.insert(1, 4)

    k.printAll()
    k.invert()
    k.printAll()