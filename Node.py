import math


class Node:

    def __init__(self, value):
        self.value = value
        self.children = list()
        self.cost = math.inf

    def __str__(self):
        return self.value
