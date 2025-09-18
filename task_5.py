import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="#CCCCCC"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, step_title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.title(step_title)
    plt.show()


def generate_colors(n, base=(18, 150, 240)):
    colors = []
    for i in range(n):
        factor = 0.3 + 0.7 * (i / max(1, n - 1))
        r = int(base[0] * factor)
        g = int(base[1] * factor)
        b = int(base[2] * factor)
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors


def dfs_iterative(root):
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        if node not in order:
            order.append(node)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return order


def bfs_iterative(root):
    queue = deque([root])
    order = []
    while queue:
        node = queue.popleft()
        if node not in order:
            order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return order


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# --- DFS visualization ---
dfs_order = dfs_iterative(root)
dfs_colors = generate_colors(len(dfs_order))

for i, node in enumerate(dfs_order):
    node.color = dfs_colors[i]
    draw_tree(root, step_title=f"DFS step {i+1}: visit {node.val}")

# --- BFS visualization ---
for node in dfs_order:
    node.color = "#CCCCCC"

bfs_order = bfs_iterative(root)
bfs_colors = generate_colors(len(bfs_order))

for i, node in enumerate(bfs_order):
    node.color = bfs_colors[i]
    draw_tree(root, step_title=f"BFS step {i+1}: visit {node.val}")
