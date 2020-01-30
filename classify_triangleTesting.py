import unittest
from classify_triangle import classify_triangle

class classify_Triangle_Test(unittest.TestCase):
    def test_invalid_a(self):
        self.assertEqual(classify_triangle("hello", 8 , 3.2), "Please set parameter a to be an integer or float")
    def test_invalid_b(self):
        self.assertEqual(classify_triangle(3, "bread", 17), "Please set parameter b to be an integer or float")
    def test_invalid_c(self):
        self.assertEqual(classify_triangle(2, 18, "Gerald"), "Please set parameter c to be an integer or float")
    def test_negative_a(self):
        self.assertEqual(classify_triangle(0, 4, 2), "Cannot have values of zero or negative")
    def test_negative_b(self):
        self.assertEqual(classify_triangle(13, -4, 12), "Cannot have values of zero or negative")
    def test_negative_c(self):
        self.assertEqual(classify_triangle(21, 42, -12), "Cannot have values of zero or negative")
    def test_equilateral(self):
        self.assertEqual(classify_triangle(5.2,5.2,5.2), "This triangle is equilateral")
    def test_isosceles_ab(self):
        self.assertEqual(classify_triangle(5,5,7), "This triangle is isosceles")
    def test_isosceles_ac(self):
        self.assertEqual(classify_triangle(5,7,5), "This triangle is isosceles")
    def test_isosceles_bc(self):
        self.assertEqual(classify_triangle(5,7,7), "This triangle is isosceles")
    def test_scalene(self):
        self.assertEqual(classify_triangle(2,3,4), "This triangle is scalene")
    def test_right_scalene(self):
        self.assertEqual(classify_triangle(3,4,5), "This triangle is scalene this triangle is also a right triangle")
    def test_right_isosceles(self):
        self.assertEqual(classify_triangle(7,7, 7*2**.5), "This triangle is isosceles this triangle is also a right triangle")

if __name__ == "__main__":
    unittest.main()