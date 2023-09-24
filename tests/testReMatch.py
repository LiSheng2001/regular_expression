import unittest
from DirectDFS import DirectedDFS, Digraph
from Recognize import match


class TestMatch(unittest.TestCase):
    """测试match方法"""
    def test_match(self):
        examples = ["AAA", "ABD", "ABCCBD"]
        regexps = ["(A*B|AC)D", "(A*B|AC)D", "(A*B|AC)D"]
        results = [False, True, False]

        # 开启子测试
        for i in range(len(examples)):
            with self.subTest(index=i, input=[examples[i], regexps[i]], result=results[i]):
                r = match(regexps[i], examples[i])
                self.assertEqual(r, results[i])