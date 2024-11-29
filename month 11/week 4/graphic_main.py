from package_graphics.graphics import circle
from package_graphics.graphics import rectangle
from package_graphics._3D_graphics import Cuboid
from package_graphics._3D_graphics import sphere
print("area and perimeter of circle")
print(" area of circle (radius=10):",circle.circle_area(10))
print("perimeter of circle (radius=10):",circle.circle_perimeter(10))

print("area and perimeter of rectangle")
print(" area of rectangle(length=4, width=3)",rectangle.rectangle_area(4,3))
print(" perimeter of rectangle(length=4, width=3)",rectangle.rectangle_perimeter(4,3))

print("area and perimeter of cuboid")
print(" area of cuboid(length=6, width=2,height=5)",Cuboid.cubiod_area(6,2,5))
print(" perimeter of cuboid(length=6, width=2,height=5)",Cuboid.cubiod_perimetrer(6,2,5))

print("area and perimeter of sphere")
print(" area of sphere(radius=7)",sphere.sphere_area(7))
print(" perimeter of sphere(radius=7)",sphere.sphere_perimetrer(7))


