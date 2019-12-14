import time
from node import bfs, dfs
from generate_tree import BFS_tree, DFS_tree

i_state = [3,3,0]

bfs_start = time.clock()
bfs(i_state)
bfs_end = time.clock()
bfs_total_time = bfs_end - bfs_start
# print(bfs_total_time)

dfs_start = time.clock()
dfs(i_state)
dfs_end = time.clock()
dfs_total_time = dfs_end - dfs_start
# print(dfs_total_time)

print(f"Total time taken by Breadth First Search:{bfs_total_time}\nTotal Time taken by Depth First Search:{dfs_total_time}")
BFS_tree()
DFS_tree()