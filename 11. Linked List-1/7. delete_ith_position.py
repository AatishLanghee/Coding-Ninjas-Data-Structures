
class LinkedListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


def create_linked_list(data):
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

    return head


def print_linked_list(head):
    while head is not None:
        print(head.data, " -> ", end="")
        head = head.next_node

    print("None")


def length_linked_list(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next_node

    return count


def delete_node(head, idx):
    length_ll = length_linked_list(head)
    if idx < 0 or idx > length_ll:
        return head

    current = head
    prev = None

    count = 0

    while count < idx:
        count += 1
        prev = current
        current = current.next_node

    if prev is None:
        prev = head
        head = head.next_node
        del prev
    else:
        prev.next_node = current.next_node
        del current

    return head


if __name__ == "__main__":
    ip_data = [int(ip) for ip in input("Enter the data of linked list :").split(" ")]
    linked_list_head = create_linked_list(ip_data)
    print_linked_list(linked_list_head)
    index = int(input("Enter the index to remove :"))
    new_head = delete_node(linked_list_head, index)
    print_linked_list(new_head)
