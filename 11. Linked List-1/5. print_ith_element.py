# Question: For a given a singly linked list of integers and a position 'i',
# print the node data at the 'i-th' position.

#  Note :
# Assume that the Indexing for the singly linked list always starts from 0.

# If the given position 'i',  is greater than the length of the given singly linked list, then don't print anything.

# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.

# The second line contains the value of 'i'. It denotes the position in the given singly linked list.

#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and
# hence, would never be a list element.

# Output format :
# For each test case, print the node data at the 'i-th' position of the linked list(if exists).

#  Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# i  >= 0

# Time Limit: 1sec

# Sample Input 1 :
# 1
# 3 4 5 2 6 1 9 -1
# 3

# Sample Output 1 :
# 2

# Sample Input 2 :
# 2
# 3 4 5 2 6 1 9 -1
# 0
# 9 8 4 0 7 8 -1
# 3

# Sample Output 2 :
# 3
# 0

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


def print_ith_element(head, ith):
    lth = length_of_linked_list(head)
    if ith > lth:
        return
    count = 0
    while count < ith:
        head = head.next_node
        count += 1

    return head.data


if __name__ == "__main__":
    test_cases = []
    test_cases_number = int(input("Enter the number of test cases :"))
    for _ in range(test_cases_number):
        test_cases.append([int(ip_data) for ip_data in input("Enter the input data :").split(" ")])

    for test_case in test_cases:
        linked_list_head = create_linked_list(test_case)
        ith_element = int(input("Enter the index of ith element :"))
        print(print_ith_element(linked_list_head, ith_element))
