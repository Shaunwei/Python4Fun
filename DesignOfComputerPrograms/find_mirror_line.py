'''
Question: Given n points on a x-y axis, if it exists a line that makes each point has symmetry point against this line.

Algorithm: 
    Brute Force O(n ^ 2): find n^2 lines between any two points, and test each line make all points symmetric

    Better algorithm O(n): 
        Observations: 
            Let's name this line L, which makes all points symmetric.
            If we only have point A and point B,
                then there are two line L
                1: the perpendicular bisector of the line connecting point A and pointB
                2: the line crossing A and B

            Then for the case of n points:
            - For arbitrary point X, it can form 2 * (n - 1) perpendicular bisectors with other n - 1 points.
            - If L exists, this L should be within the 2 * (n - 1) perpendicular bisectors.

            - So, for 2 * (n - 1) lines, if any line make other points are symmetric
                - then L exist
                - else L NOT exist
FYI: there are many corner cases, let's just assume no same points
'''


class LineFinder:
    @classmethod
    def find(cls, points):
        """
        Main Algorithm
        @params: List[[int, int]]
        @return: str
        """
        if not points or len(points) < 2:
            return ''

        point_x = points[0]
        for line in cls.form_lines(point_x, points[1:]):
            if cls.is_valid(line, points):
                return cls.build(line)
        return ''


    @classmethod
    def form_lines(cls, x, points):
        for point in points:
            yield HighSchoolMath.find_crossing_line(x, point)
            yield HighSchoolMath.find_perpendicular_bisector(x, point)

    @classmethod
    def is_valid(cls, line, points):
        """
        check if symmetric point exist
        """
        points_set = set(points)
        for point in points_set:
            m_point = HighSchoolMath.find_symmetric_point(line, point)
            if m_point not in points_set:
                return False
        return True


    # helper method
    @classmethod
    def build(cls, line):
        if line[0] == 'x' or line[0] == 'y':
            return '%s = %d' % (line[0], line[1])
        else:
            return 'y = %d * x + %d' % (line[0], line[1])





###
# Helper Class
# Pure Math!!
class HighSchoolMath:
    @staticmethod
    def find_perpendicular_bisector(point_a, point_b):
        """
        ax + b = y
        if vertical line: ['x', float]
        if horizontal line: ['y', float]
        @return: ({float|str}, float)
        """
        x1, y1 = point_a
        x2, y2 = point_b

        if x1 == x2:
            # y = %d
            return ('y', (y1 + y2) / 2.0)
        if y1 == y2:
            # x = %d
            return ('x', (x1 + x2) / 2.0)

        a, _ = HighSchoolMath.find_crossing_line(point_a, point_b)
        a = -a
        b = (y1 + y2) / 2.0 - a * ((x1 + x2) / 2.0)
        return (a, b)

    @staticmethod
    def find_crossing_line(point_a, point_b):
        """
        ax + b = y
        @return: [a, b]
        """
        x1, y1 = point_a
        x2, y2 = point_b

        if x1 == x2:
            # y = %d
            return ('y', (y1 + y2) / 2.0)
        if y1 == y2:
            # x = %d
            return ('x', (x1 + x2) / 2.0)

        a = (y1 - y2) / (x1 - x2)
        b = y1 - a * x1
        return (a, b)

    @staticmethod
    def find_symmetric_point(line, point):
        a, b = line
        x1, y1 = point
        if a == 'y':
            return (x1, 2 * b - y1)
        if a == 'x':
            return (2 * b - x1, y1)

        p_line = HighSchoolMath._find_perpendicular(line, point)
        p_x, p_y = HighSchoolMath._find_intersection(line, p_line)

        x2 = 2 * p_x - x1
        y2 = 2 * p_y - y1
        return (x2, y2)

    @staticmethod
    def _find_perpendicular(line, point):
        a, b = line
        x, y = point
        a = -a
        b = y - a * x
        return (a, b)

    @staticmethod
    def _find_intersection(line1, line2):
        a1, b1 = line1
        a2, b2 = line2
        x = 1.0 * (b2 - b1) / (a1 - a2)
        y = a1 * x + b1
        return (x, y)


if __name__ == '__main__':
    test_points = [(1, 0), (0, 1)]
    assert (-1.0, 1.0) == HighSchoolMath.find_crossing_line(*test_points)
    assert (1.0, 0.0) == HighSchoolMath.find_perpendicular_bisector(*test_points)
    assert (-1.0, 1.0) == HighSchoolMath._find_perpendicular((1.0, 0.0), (0, 1))
    assert (0.5, 0.5) == HighSchoolMath._find_intersection((-1.0, 1.0), (1.0, 0.0))
    assert (1.0, 0.0) == HighSchoolMath.find_symmetric_point((1.0, 0.0), (0, 1))

    # # [x, y]
    points = [
        (0, 3),
        (1, 1),
        (3, 1),
        (4, 3)
    ]
    print(points)
    print(LineFinder.find(points))
    print('=========')

    points = [
        (3, 0),
        (0, 3)
    ]
    print(points)
    print(LineFinder.find(points))
    print('=========')

    points = [
        (3, 0),
        (1, 0)
    ]
    print(points)
    print(LineFinder.find(points))
    print('=========')

    points = [
        (0, 1),
        (0, 3)
    ]
    print(points)
    print(LineFinder.find(points))
    print('=========')
