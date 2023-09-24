"""用Python实现一个正则表达式
"""
from DirectDFS import Digraph, DirectedDFS
from typing import List

def recognizes(txt: str, G: Digraph, re: List[str]):
    """通过NFA判断文本txt来是否能识别"""
    pc = set()
    dfs = DirectedDFS(G, 0)
    M = len(re)

    for v in range(G.V):
        if dfs.marked(v):
            pc.add(v)
    
    for i in range(len(txt)):
        # 计算txt[i+1]能够到达的所有NFA状态
        match_nodes = set()
        for v in pc:
            if v < M:
                # 字符或.号就match到v+1
                if re[v] == txt[i] or re[v] == ".":
                    match_nodes.add(v+1)
        
        pc = set()
        dfs = DirectedDFS(G, match_nodes)
        # 计算新一轮可到达状态
        for v in range(G.V):
            if dfs.marked(v):
                pc.add(v)
    
    # 判断是否到达接受状态
    if M in pc:
        return True
    else:
        return False

def NFA(regexp: str):
    """根据给定表达式构造NFA(非确定有限自动机)"""
    ops = []
    re = list(regexp)
    M = len(re)
    G = Digraph(M+1)  # 最后加一个接受状态

    for i in range(M):
        lp = i
        if re[i] == "(" or re[i] == "|":
            ops.append(i)
        elif re[i] == ")":
            op_i = ops.pop()
            if re[op_i] == "|":
                lp = ops.pop()
                G.add_edge(lp, op_i+1)
                G.add_edge(op_i, i)
            else:
                lp = op_i
        
        if i < M-1 and re[i+1] == "*":  # 查看下一个字符
            G.add_edge(lp, i+1)
            G.add_edge(i+1, lp)
        
        if re[i] == "(" or re[i] == "*" or re[i] == ")":
            G.add_edge(i, i+1)
    
    return G, re


def match(regexp: str, txt: str):
    """返回字符串txt是否满足表达式regexp的结果"""
    G, re = NFA("(" + regexp + ")")
    return recognizes(txt, G, re)


def search(regexp: str, txt: str):
    """返回字符串txt中能否搜索到满足表达式regexp的子模式"""
    G, re = NFA("(.*" + regexp + ".*)")
    return recognizes(txt, G, re)

