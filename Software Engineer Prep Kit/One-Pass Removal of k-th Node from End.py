""" Title: One-Pass Removal of k-th Node from End
Given the head of a singly linked list and an integer k,
remove the k-th node from the end in one traversal and return the new head. If k is invalid, return the original list."""

#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')



def removeKthNodeFromEnd(head, k):
    k1 = k + 1
    if not head or k1 <= 0:
        return head
    
    first = head
    second = head
    
    for _ in range(k1):
        if first is None:
            return head
        first = first.next
    
    if first is None:
        return head.next
    
    while first.next is not None:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    return head

if __name__ == '__main__':
    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    k = int(input().strip())

    result = removeKthNodeFromEnd(head.head, k)

    print_singly_linked_list(result, '\n')
    print()
