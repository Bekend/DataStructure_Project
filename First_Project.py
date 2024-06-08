class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        # Initialize a dummy head node
        self.head = Node()
        self.head.next = self.head  # Point the dummy head to itself

    def is_empty(self):
        # Check if the list is empty
        return self.head.next == self.head

    def append(self, data):
        # Append a new node with the given data to the list
        new_node = Node(data)
        if self.is_empty():
            self.head.next = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        # Display the elements of the list
        if self.is_empty():
            print("The list is empty.")
            return
        current = self.head.next
        while current != self.head:
            print(current.data, end=" -> ")
            current = current.next
        print("(head)")

    def is_prime(self, n):
        # Check if a given number is prime
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def remove_primes(self):
        # Remove all prime numbers from the list
        if self.is_empty():
            return
        prev = self.head
        current = self.head.next
        while current != self.head:
            if self.is_prime(current.data):
                prev.next = current.next
            else:
                prev = current
            current = current.next
        # Ensuring the list remains circular if all elements are primes
        if self.head.next == self.head:
            self.head.next = self.head

    @staticmethod
    def merge_sorted(list1, list2):
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort(left_half)
                merge_sort(right_half)

                i = j = k = 0

                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

            return arr

        result = CircularLinkedList()
        nodes = []

        current1 = list1.head.next
        while current1 != list1.head:
            nodes.append(current1.data)
            current1 = current1.next

        current2 = list2.head.next
        while current2 != list2.head:
            nodes.append(current2.data)
            current2 = current2.next

        nodes = merge_sort(nodes)

        for data in nodes:
            result.append(data)

        return result

class Stack:
    def __init__(self):
        # Initialize a stack using a circular linked list
        self.list = CircularLinkedList()

    def push(self, data):
        # Push an element onto the stack
        new_node = Node(data)
        if self.list.is_empty():
            self.list.head.next = new_node
            new_node.next = self.list.head
        else:
            new_node.next = self.list.head.next
            self.list.head.next = new_node

    def pop(self):
        # Pop an element from the stack
        if self.list.is_empty():
            raise IndexError("Pop from empty stack")
        pop_node = self.list.head.next
        self.list.head.next = pop_node.next
        return pop_node.data

    def display(self):
        # Display the elements of the stack
        self.list.display()

class Queue:
    def __init__(self):
        # Initialize a queue using a circular linked list
        self.list = CircularLinkedList()
        self.tail = self.list.head

    def add(self, data):
        # Add an element to the queue
        new_node = Node(data)
        if self.list.is_empty():
            self.list.head.next = new_node
            new_node.next = self.list.head
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.list.head
            self.tail = new_node

    def delete(self):
        # Delete an element from the queue
        if self.list.is_empty():
            raise IndexError("Delete from empty queue")
        delete_node = self.list.head.next
        self.list.head.next = delete_node.next
        if self.tail == delete_node:
            self.tail = self.list.head
        return delete_node.data

    def display(self):
        # Display the elements of the queue
        self.list.display()

# Example usage:
# cll = CircularLinkedList()
# cll.append(2)
# cll.append(3)
# cll.append(4)
# cll.append(5)
# cll.append(6)
# print("Original list:")
# cll.display()
# cll.remove_primes()
# print("List after removing primes:")
# cll.display()
#
# list1 = CircularLinkedList()
# list1.append(1)
# list1.append(3)
# list1.append(5)
# list2 = CircularLinkedList()
# list2.append(2)
# list2.append(4)
# list2.append(6)
# merged_list = CircularLinkedList.merge_sorted(list1, list2)
# print("Merged sorted list:")
# merged_list.display()
#
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print("Stack:")
# stack.display()
# print("Popped from stack:", stack.pop())
# stack.display()
#
# queue = Queue()
# queue.add(10)
# queue.add(20)
# queue.add(30)
# print("Queue:")
# queue.display()
# print("Deleted from queue:", queue.delete())
# queue.display()
