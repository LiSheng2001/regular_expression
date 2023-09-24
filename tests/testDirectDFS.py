import unittest
from DirectDFS import DirectedDFS, Digraph

class TestDirectedDFS(unittest.TestCase):
    """测试DirectedDFS类"""
    def test_directed_dfs(self):
        # 先构造一个图
        G = Digraph(13)
        G.add_edge(4, 2)
        G.add_edge(2, 3)
        G.add_edge(3, 2)
        G.add_edge(6, 0)
        G.add_edge(0, 1)
        G.add_edge(2, 0)
        G.add_edge(11, 12)
        G.add_edge(12, 9)
        G.add_edge(9, 10)
        G.add_edge(9, 11)
        G.add_edge(8, 9)
        G.add_edge(10, 12)
        G.add_edge(11, 4)
        G.add_edge(4, 3)
        G.add_edge(3, 5)
        G.add_edge(7, 8)
        G.add_edge(8, 7)
        G.add_edge(5, 4)
        G.add_edge(0, 5)
        G.add_edge(6, 4)
        G.add_edge(6, 9)
        G.add_edge(7, 6)

        # 查看边是否全部加载
        self.assertEqual(G.E, 22)

        # 测试可达性
        sources_list = [1, 2, [1, 2, 6]]
        result = [[1], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12]]

        # 开启子测试
        for index in range(len(sources_list)):
            with self.subTest(index=index, input=sources_list[index], result=result[index]):
                # 构建可达性数据结构
                d = DirectedDFS(G, sources_list[index])
                # 获取可达节点
                r = [i for i in range(G.V) if d.marked(i)]
                self.assertEqual(result[index], r)


