# Question: For a given singly linked list of integers, find and return its length.

# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.

#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and
# hence, would never be a list element.

# Output format :
# For each test case, print the length of the linked list.
# Output for every test case will be printed in a separate line.

#  Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5

# Time Limit: 1 sec

# Sample Input 1 :
# 1
# 3 4 5 2 6 1 9 -1

# Sample Output 1 :
# 7

# Sample Input 2 :
# 2
# 10 76 39 -3 2 9 -23 9 -1
# -1

# Sample Output 2 :
# 8
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


def linked_list_length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next_node
    return count


if __name__ == "__main__":
    test_cases = []
    test_case_number = int(input("Enter the number of test cases :"))
    for _ in range(test_case_number):
        test_cases.append([int(data) for data in input("Enter the elements of linked list :").split(" ")])

    for test_case in test_cases:
        ll_head = create_linked_list(test_case)
        print(linked_list_length(ll_head))
