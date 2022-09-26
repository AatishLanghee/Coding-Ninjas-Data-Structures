# Question: Find a Node in Linked List

# You have been given a singly linked list of integers.
# Write a function that returns the index/position of an integer data denoted by 'N' (if it exists).
# Return -1 otherwise.

# Note :
# Assume that the Indexing for the singly linked list always starts from 0.

# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.

# The second line contains the integer value 'N'.
# It denotes the data to be searched in the given singly linked list.

# Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence,
# would never be a list element.

# Output format :
# For each test case/query, return the index/position of 'N' in the singly linked list. Return -1, otherwise.

#  Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Where 'M' is the size of the singly linked list.

# Sample Input 1 :
# 2
# 3 4 5 2 6 1 9 -1
# 5
# 10 20 30 40 50 60 70 -1
# 6

# Sample Output 1 :
# 2
# -1

# Sample Input 2 :
# 1
# 3 4 5 2 6 1 9 -1
# 6

# Sample Output 2 :
# 4

#  Explanation for Sample Input 2 :
# For the given singly linked list, considering the indices starting from 0,
# progressing in a left to right manner with a jump of 1, then the N = 6 appears at position 4.


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


def search_ll(head, elem):
    count = 0
    while head is not None:
        if head.data == elem:
            return count
        count += 1
        head = head.next_node

    return -1


if __name__ == "__main__":
    ip_data = [int(data) for data in input("Enter the Linked List element :").split(" ")]
    head_ll = create_ll(ip_data)
    print_ll(head_ll)
    element = int(input("Enter the element to search in LL :"))
    print(search_ll(head_ll, element))
