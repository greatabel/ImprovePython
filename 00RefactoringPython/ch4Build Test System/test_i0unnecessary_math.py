import unittest
from i0unnecessary_math import multiply

# 使用 unittest 的标准流程为：

# 从 unittest.TestCase 派生一个子类
# 在类中定义各种以 “test_” 打头的方法
# 通过 unittest.main() 函数来启动测试

# https://www.jianshu.com/p/0b04cb0450ee

class TestUnnecessaryMath(unittest.TestCase):
    def setUp(self):
        pass
    def test_number_3_4(self):
        self.assertEqual(multiply(3,4),12)

    def test_string_a_3(self):
        self.assertEqual(multiply('a',3),'aaa')


if __name__ == "__main__":
    unittest.main()
