import time 
from node import bfs, dfs

bfs_start = time.time()
b = bfs()
bfs_end = time.time()
bfs_total_time = bfs_end - bfs_start

dfs_start = time.time()
d = dfs()
dfs_end = time.time()
dfs_total_time = dfs_end - dfs_start

print("bfs= ", b)
print("dfs= ", d)
print(f"bfs:{bfs_total_time}\ndfs:{dfs_total_time}")
