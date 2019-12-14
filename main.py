import time
from node import bfs, dfs, find_path
from generate_tree import BFS_tree, DFS_tree

i_state = [3,3,0]

BFS_tree()
DFS_tree()

bfs_start = time.clock()
bfs_sol = bfs(i_state)
bfs_end = time.clock()
bfs_total_time = bfs_end - bfs_start
bfs_path = find_path(bfs_sol)

# print(bfs_total_time)

dfs_start = time.clock()
dfs_sol = dfs(i_state)
dfs_end = time.clock()
dfs_total_time = dfs_end - dfs_start
dfs_path = find_path(dfs_sol)
# print(dfs_total_time)

print(f"\nTotal time taken by Breadth First Search:{bfs_total_time}\nTotal Time taken by Depth First Search:{dfs_total_time}")
print(f"\nBFS traversal path = {bfs_path}\nDFS traversal path = {dfs_path}")