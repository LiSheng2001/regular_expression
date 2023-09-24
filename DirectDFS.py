"""处理有向图多点可达性问题
这是非确定有限状态机判断是否能到达完成状态重要的一环
"""
from typing import Union, List

class Digraph:
    """用邻接表储存有向图的数据结构"""
    def __init__(self, V: int):
        self.V = V
        self.E = 0
        # 邻接表
        self.adj = [set() for i in range(V)]
        
    def add_edge(self, v: int, w: int):
        """添加边"""
        self.adj[v].add(w)
        self.E += 1

    def get_adj(self, v: int):
        """获取边的邻接表"""
        return self.adj[v]


class DirectedDFS:
    """判断有向图可达性的API"""
    def __init__(self, G: Digraph, sources: Union[int, List[int]]):
        """sources可以是单个数字，代表单点。也可以是一个列表，代表多点情况下的可达性"""
        self.marked_list = [False for i in range(G.V)]
        # 把单点情况处理为多点
        if isinstance(sources, int):
            sources = [sources]

        # 多点可达性DFS
        for s in sources:
            if not self.marked_list[s]:
                self.dfs(G, s)


    def marked(self, v: int):
        """返回该点是否可达"""
        return self.marked_list[v]

    def dfs(self, G: Digraph, v: int):
        """用深度优先搜索判断可达性"""
        self.marked_list[v] = True
        for w in G.adj[v]:
            if not self.marked_list[w]:
                self.dfs(G, w)
