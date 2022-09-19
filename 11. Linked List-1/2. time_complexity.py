# Time complexity of a Linked List

class LinkedListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


# While creating this linked list, for nth element, we are traversing (n-1) elements.
# 0 + 1 + 2 + 3 + ... + (n - 1) + n ---->  n(n - 1) / 2 -> n2.
# Therefor time complexity is o(n) = n2.
def create_ll(data):
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


def print_ll(head):
    while head is not None:
        print(head.data, " -> ", end="")
        head = head.next_node
    print("None")


if __name__ == "__main__":
    ip_data = [int(data) for data in input("Enter the data :").split(" ")]
    ll_head = create_ll(ip_data)
    print_ll(ll_head)
