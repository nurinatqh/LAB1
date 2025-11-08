import streamlit as st
from collections import deque
from PIL import Image

image = Image.open("LabReport_BSD2513_#1.jpg")


graph = {
    'A': ['B'],
    'B': ['A', 'C', 'G'],
    'C': ['A', 'B'],
    'D': ['A', 'C'],
    'E': ['B', 'H'],
    'F': [],
    'G': ['F', 'H'],
    'H': ['F']
}

for node in graph:
    graph[node] = sorted(graph[node])

# BFS FUNCTION

def bfs(start):
    visited = set([start])
    queue = deque([start])
    order = []
    level = {start: 0}

    while queue:
        u = queue.popleft()
        order.append(u)

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
                level[v] = level[u] + 1

    return order, level

# DFS FUNCTION

def dfs(start):
    visited = set()
    order = []

    def _dfs(u):
        visited.add(u)
        order.append(u)
        for v in graph[u]:
            if v not in visited:
                _dfs(v)

    _dfs(start)
    return order

# STREAMLIT UI

st.title("BFS and DFS Traversal App")
st.write("This app visualizes BFS and DFS traversal based on the given directed graph.")

# Display Graph Image
st.subheader("Graph Used for Traversal")
st.image(image, caption="Directed Graph", use_column_width=True)

# Select Start Node
start_node = st.selectbox("Select Start Node:", list(graph.keys()), index=0)

# Display Graph Adjacency
st.subheader("Graph Adjacency List")
for node in sorted(graph.keys()):
    st.write(f"{node} → {graph[node]}")

# BFS Output
st.subheader("BFS Result")
bfs_order, bfs_level = bfs(start_node)
st.write("**Order:**", bfs_order)
st.write("**Levels:**", bfs_level)

# DFS Output
st.subheader("DFS Result")
dfs_order = dfs(start_node)
st.write("**Order:**", dfs_order)
