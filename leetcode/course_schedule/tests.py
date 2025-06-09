import unittest
from courseSchedule import Solution

class TestCourseSchedule(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test_single_course_no_prereqs(self):
        self.assertTrue(self.sol.canFinish(1, []))

    def test_two_courses_no_cycle(self):
        self.assertTrue(self.sol.canFinish(2, [[1, 0]]))

    def test_two_courses_with_cycle(self):
        self.assertFalse(self.sol.canFinish(2, [[1, 0], [0, 1]]))

    def test_three_courses_with_cycle(self):
        self.assertFalse(self.sol.canFinish(3, [[0, 1], [1, 2], [2, 0]]))

    def test_three_courses_no_cycle(self):
        self.assertTrue(self.sol.canFinish(3, [[1, 0], [2, 1]]))

    def test_multiple_dependencies_no_cycle(self):
        self.assertTrue(self.sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

    def test_multiple_dependencies_with_cycle(self):
        self.assertFalse(self.sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [1, 3]]))

    def test_empty_prerequisites(self):
        self.assertTrue(self.sol.canFinish(5, []))

    def test_self_dependency(self):
        self.assertFalse(self.sol.canFinish(1, [[0, 0]]))

    def test_large_no_cycle(self):
        self.assertTrue(self.sol.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3]]))

    def test_large_with_cycle(self):
        self.assertFalse(self.sol.canFinish(5, [[1, 0], [2, 1], [3, 2], [1, 3]]))

if __name__ == "__main__":
    unittest.main()