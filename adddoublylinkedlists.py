class ListNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
        if prev is not None:
            self.prev.next = self
        if next is not None:
            self.next.prev = self

class DoublyLinkedList:
    def __init__(self, string = ''):
        self.head = None
        self.tail = None
        self._length = 0
        self.isReversed = False
        for x in string:
            self.addLast(int(x))

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        temp = None
        if self._current == None:
            raise StopIteration
        elif self.isReversed:
            if self._current.value == None:
                temp = 0
            else:
                temp = self._current.value
            self._current = self._current.prev
            return temp
        else:
            temp = self._current.value
            self._current = self._current.next
            return temp

    def addFirst(self, item):
            new = ListNode(item, None, self.head)
            if self._length == 0:
                self.tail = new
            self.head = new
            self._length += 1

    def addLast(self, item):
        if self.isReversed:
            new = ListNode(item, None, self.tail)
            self.tail.prev = new
            self.tail = new
            self._length += 1
        else:
            new = ListNode(item, self.tail, None)
            if self._length == 0:
                self.head = new
            else:
                self.tail.next = new
            self.tail = new
            self._length += 1

    def reverse(self):
        if not self.isReversed:
            start = self.head
            prevTemp = None
            prevTail = self.tail
            while start:
                prevTemp = start.prev
                start.prev = start.next
                start.next = prevTemp
                start = start.prev
            self.tail = self.head
            self.head = prevTail
        else:
            start = self.head
            nextTemp = None
            prevTail = self.tail
            while start:
                nextTemp = start.next
                start.next = start.prev
                start.prev = nextTemp
                start = start.next
            self.tail = self.head
            self.head = prevTail

    def fastReverse(self):
        self.isReversed = not self.isReversed
        tempHead = self.head
        self.head = self.tail
        self.tail = tempHead

    def __str__(self):
        str1 = ''
        current = self.head
        zeroCheck = True
        if self._length == 1:
            return str(self.head.value)
        while current:
            if zeroCheck:
                if current.value == 0:
                    if self.isReversed:
                        current = current.prev
                    else:
                        current = current.next
                    continue
                else:
                    zeroCheck = False
            str1 += str(current.value)
            if self.isReversed:
                current = current.prev
            else:
                current = current.next
        return str1

    def __len__(self):
        return self._length

    def _zeroCheck(self): #seems like it will be unncessary
        start = self.head
        while start:
            if start.value == 0:
                start.value = None
            else:
                self.head = start
                break
            start = start.next

# def sumlinkednumbers(dll1, dll2):
#     currentA = dll1.tail
#     currentB = dll2.tail
#     carry = 0
#     sumList = DoublyLinkedList('')
#     while currentA or currentB:
#         if currentA != None and currentB != None:
#             sum = currentA.value + currentB.value + carry
#             currentA = currentA.prev
#             currentB = currentB.prev
#         elif currentA != None:
#             sum = currentA.value + carry
#             currentA = currentA.prev
#         elif currentB != None:
#             sum = currentB.value + carry
#             currentB = currentB.prev
#         if sum >= 10:
#             sumList.addFirst(sum-10)
#             carry = 1
#         else:
#             sumList.addFirst(sum)
#             carry = 0
#     # sumList._zeroCheck()
#     if carry == 1:
#         sumList.addFirst(1)
#     return sumList

def sumlinkednumbers(dll1, dll2):
    if dll1.isReversed == False and dll2.isReversed == False:
        return sum1(dll1, dll2)
    elif dll1.isReversed == True and dll2.isReversed == False:
        return sum2(dll1, dll2)
    elif dll1.isReversed == False and dll2.isReversed == True:
        return sum4(dll1, dll2)
    else:
        return sum3(dll1, dll2)

def sum1(dll1, dll2):
    currentA = dll1.tail
    currentB = dll2.tail
    carry = 0
    sumList = DoublyLinkedList('')
    while currentA or currentB:
        if currentA != None and currentB != None:
            sum = currentA.value + currentB.value + carry
            currentA = currentA.prev
            currentB = currentB.prev
        elif currentA != None:
            sum = currentA.value + carry
            currentA = currentA.prev
        elif currentB != None:
            sum = currentB.value + carry
            currentB = currentB.prev
        if sum >= 10:
            sumList.addFirst(sum-10)
            carry = 1
        else:
            sumList.addFirst(sum)
            carry = 0
    sumList._zeroCheck()
    return sumList

def sum2(dll1, dll2):
    currentA = dll1.tail
    currentB = dll2.tail
    carry = 0
    sumList = DoublyLinkedList('')
    while currentA or currentB:
        if currentA != None and currentB != None:
            sum = currentA.value + currentB.value + carry
            currentA = currentA.next
            currentB = currentB.prev
        elif currentA != None:
            sum = currentA.value + carry
            currentA = currentA.next
        elif currentB != None:
            sum = currentB.value + carry
            currentB = currentB.prev
        if sum >= 10:
            sumList.addFirst(sum-10)
            carry = 1
        else:
            sumList.addFirst(sum)
            carry = 0
    sumList._zeroCheck()
    return sumList

def sum3(dll1, dll2):
    currentA = dll1.tail
    currentB = dll2.tail
    carry = 0
    sumList = DoublyLinkedList('')
    while currentA or currentB:
        if currentA != None and currentB != None:
            sum = currentA.value + currentB.value + carry
            currentA = currentA.next
            currentB = currentB.next
        elif currentA != None:
            sum = currentA.value + carry
            currentA = currentA.next
        elif currentB != None:
            sum = currentB.value + carry
            currentB = currentB.next
        if sum >= 10:
            sumList.addFirst(sum-10)
            carry = 1
        else:
            sumList.addFirst(sum)
            carry = 0
    sumList._zeroCheck()
    return sumList

def sum4(dll1, dll2):
    currentA = dll1.tail
    currentB = dll2.tail
    carry = 0
    sumList = DoublyLinkedList('')
    while currentA or currentB:
        if currentA != None and currentB != None:
            sum = currentA.value + currentB.value + carry
            currentA = currentA.prev
            currentB = currentB.next
        elif currentA != None:
            sum = currentA.value + carry
            currentA = currentA.prev
        elif currentB != None:
            sum = currentB.value + carry
            currentB = currentB.next
        if sum >= 10:
            sumList.addFirst(sum-10)
            carry = 1
        else:
            sumList.addFirst(sum)
            carry = 0
    sumList._zeroCheck()
    return sumList

# dll = DoublyLinkedList('')
# for i in range(10):
#     dll.addFirst(i)
# dll.fastReverse()
# print(dll)
# for x in range(10, 20):
#     dll.addLast(x)
# print(dll, dll.head.value, dll.tail.value)
# dll.fastReverse()
# print(dll, dll.isReversed)
# for i in range(20, 30):
#     dll.addFirst(i)
# print(dll)
#
# def test(dll):
#     n = 0
#     cur = dll.head
#     while cur:
#         if n == cur.value:
#             cur = cur.prev
#             n += 1
#         else:
#             print('FAIL')
#             break
#     print('SUCCESS')
#
# def test2(dll):
#     n = 29
#     cur = dll.head
#     while cur:
#         if n == cur.value:
#             cur = cur.prev
#             n -= 1
#         else:
#             print('FAIL')
#             break
#     print('SUCCESS')
