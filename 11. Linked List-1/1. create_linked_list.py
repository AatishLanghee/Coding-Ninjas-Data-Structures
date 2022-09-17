# Create a Linked List and print the linked list.

# In LL, data is not stored in continuous location.
# ( In list/array data structure, data is stored in continuous location. )
# Each element in LL is called as Node.

# Node Structure:
# Node{
#     data,
#     next_node_reference
# }

# Reference to first node is called as Head.
# Reference to last node is called as Tail.

class LinkedListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


def create_linked_list(data):
    head = None
    for ip in data:
        if ip == -1:
            return head

        node = LinkedListNode(ip)

        if head is None:
            head = node
        else:
            current_head = head

            while current_head.next_node is not None:
                current_head = current_head.next_node

            current_head.next_node = node


def print_linked_list(head):
    while head is not None:
        print(head.data, " -> ", end="")
        head = head.next_node
    print("None")


if __name__ == "__main__":
    ip_data = [int(ip_data) for ip_data in input("Enter the data with space separated :").split(" ")]
    linked_list_head = create_linked_list(ip_data)
    print_linked_list(linked_list_head)
