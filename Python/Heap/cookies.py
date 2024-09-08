#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
class Heap:
    def __init__(self) -> None:
        self.data = []
        self.count = 0
    
    def left_child_index(self, index):
        return (index * 2) + 1
    
    def right_child_index(self, index):
        return (index * 2) + 2
    
    def parent_index(self, index):
        return (index - 1) // 2
    
    def insert(self, value):
        self.data.append(value)
        self.count += 1
        new_node_index = len(self.data) - 1
        self.trickle_up(new_node_index)
            
    def trickle_up(self, index):
        if index > 0 and (
            self.data[index] < self.data[self.parent_index(index)]):
            
            temp = self.data[index]
            self.data[index] = self.data[self.parent_index(index)]
            self.data[self.parent_index(index)] = temp
            self.trickle_up(self.parent_index(index))
    
    def root_node(self):
        return self.data[0]
        
    def delete(self):
        
        value = self.data[0]
        self.count -= 1
        self.data[0] = self.data[-1]
        self.data.pop()
        trickle_node_index = 0
        
        while self.has_lesser_child(trickle_node_index):
            lesser_child_index = self.calculate_lesser_child_index(trickle_node_index)
            temp = self.data[trickle_node_index]
            self.data[trickle_node_index] = self.data[lesser_child_index]
            self.data[lesser_child_index] = temp
            trickle_node_index = lesser_child_index
        return value
        
    def has_lesser_child(self, index):
        return ((self.left_child_index(index) < self.count and (
                self.data[self.left_child_index(index)] < self.data[index])) or (
                    self.right_child_index(index) < self.count and (
                        self.data[self.right_child_index(index)] < self.data[index]
                    )
                ))

    def calculate_lesser_child_index(self, index):
        
        if self.right_child_index(index) >= self.count:
            return self.left_child_index(index)
        
        if self.data[self.right_child_index(index)] < self.data[self.left_child_index(index)]:
            return self.right_child_index(index)
        else:
            return self.left_child_index(index)
            
hp = Heap()

def cookies(k, A):
    # Write your code here
    for i in A:
        hp.insert(i)
        
    count = 0

    while len(hp.data) > 1 and hp.root_node() <= k:
        a = hp.delete()
        b = hp.delete()
        x = a + (2*b)
        hp.insert(x)
        count += 1
    if hp.root_node() >= k:
        return count
    else:
        return -1
