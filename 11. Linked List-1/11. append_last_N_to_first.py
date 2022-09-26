# Question: AppendLastNToFirst

# You have been given a singly linked list of integers along with an integer 'N'.
# Write a function to append the last 'N' nodes towards the front of the
# singly linked list and returns the new head to the list.

# Input format :
# The first line contains an Integer 't' which denotes the number of test cases
# or queries to be run. Then the test cases follow.

# The first line of each test case or query contains the elements of the singly linked list separated by a single space.

# The second line contains the integer value 'N'. It denotes the
# number of nodes to be moved from last to the front of the singly linked list.

# Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly
# linked list and hence, would never be a list element.

# Output format :
# For each test case/query, print the resulting singly linked list of integers in a row, separated by a single space.

# Output for every test case will be printed in a separate line.

# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# 0 <= N < M

# Time Limit: 1sec
# Where 'M' is the size of the singly linked list.

# Sample Input 1 :
# 2
# 1 2 3 4 5 -1
# 3
# 10 20 30 40 50 60 -1
# 5

# Sample Output 1 :
# 3 4 5 1 2
# 20 30 40 50 60 10

# Sample Input 2 :
# 1
# 10 6 77 90 61 67 100 -1
# 4

# Sample Output 2 :
# 90 61 67 100 10 6 77

#  Explanation to Sample Input 2 :
# We have been required to move the last 4 nodes to the front of the list.
# Here, "90->61->67->100" is the list which represents the last 4 nodes. When we move this list to the
# front then the remaining part of the initial list which is, "10->6->77" is
# attached after 100. Hence, the new list formed with an updated head pointing to 90.

class LinkedListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


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


def length_linked_list(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next_node
    return count


def append_last_n(head, elem):
    idx = length_linked_list(head) - elem

    count = 0
    current = head
    prev = None
    while count < idx:
        prev = current
        current = current.next_node
        count += 1

    op_head = current

    while current.data != prev.data:
        if current.next_node is None:
            current.next_node = head
        else:
            current = current.next_node
    current.next_node = None
    return op_head


if __name__ == "__main__":
    ip_data = [int(data) for data in input("Enter the Linked List element :").split(" ")]
    head_ll = create_ll(ip_data)
    print_ll(head_ll)
    element = int(input("Enter the number of nodes to append to first :"))
    new_head = append_last_n(head_ll, element)
    print_ll(new_head)
