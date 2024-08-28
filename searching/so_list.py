class LinkedList:
    def __init__(self):
        self.head = None

    def __getitem__(self, pos):
        if not self.head:
            raise IndexError("index out of range")
        else:
            curElement = self.head
            counter = 0
            while counter != pos:
                if not curElement.next:
                    raise IndexError("index out of range")
                curElement = curElement.next
                counter += 1
            return curElement.value
        
    def __str__(self) -> str:
        curElement = self.head
        out = "LinkedList: "
        if curElement:
            out = out + str(curElement.value)
            while curElement.next != None:
                out = out + ", "
                curElement = curElement.next
                out = out + str(curElement.value)
        return out

    def insert(self, value, pos = None):
        newElement = LinkedListElement(value)
        curElement = self.head
        if not curElement:
            self.head = newElement
        else:
            if pos == 0:
                self.head.previous = newElement
                newElement.next = self.head
                self.head = newElement
            else:
                if pos != None:
                    counter = 0
                    while counter + 1 != pos:
                        if not curElement.next:
                            raise IndexError("index out of range")
                        curElement = curElement.next
                        counter += 1
                    curElement.insert(newElement)
                else:
                    while curElement.next:
                        curElement = curElement.next
                    curElement.insert(newElement)

    def remove(self, pos):
        if not self.head:
            raise IndexError("index out of range")
        else:
            curElement = self.head
            counter = 0
            if pos == 0:
                if curElement.next:
                    curElement.next.previous = None
                    self.head = curElement.next
                else:
                    self.head = None
                curElement.next = None
            else:
                while counter != pos:
                    if not curElement.next:
                        raise IndexError("index out of range")
                    curElement = curElement.next
                    counter += 1
                curElement.remove(self)

    def t_search(self, value):
        curElement = self.head
        while curElement:
            if curElement.value == value:
                x = curElement.transpose()
                if x != None:
                    self.head = x
                return curElement.value
            else:
                curElement = curElement.next
        return -1
    
    def mtf_search(self, value):
        curElement = self.head
        while curElement:
            if curElement.value == value:
                curElement.remove()
                self.insert(curElement.value, 0)
                return curElement.value
            else:
                curElement = curElement.next
        return -1


class LinkedListElement:
    next = None
    previous = None
    counter = 0

    def __init__(self, value):
        self.value = value

    def insert(self, element):
        if self.next != None:
            self.next.previous = element
            element.next = self.next
        element.previous = self
        self.next = element

    def remove(self):
        if not self.next:
            self.previous.next = None
            self.previous = None
        else:
            self.previous.next = self.next
            self.next.previous = self.previous
            self.previous = None
            self.next = None

    def transpose(self):
        if self.previous != None and self.previous.previous != None:
            self.previous.previous.next = self
            self.next.previous = self.previous
            self.previous.next = self.next
            self.next = self.previous
            self.previous = self.next.previous
            self.next.previous = self
        elif self.previous != None and self.previous.previous == None:
            self.next.previous = self.previous
            self.previous.next = self.next
            self.previous.previous = self
            self.next = self.previous
            self.previous = None
            return self
        return None



if __name__ == "__main__":
    arr = [4,5,10,11,13,20,19,22,7]
    tests = [13,20,13,19,5,4]

    l = LinkedList()
    for i in arr:
        l.insert(i)
    for i in tests:
        l.t_search(i)

    m = LinkedList()
    for i in arr:
        m.insert(i)
    for i in tests:
        m.mtf_search(i)


print(l)
print(m)