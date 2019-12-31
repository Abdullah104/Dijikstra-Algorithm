from Node import Node
from path import Path
from Graph import Graph


if __name__ == '__main__':
    # defining nodes
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')

    # defining path
    a.children.append(Path(b, 3))
    a.children.append(Path(c, 4))
    a.children.append(Path(d, 7))

    b.children.append(Path(a, 3))
    b.children.append(Path(c, 1))
    b.children.append(Path(f, 5))

    c.children.append(Path(a, 4))
    c.children.append(Path(b, 1))
    c.children.append(Path(d, 2))
    c.children.append(Path(f, 6))

    d.children.append(Path(a, 7))
    d.children.append(Path(c, 2))
    d.children.append(Path(e, 3))
    d.children.append(Path(g, 6))

    e.children.append(Path(d, 3))
    e.children.append(Path(g, 3))
    e.children.append(Path(h, 4))
    e.children.append(Path(f, 1))

    f.children.append(Path(b, 5))
    f.children.append(Path(c, 6))
    f.children.append(Path(e, 1))
    f.children.append(Path(h, 8))

    g.children.append(Path(d, 6))
    g.children.append(Path(e, 3))
    g.children.append(Path(h, 2))

    h.children.append(Path(g, 2))
    h.children.append(Path(e, 4))
    h.children.append(Path(f, 8))

    # Setting up the graph
    graph = Graph()
    graph.vertices.append(a)
    graph.vertices.append(b)
    graph.vertices.append(c)
    graph.vertices.append(d)
    graph.vertices.append(e)
    graph.vertices.append(f)
    graph.vertices.append(g)
    graph.vertices.append(h)

    graph.search(a, h)
