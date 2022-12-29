# Python 3 program to
# compute sum of digits in
# number.

# Function to get sum of digits


def getSum(n):

	sum = 0
	while (n != 0):

		sum = sum + int(n % 10)
		n = int(n/10)

	return sum


# Driver code
if __name__ == "__main__":
	n = 687

	# Function call
	print(getSum(n))
