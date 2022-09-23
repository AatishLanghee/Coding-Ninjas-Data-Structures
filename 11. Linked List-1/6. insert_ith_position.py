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


def length_of_linked_list(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next_node

    return count


def insert_ith_position(head, idx, data):
    len_ll = length_of_linked_list(head)
    if idx < 0 or idx > len_ll:
        return head

    count = 0
    current = head
    prev = None
    while count < idx:
        prev = current
        current = current.next_node
        count += 1

    temp_node = LinkedListNode(data)
    if prev is None:
        head = temp_node
    else:
        prev.next_node = temp_node

    temp_node.next_node = current

    return head


def print_linked_list(head):
    while head is not None:
        print(head.data, " -> ", end="")
        head = head.next_node
    print("None")


if __name__ == "__main__":
    ip_data = [int(data) for data in input("Enter the linked list :").split(" ")]
    linked_list_head = create_linked_list(ip_data)
    print_linked_list(linked_list_head)
    index = int(input("Enter the index :"))
    data = int(input("Enter the data to be inserted :"))
    new_head = insert_ith_position(linked_list_head, index, data)
    print_linked_list(new_head)
