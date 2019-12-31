import math


class Graph:
    vertices = list()

    def search(self, start, goal):
        for node in self.vertices:
            if node == start:
                node.cost = 0
            else:
                node.cost = math.inf

        visited = list()
        path = list()
        updated = list()

        path = self.dijikstra_search(start, goal, start, visited, path, updated)
        return path

    def dijikstra_search(self, start, goal, current, visited, path, updated):
        if visited is None:
            visited = list()
        visited.append(current)
        path.append('{}{}'.format(current, current.cost))


        if current == goal:
            print("The path to {} using Dijikstra's algorithm is: {}".format(goal, path))
            return path
        else:
            # evaluate cost of unvisited connected nodes & determine the next node to visit
            next = None

            for child in current.children:
                cost = current.cost + child.path_cost

                if cost < child.child.cost:
                    child.child.cost = cost
                    updated.append(child.child)

            for n in updated: #current.children:
                if n not in visited:
                    if next is None:
                        next = n
                    else:
                        if n not in visited:
                            if n.cost < next.cost:
                                next = n

            if next is not None:
                return self.dijikstra_search(start, goal, next, visited, path, updated)
            else:
                print('The path to {} could not be found'.format(goal))
