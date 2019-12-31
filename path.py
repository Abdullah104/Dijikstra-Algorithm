from Node import Node


class Path:
    def __init__(self, child=Node, path_cost=int):
        self.child = child
        self.path_cost = path_cost
