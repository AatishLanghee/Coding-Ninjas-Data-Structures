# Optimized Linked Link


class LinkedListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


# Here we are using tail to traverse the element, and we are traversing only once per element.
# 1 + 1 + 1 + 1 + ... + (n - 1) + n ----> n.
# Therefor time complexity is o(n) = n.
def create_ll(data):
    head = None
    tail = None
    for ip in data:
        if ip == -1:
            return head

        node = LinkedListNode(ip)

        if head is None:
            head = node
            tail = node
        else:
            tail.next_node = node
            tail = node


def print_ll(head):
    while head is not None:
        print(head.data, " -> ", end="")
        head = head.next_node

    print("None")


if __name__ == "__main__":
    ip_data = [int(data) for data in input("Enter the linked list data :").split(" ")]
    ll_head = create_ll(ip_data)
    print_ll(ll_head)
