#point to demo the class def
import math

class Point:
    'Represents a point in two-dimensional geometric coordinates'
    
    def __init__(self, x=0, y=0):
        '''Initialize the positon of a new point. The x and y
       coordinates can be specified. If they are not, the point
       defaults to the origin.'''
        self.move(x,y)
        
    def reset(self):
        'Reset the point back to the geometric origin: 0, 0'
        self.move(0,0)
    
    def move(self,x,y):
        """Move the point to a new location in two-dimensional space."""
        self.x = x
        self.y = y
    
    def calculate_distance(self, other_point):
        """Claculate the distance from this point to a second point
           passed as a parameter.
           
           This function uses the Pythoagorean Theorem to calculate
           the distance between the two points. The distance is 
           returned as a float."""
        return math.sqrt(
                   (self.x - other_point.x)**2 +
                   (self.y - other_point.y)**2)



point1 = Point()
#Point.reset(p)
#p.reset()
point2 = Point()

point1.reset()
point2.move(5,0)

print(point2.calculate_distance(point1))
assert (point2.calculate_distance(point1) ==
        point1.calculate_distance(point2))

point1.move(3,4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))
