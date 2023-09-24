import unittest
from Recognize import search


class TestSearch(unittest.TestCase):
    """测试search方法"""
    def test_search(self):
        examples = ["AAA", "ABD", "ABCCBD"]
        regexps = ["(A*B|AC)D", "(A*B|AC)D", "(A*B|AC)D"]
        results = [False, True, True]

        # 开启子测试
        for i in range(len(examples)):
            with self.subTest(index=i, input=[examples[i], regexps[i]], result=results[i]):
                r = search(regexps[i], examples[i])
                self.assertEqual(r, results[i])