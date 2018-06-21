-- A point is a point in the xy plane, represented by x and y coordinates

data Point = Point Double Double
	deriving (Show, Eq)
	
-- A line segment is a straigt line of finite length, defined by its two end points.  

data LineSegment = LineSegment Point Point
	deriving (Show, Eq)
	
-- A path is a 2D path in the xy-plane.  It can be extended to support lines, curves and arbitrary paths

data Path = Line Double Double
	| Parabola Double Double Double
	deriving (Show, Eq)

--intersects checks if a LineSegment intersects with a line
--intersects now also checks if a LineSegment intersects with a parabola

intersects :: LineSegment -> Path -> Bool
intersects foo (Line a b) = pointBetweenSegments foo $ lineIntersection (linearization foo) (Line a b)
intersects foo (Parabola a b c) = any (pointBetweenSegments foo) $ parabolaIntersection (linearization foo) (Parabola a b c)

pointBetweenSegments :: LineSegment -> Point -> Bool
pointBetweenSegments (LineSegment (Point a b) (Point c d)) (Point e f)
				| (a <= e && e <= c) =
									if (b <= f && f <= d)
									then True
									else if (f <= b && d <= f)
									then True
									else False
				| (e <= a && c <= e) =
									if (b <= f && f <= d)
									then True
									else if (f <= b && d <= f)
									then True
									else False
				| otherwise = False

linearization :: LineSegment -> Path
linearization (LineSegment (Point a b) (Point c d)) = Line ((d-b)/(c-a))(b-a * ((d-b)/(c-a)))

lineIntersection :: Path -> Path -> Point
lineIntersection (Line a b) (Line c d) = Point ((d-b)/(a-c)) (b + ((d-b)/(a-c)) * a)

parabolaIntersection :: Path -> Path -> [Point]
parabolaIntersection (Line a b) (Parabola c d e)
			| ((d-a) ** 2 - (4 * c * (e-b))) < 0 = 
				[]
			| ((d-a) ** 2 - (4 * c * (e-b))) == 0 = 
				[(Point ((d-a)/(2*c)) (a * ((d-a)/(2*c))+b))]
			| ((d-a) ** 2 - (4 * c * (e-b))) > 0 =
				[(Point (((d-a) - (sqrt ((d-a)^2 - (4 * c * (e - b)))))/(2 * c)) (a * ((d-a) - (sqrt ((d-a)^2 - (4 * c * (e - b)))))/(2 * c) + b)), (Point (((d-a) + (sqrt ((d-a)^2 - (4 * c * (e - b)))))/(2 * c)) (a * ((d-a) + (sqrt ((d-a)^2 - (4 * c * (e - b)))))/(2 * c)+ b))]

test1 = intersects (LineSegment (Point 1 1)(Point 0 0)) (Line (-1) 0)
test2 = intersects (LineSegment (Point 1 1)(Point 0 0)) (Parabola 1 0 0)

--we define a new datatype Shape which can be a Triangle, Quadrilateral or a Circle

data Shape = Triangle Point Point Point | Quadrilateral Point Point Point Point | Circle Point Double
	deriving (Show, Eq)
	
--we define a new datatype BoundingBox by two points, it's lower-left and upper-right corners

data BoundingBox = BoundingBox Point Point
	deriving (Show, Eq)
	
--boundShape maps a Shape to a BoundingBox, which then maps that shape to its minimum bounding rectangle

boundShape :: Shape -> BoundingBox
boundShape (Triangle (Point a b) (Point c d) (Point e f)) = BoundingBox (Point (minimum [a,c,e]) (minimum [b,d,f])) (Point (maximum [a,c,e]) (maximum [b,d,f]))
boundShape (Quadrilateral (Point a b) (Point c d) (Point e f) (Point g h)) = BoundingBox (Point (minimum [a,c,e,g]) (minimum [b,d,f,h])) (Point (maximum [a,c,e,g]) (maximum [b,d,f,h]))
boundShape (Circle (Point a b) c) = BoundingBox (Point (a-c) (b-c)) (Point (a + c) (b + c))

test3 = boundShape (Triangle (Point 0 0) (Point 6 2) (Point 4 3)) == BoundingBox (Point 0 0) (Point 6 3)
test4 = boundShape (Quadrilateral (Point 0 0) (Point (-12) 5) (Point 2 4) (Point 0 24)) == BoundingBox (Point (-12) 0) (Point 2 24)
test5 = boundShape (Circle (Point 1 1) 5) == BoundingBox (Point (-4) (-4)) (Point 6 6)

--intersectsBB takes a BoundingBox and a Path and checks to see if the path intersects the bounding box

intersectsBB :: BoundingBox -> Path -> Bool
intersectsBB (BoundingBox (Point a b) (Point c d)) path = or 	[intersects (LineSegment (Point a b) (Point a d)) path, 
																intersects (LineSegment (Point a d) (Point c d)) path, 
																intersects (LineSegment (Point c d) (Point c b)) path, 
																intersects (LineSegment (Point a b) (Point c b)) path]

test6 = intersectsBB (BoundingBox (Point 0 0) (Point 1 1)) (Line 1 1)

--mightIntersectShape checks if a path intersects the bounding box of a shape

mightIntersectShape :: Shape -> Path -> Bool
mightIntersectShape shape path = intersectsBB (boundShape shape) path

test7 = mightIntersectShape (Circle (Point 0 0) 1) (Line 1 1)

--test8 = intersectsBB (BoundingBox (Point 0 0) (Point 1 1)) (Parabola 0 0 1)

tests = test1 &&
		test2 &&
		test3 &&
		test4 &&
		test5 &&
		test6 &&
		test7
