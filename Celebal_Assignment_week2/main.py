class Node:
    #Class to represent a node in a singly linked list
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    #The Class to manage the singly linked list
    def __init__(self):
        self.head = None

    def add_node(self, data):
        #Adding a node to the end of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        #Used to Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        #It will Print the contents of the list
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        #It will Delete the nth node (1-based index)
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index must be 1 or greater.")

        if n == 1:
            print(f"Deleting node at position {n}: {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range.")

        print(f"Deleting node at position {n}: {current.data}")
        prev.next = current.next


if __name__ == "__main__":
    ll = LinkedList()


    for value in [10, 20, 30, 40, 50]:
        ll.add_node(value)

    print("Original list:")
    ll.print_list()

    try:
        ll.delete_nth_node(3)
        print("\nList after deleting 3rd node:")
        ll.print_list()

        ll.delete_nth_node(1)
        print("\nList after deleting 1st node:")
        ll.print_list()

     # Will raise an exception
        ll.delete_nth_node(10)  
    except Exception as e:
        print("\nError:", e)
