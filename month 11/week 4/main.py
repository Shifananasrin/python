from math_operation.basic_opertion import Arithmetic
from math_operation.geometry import Area
print("Arthematic operation")
print("5+3= ",Arithmetic.Add(5 , 3))
print("10 - 7 = ",Arithmetic.substract(10, 7))
print("5*3= ",Arithmetic.multiply(5 , 3))
print("5*3= ",Arithmetic.multiply(5 , 3))
print("8/2 = ",Arithmetic.divide(8  , 2))
print("8/0 = ",Arithmetic.divide(8  , 0))
print("Area calculate")
print("rectangle(length=5, width=3):",Area.rectangle_area(5,3))
print("circle (radius=7):",Area.circle_area(7))
print("triangle_area (base=4, height=5):",Area.triangle_area(4, 5))



