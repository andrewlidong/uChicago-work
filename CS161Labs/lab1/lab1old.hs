import Data.Complex

{-Implement tests later-}

tester1 = Poly [1,2,-1]
tester2 = Poly [1,2]


data Poly = Poly [Complex Double]
	deriving (Show,Eq)

--polyCoeffs takes the coefficients of the polynomial.  

polyCoeffs :: Poly -> [Complex Double]
polyCoeffs (Poly (x:xs)) = x:xs

--polyEval makes a polynomial evaluable

polyEval :: Poly -> Complex Double -> Complex Double
polyEval (Poly []) a = 0
polyEval (Poly (x:xs)) a = x + a * (polyEval (Poly xs) a)

{-

--old version of polyAdd

polyAdd :: Poly -> Poly -> Poly
polyAdd x1 x2 
	| length (polyCoeffs x1) == length (polyCoeffs x2) = Poly (zipWith (+) (polyCoeffs x1) (polyCoeffs x2))
	| length (polyCoeffs x1) < length (polyCoeffs x2) = polyAdd (Poly (polyCoeffs x1 ++ [0])) x2
	| length (polyCoeffs x1) > length (polyCoeffs x2) = polyAdd x1 (Poly (polyCoeffs x2 ++ [0]))
-}

--polyAdd introduces a helper function, polyAdd' which circumvents the need to check lengths as in old polyAdd

polyAdd :: Poly -> Poly -> Poly
polyAdd x1 x2 = Poly $ polyAdd' (polyCoeffs x1) (polyCoeffs x2)

polyAdd' :: Num a => [a] -> [a] -> [a]
polyAdd' [] [] = []
polyAdd' [] (x:xs) = x : polyAdd' [] xs
polyAdd' (x:xs) [] = x : polyAdd' xs []
polyAdd' (x:xs) (y:ys) = (x+y) : polyAdd' xs ys

--polyScalMult allows for multiplication of a polynomial with a scalar

polyScalMult :: Poly -> Complex Double -> Poly
polyScalMult x1 x2 = Poly $ map (*x2) (polyCoeffs x1)

--polyNegate takes a polynomial and multiplies it by -1 

polyNegate :: Poly -> Poly
polyNegate x = polyScalMult x (-1)

--polyDiff takes two polynomials and outputs their difference.  

polyDiff :: Poly -> Poly -> Poly
polyDiff x1 x2 = polyAdd x1 $ polyNegate x2

--polyAbs takes a polynomial and returns the absolute value of that polynomial.  

polyAbs :: Poly -> Poly
polyAbs x = Poly $ map (abs) (polyCoeffs x)

--polyApproxEqual takes two polynomials and checks if they are approximately equal (if their difference is less than epsilon)

polyApproxEqual :: Poly -> Poly -> Bool
polyApproxEqual x1 x2
	| realPart (sum (polyCoeffs (polyAbs (polyDiff x1 x2)))) < (0.0001) = True
	| otherwise = False

--polyMult multiplies two polynomials together

polyMult :: Poly -> Poly -> Poly
polyMult x1 x2 = Poly $ polyMult' (polyCoeffs x1) (polyCoeffs x2)

polyMult' :: Num a => [a] -> [a] -> [a]
polyMult' _ [] = []
polyMult' xs (y:ys) = polyAdd' (map (*y) xs) (0 : (polyMult' xs ys))


data PolyPoints = PolyPoints (Int) [Complex Double] [Complex Double]
	deriving (Show)

polyPointsEval :: Poly -> [Complex Double] -> [Complex Double]
polyPointsEval (Poly x) [] = []
polyPointsEval (Poly x) (y:ys) = (polyEval (Poly x) y) : (polyPointsEval (Poly x) ys)

toPolyPoints :: Poly -> [Complex Double] -> PolyPoints
toPolyPoints (Poly x) (y:ys) = PolyPoints (length(x) -1) (y:ys) (polyPointsEval (Poly x) (y:ys))

polyPointsAdd :: PolyPoints -> PolyPoints -> PolyPoints
polyPointsAdd (PolyPoints x1 x2 x3) (PolyPoints y1 y2 y3)
	| x2 == y2 = (PolyPoints x1 x2 (zipWith (+) x3 y3))
	| otherwise = undefined

polyPointsScalMult :: PolyPoints -> Complex Double -> PolyPoints
polyPointsScalMult (PolyPoints x1 x2 x3) x4 = PolyPoints x1 x2 (map (x4*) x3)

polyPointsMult :: PolyPoints -> PolyPoints -> PolyPoints
polyPointsMult (PolyPoints x1 x2 x3) (PolyPoints y1 y2 y3)
	| (x2 == y2) && (x1 + y1 + 1 > length (x2)) = PolyPoints (x1 + y1) x2 (zipWith (*) x3 y3)
	| otherwise = undefined


data PolyPointsFFT = PolyPointsFFT Int [Complex Double]
	deriving (Show,Eq)

fft:: Poly -> Int -> PolyPointsFFT
fft (Poly x) y
	| not $ elem (length x) (take (length x) takeSecondPower) = undefined
	| otherwise = PolyPointsFFT (length x) (fft2 (Poly x) (rootsOfUnity (fromIntegral (length (polyCoeffs(polyPad (Poly x)))) :+ 0) (0 :+ 0)) y)

fft1 :: Poly -> Complex Double -> Int -> Complex Double
fft1 (Poly []) y z = 0
fft1 (Poly x) y z
    | length(x) == 1 = (head x)
    | otherwise = (+) (fft1 (Poly (evenPowerTerms (Poly x))) y (z+1)) (fft1 (Poly (map (*(y**(2^z))) (oddPowerTerms (Poly x)))) y (z+1))

fft2 :: Poly -> [Complex Double] -> Int -> [Complex Double]
fft2 (Poly x) [] y = []
fft2 (Poly x) (z:zs) y= (fft1 (Poly x) z y) : (fft2 (Poly x) zs y)

oddPowerTerms :: Poly -> [Complex Double]
oddPowerTerms (Poly []) = []
oddPowerTerms (Poly x)
    | length (x) == 1 = []
    | odd (length (x)) = oddPowerTerms (Poly (init x))
    | even (length (x)) = oddPowerTerms (Poly (init x)) ++ [last x]

evenPowerTerms :: Poly -> [Complex Double]
evenPowerTerms (Poly []) = []
evenPowerTerms (Poly x)
    | length(x) == 1 = [head x]
    | even (length(x)) = evenPowerTerms (Poly (init x))
    | odd (length(x)) = evenPowerTerms (Poly (init x)) ++ [last x]

rootsOfUnity :: Complex Double -> Complex Double -> [Complex Double]
rootsOfUnity x1 x2
    | (magnitude x1) < (magnitude x2) = exp(((-2)*pi*(0:+1)*x1)/x2) : (rootsOfUnity x2 (x1+1))
    | otherwise = []

takeSecondPower :: [Int]
takeSecondPower = map (2^) [0,1..]

polyPad:: Poly -> Poly
polyPad (Poly x)
    | elem (length x) (take (length x) takeSecondPower) == True = Poly x
    | otherwise = polyPad (Poly (x ++ [0]))

toPolyPointsFFT :: Poly -> PolyPointsFFT
toPolyPointsFFT (Poly x) = fft (polyPad (Poly x)) 0

invfft :: PolyPointsFFT -> Poly
invfft (PolyPointsFFT x (y:ys)) =  xandconjugate(PolyPointsFFT x (fourier (PolyPointsFFT x (zconjugate (y:ys)))))

xandconjugate :: PolyPointsFFT -> Poly
xandconjugate (PolyPointsFFT x (y:ys)) = Poly (map (/(fromIntegral x :+ 0))(zconjugate (y:ys)))

zconjugate :: [Complex Double] -> [Complex Double]
zconjugate (z:zs) = map conjugate (z:zs)
zeroes 0 = []
zeroes x = 0: zeroes (x-1)

fourier :: PolyPointsFFT -> [Complex Double] 
fourier (PolyPointsFFT x []) = zeroes x
fourier (PolyPointsFFT x (y:ys))=  zipWith (+) (map ((*y). (**((fromIntegral x :+0)-(fromIntegral (length ys) :+ 0)-1))) (rootsOfUnity (fromIntegral x :+ 0) (0 :+ 0))) (fourier (PolyPointsFFT x ys))

fromPolyPointsFFT :: PolyPointsFFT -> Poly
fromPolyPointsFFT = invfft


polyMultFFT :: Poly -> Poly -> Poly
polyMultFFT x y = invfft(PolyPointsFFT (lengthPoly (fillup x y y)) (zipWith (*) (polyCoeffs(fftCoeffs (toPolyPointsFFT (fillup x y x)))) (polyCoeffs(fftCoeffs (toPolyPointsFFT (fillup x y y))))))

fftCoeffs :: PolyPointsFFT -> Poly 
fftCoeffs (PolyPointsFFT x y) = Poly y

addzerotopoly:: Poly -> Int -> Poly
addzerotopoly(Poly (x:xs)) 0 = (Poly (x:xs))
addzerotopoly(Poly (x:xs)) a = addzerotopoly(Poly ((x:xs)++ [0])) (a-1)

fillup :: Poly -> Poly -> Poly -> Poly
fillup x y z
    | (lengthPoly(x) + lengthPoly(y) - 1) > lengthPoly(z) = fillup  x y (addzerotopoly z (lengthPoly(x) + lengthPoly(y) - lengthPoly(z) - 1))
    | (lengthPoly(x) + lengthPoly(y) - 1) <= lengthPoly(z) = polyPad(z)

lengthPoly :: Poly -> Int
lengthPoly (Poly (x:xs)) = length(x:xs)



test = test1 && test2 && test3 && test4

test1 = polyMult (Poly [1,2]) (Poly [1,2]) == Poly [1,4,4]

test2 = fft2 (Poly [1,1]) [1,2] 0 == [2,3] 

test3 = polyApproxEqual (fftCoeffs (fft (polyPad (Poly [0,0,0,0,1])) 0)) (Poly [1, (-1), 1, (-1), 1, (-1)])

test4 = polyApproxEqual (invfft(toPolyPointsFFT (Poly [1,2,3,4,5,6,7,8])))  (Poly [1,2,3,4,5,6,7,8])

test5 = polyApproxEqual (polyMultFFT (Poly [1,2,3,4]) (Poly [1,2,3,4,5,6])) (polyMult (Poly [1,2,3,4]) (Poly [1,2,3,4,5,6]))
