import pytest
import math
import src.shapes as shapes


class TestCircle:
    def setup_method(self, method):
        print("Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print("Tearing down {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius**2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius

    def test_area_not_equal(self, weird_rectangle):
        assert self.circle.area() != weird_rectangle.area()
