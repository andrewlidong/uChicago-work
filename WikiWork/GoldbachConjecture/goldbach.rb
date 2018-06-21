def is_prime(n)
  return false if n <= 1
  2.upto(Math.sqrt(n).to_i) do |x|
    return false if n%x == 0
  end
  true
end

def two_prime(n)
	two_primes = []
	arr = *(1..n)
	arr.delete_if{|e| is_prime(e) != true}
	for i in arr
		if is_prime(n-i) == true
			two_primes << i
			two_primes << n-i
			return two_primes
		end
	end
end

puts two_prime(100)