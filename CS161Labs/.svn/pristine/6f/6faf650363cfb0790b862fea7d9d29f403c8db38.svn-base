import Data.Complex

testSubjectA = Poly [1, 2]
testSubjectB = Poly [1, -1]

data Poly = Poly [Complex Double]

--polyCoeffs allows us to access the chosen representation.  

polyCoeffs :: Poly -> [Complex Double]
polyCoeffs (Poly xs) = xs

--polyEval allows us to evaluate the polynomial

polyEval :: Poly -> Complex Double -> Complex Double
polyEval (Poly []) a = 0
polyEval (Poly (x:xs)) a = x + a * polyEval (Poly xs) a

--polyAdd allows us to add polynomials

polyAdd :: Poly -> Poly -> Poly
polyAdd a b = Poly $ addLists (polyCoeffs a) (polyCoeffs b)

test1 = (polyCoeffs $ polyAdd testSubjectA testSubjectB) == [2, 1]

addLists :: Num a => [a] -> [a] -> [a]
addLists [] [] = []
addLists [] (x:xs) = x : addLists [] xs
addLists (x:xs) [] = x : addLists xs []
addLists (x:xs) (y:ys) = (y + x) : addLists xs ys

--polyScalMult allows us to take a polynomial and multiply it with a scalar

polyScalMult :: Poly -> Complex Double -> Poly
polyScalMult a b = Poly $ scalMultLists (polyCoeffs a) b

scalMultLists :: Num a => [a] -> a -> [a]
scalMultLists xs a = map (*a) xs

test2 = (scalMultLists (polyCoeffs testSubjectB) (5.5)) == [5.5, -5.5]

--polyNegate allows us to take the negative of a polynomial

polyNegate :: Poly -> Poly
polyNegate a = polyScalMult a (-1)

test3 = polyCoeffs (polyNegate testSubjectA) == [-1, -2]

--polyDiff allows us to take the difference between two polynomials

polyDiff :: Poly -> Poly -> Poly
polyDiff a b = polyAdd a (polyNegate b)

test4 = polyCoeffs (polyDiff testSubjectA testSubjectB) == [0, 3]

--polyAbs takes the absolute value of the coefficients

polyAbs :: Poly -> Poly
polyAbs a = Poly (absolutePoly a)

absolutePoly :: Poly -> [Complex Double]
absolutePoly (Poly []) = []
absolutePoly (Poly (x:xs)) = (abs x) : absolutePoly (Poly xs)

test5 = polyCoeffs (polyAbs testSubjectB) == [1,1]

--polyApproxEqual allows us to check for approximate equality

polyApproxEqual :: Poly -> Poly -> Double -> Bool
polyApproxEqual a b epsilon = epsilon >= sum (map magnitude (polyCoeffs (polyDiff a b)))

test6 = polyApproxEqual testSubjectA testSubjectA (0.00005) == True

--polyMult allows us to multiply polynomials

polyMult :: Poly -> Poly -> Poly
polyMult a b = Poly $ multLists (polyCoeffs a) (polyCoeffs b)

multLists :: Num a => [a] -> [a] -> [a]
multLists _ [] = []
multLists xs (y:ys) = addLists (map (*y) xs) (0: (multLists xs ys))

test7 = polyCoeffs (polyMult testSubjectA testSubjectB) == [1,1,-2]

--new datatype polypoints maintains two lists of x locations and y locations
--locations correspond to the values of the polynomial and the polynomial degree

data PolyPoints = PolyPoints Int [Complex Double] [Complex Double]

--toPolyPoints maps a polynomial and a set of points to the PolyPoints datatype

toPolyPoints :: Poly -> [Complex Double] -> PolyPoints
toPolyPoints a xs
	| (length xs) < (length $polyCoeffs a) = undefined
	| otherwise = PolyPoints (length (polyCoeffs a) -1) xs (createList a xs)
	
createList :: Poly -> [Complex Double] -> [Complex Double]
createList a xs = map (polyEval a) xs

--helper functions for getting degrees, listX and listY

getDegree :: PolyPoints -> Int
getDegree (PolyPoints deg _ _) = deg

getListX :: PolyPoints -> [Complex Double]
getListX (PolyPoints _ xs _) = xs

getListY :: PolyPoints -> [Complex Double]
getListY (PolyPoints _ _ ys) = ys

--polyPointsAdd allows for addition of two PolyPoints

polyPointsAdd :: PolyPoints -> PolyPoints -> PolyPoints
polyPointsAdd (PolyPoints deg ax ay) (PolyPoints _ _ by) = PolyPoints deg ax (addLists ay by)

--polyPointsScalMult allows for scalar multiplication of a PolyPoint

polyPointsScalMult :: PolyPoints -> Complex Double -> PolyPoints
polyPointsScalMult a b = PolyPoints (getDegree a) (getListX a) (scalMultLists (getListY a) b)

--polyPointsMult allows for multiplication of two PolyPoints

polyPointsMult :: PolyPoints -> PolyPoints -> PolyPoints
polyPointsMult a b = PolyPoints (getDegree a + getDegree b) (getListX a) (multListsPoints (getListY a) (getListY b))

multListsPoints :: Num a => [a] -> [a] -> [a]
multListsPoints [] _ = []
multListsPoints _ [] = []
multListsPoints (x:xs) (y:ys) = x * y : multLists xs ys

--the datatype PolyPointsFFT serves as the new PolyPoints type for our fft function

data PolyPointsFFT = PolyPointsFFT PolyPoints

--toPolyPointsFFT allows us get PolyPointsFFT from Poly

toPolyPointsFFT :: Poly -> PolyPointsFFT
toPolyPointsFFT a
	| isPowerOfTwo (length $ polyCoeffs a) = fft a
	| otherwise = fft (polyPad a)
	
--helper functions for getting degree, ListX, ListY and points

getDegreeFFT :: PolyPointsFFT -> Int
getDegreeFFT (PolyPointsFFT (PolyPoints deg _ _)) = deg

getListXFFT :: PolyPointsFFT -> [Complex Double]
getListXFFT (PolyPointsFFT (PolyPoints _ xs _)) = xs

getListYFFT :: PolyPointsFFT -> [Complex Double]
getListYFFT (PolyPointsFFT (PolyPoints _ _ ys)) = ys

getPointsFFT :: PolyPointsFFT -> [(Complex Double, Complex Double)]
getPointsFFT a = zip (getListXFFT a) (getListYFFT a)

--helper functions for pading lists and checking that length is power of 2
polyPad :: Poly -> Poly
polyPad a = Poly (padListBack $ polyCoeffs a)

padListBack :: Num a => [a] -> [a]
padListBack = reverse . padListFront . reverse

padListFront :: Num a => [a] -> [a]
padListFront xs
	| isPowerOfTwo (length xs) = xs
	| otherwise = padListFront (0 : xs)

isPowerOfTwo :: Int -> Bool
isPowerOfTwo a
	| a == 1 = True
	| a `mod` 2 == 1 = False
	| otherwise = isPowerOfTwo (a `div` 2)
	
--the Fast Fourier Transform

fft :: Poly -> PolyPointsFFT
fft a
	| not (isPowerOfTwo (length $ polyCoeffs a)) = fft (polyPad a)
	| otherwise = PolyPointsFFT (PolyPoints (length (polyCoeffs a) -1)
											(createListX $ length $ polyCoeffs a)
											(map (fastPolyEval a)
												(createListX (length $ polyCoeffs a))))
												
-- fastPolyEval recursively implements the divide and conquer algorithm

fastPolyEval :: Poly -> Complex Double -> Complex Double
fastPolyEval (Poly []) x1 = 0
fastPolyEval (Poly (x2:[])) _ = x2
fastPolyEval a x1 = fastPolyEval (getEvenPoly a) (x1 ** 2) + x1 * (fastPolyEval (getOddPoly a) (x1 ** 2))
				   
-- getEvenPoly returns a Poly consisting of the even term coefficients

getEvenPoly :: Poly -> Poly	
getEvenPoly a = Poly $ getListEvens $ polyCoeffs a

getListEvens :: [a] -> [a]
getListEvens [] = []
getListEvens (a:[]) = (a:[])
getListEvens (a:b:as) = a : getListEvens as

-- getOddPoly returns a Poly consisting of the odd term coefficients 

getOddPoly :: Poly -> Poly
getOddPoly a = Poly $ getListOdds $ polyCoeffs a

getListOdds :: [a] -> [a]
getListOdds as = getListEvens $ tail as

--createListX creates a list of nth roots of unity

createListX :: Int -> [Complex Double]
createListX a = reverse $ getNthRoots a (a-1)

getNthRoots :: Int -> Int -> [Complex Double]
getNthRoots _ 0 = 1 : []
getNthRoots deg a = (cis $ (-2) * pi * (fromIntegral a) / (fromIntegral deg)) : (getNthRoots deg (a - 1))

--invfft allows us to take the inverse of the fourier transformation.  
 
invfft :: PolyPointsFFT -> Poly
invfft a = Poly (divideByN $ conjugateList $ getListYFFT $ fft $ Poly $ getConjugate a)
 
test8 = polyApproxEqual (invfft (fft testSubjectA)) testSubjectA (0.0005) == True

--conjugateList allows us to take the conjugate of a list
 
conjugateList :: [Complex Double] -> [Complex Double]
conjugateList xs = map conjugate xs
 
--getConjugate gives us the conjugates of the ListY of PolyPointsFFT
 
getConjugate :: PolyPointsFFT -> [Complex Double]
getConjugate a = conjugateList (getListYFFT a)
 
--divideByN divides all the elements of a list by the number of elements
 
divideByN :: Fractional a => [a] -> [a]
divideByN xs = map (flip (/) $ fromIntegral $ length xs) xs

--polyMultFFT uses fft to quickly multiply polynomials

polyMultFFT :: Poly -> Poly -> Poly
polyMultFFT a b
	| (length $ polyCoeffs a) < (length $ polyCoeffs b) = polyMultFFT b a
	| otherwise = invfft (polyPointsMultFFT (fft $ polyPad' a) (fft $ polyPadUntil b $ polyPad' a))
	
polyPointsMultFFT :: PolyPointsFFT -> PolyPointsFFT -> PolyPointsFFT
polyPointsMultFFT (PolyPointsFFT a) (PolyPointsFFT b) = PolyPointsFFT (polyPointsMult a b)

--polyPad' pads a poly whose length is equal to a dyadic integer greater than or equal to 2* the Poly's initial length

polyPad' :: Poly -> Poly
polyPad' a = polyPad $ Poly $ reverse $ 0 : (reverse $ polyCoeffs $ polyPad a)

--polyPadUntil pads a shorter poly until its length matches the longer poly

polyPadUntil :: Poly -> Poly -> Poly
polyPadUntil a b
	| (length $ polyCoeffs a) == (length $ polyCoeffs b) = a
	| (length $ polyCoeffs a) > (length $ polyCoeffs b) = undefined
	| otherwise = polyPadUntil (polyPad' a) b
	
--test9 = polyApproxEqual (polyMultFFT testSubjectA testSubjectB) (polyMult testSubjectA testSubjectB) 0.005

tests = test1 &&
		test2 &&
		test3 &&
		test4 &&
		test5 &&
		test6 &&
		test7 &&
		test8 &&
--		test9
