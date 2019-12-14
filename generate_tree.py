import networkx as nx
import matplotlib.pyplot as plt

from node import G_bfs_optimized, G_dfs_optimized

i_state = [3,3,0]

#determining nodes position for hierarchial structure
def nodes_pos(G, root, width=1, vert_gap = 0.1, vert_pos = 0, xcenter = 0, pos = None, parent = None):
    if pos is None:
        pos = {root:(xcenter,vert_pos)}
    else:
        pos[root] = (xcenter, vert_pos)
    
    children = list(G.neighbors(root))
    
    if parent is not None:
        children.remove(parent)  
    
    if len(children)!= 0:
        if len(children) == 4:
            width = 0.1
        if len(children) == 3:
            width = 1
        else:
            width = len(children)/2
        dx = width/len(children) 
        nextx = xcenter - width/2 - dx/2
        for child in children:
            nextx += dx
            pos = nodes_pos(G,child, width = dx, vert_gap = vert_gap, 
                                vert_pos = vert_pos-vert_gap, xcenter=nextx,
                                pos=pos, parent = root)
    return pos

#defining the color dictionary
color_dict = {'Killed Node':'r','Traversed Node':'g', 'Goal Node':'y'}

#coloring bfs_tree nodes
bfs_pos = nodes_pos(G_bfs_optimized,str(i_state)) 
bfs_color_list = [color_dict[i[1]] for i in G_bfs_optimized.nodes.data('color')] 
plt.title("Breadth First Search Traversal")
nx.draw(G_bfs_optimized, pos=bfs_pos,node_color=bfs_color_list, with_labels=True, font_size= 9, font_weight='bold')
plt.savefig('bfs_tree.png')
plt.show()

#coloring dfs_tree nodes
dfs_pos = nodes_pos(G_dfs_optimized, str(i_state))
dfs_color_list = [color_dict[i[1]] for i in G_dfs_optimized.nodes.data('color')]
plt.title("Depth First Search Traversal")
nx.draw(G_dfs_optimized, pos=dfs_pos, node_color = dfs_color_list,with_labels=True, font_size = 9, font_weight='bold')
plt.savefig('dfs_tree.png')
plt.show()