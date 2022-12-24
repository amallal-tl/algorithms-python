# Python3 implementation of the approach

class Node:
	
	def __init__(self, x):
		
		# To store the maximum sum for a sub-array
		self._max = x
		
		# To store the maximum prefix sum for a sub-array
		self._pre = x
		
		# To store the maximum suffix sum for a sub-array
		self._suf = x
		
		# To store the total sum for a sub-array
		self._sum = x
		
# Function to merge the 2 nodes left and right
def merg(l, r):
	
	# Creating node ans
	ans = Node(0)

	# The max prefix sum of ans Node is maximum of
	# a) max prefix sum of left Node
	# b) sum of left Node + max prefix sum of right Node
	# c) sum of left Node + sum of right Node
	ans._pre = max(l._pre, l._sum+r._pre, l._sum+r._sum)

	# The max suffix sum of ans Node is maximum of
	# a) max suffix sum of right Node
	# b) sum of right Node + max suffix sum of left Node
	# c) sum of left Node + sum of right Node
	ans._suf = max(r._suf, r._sum+l._suf, l._sum+r._sum)
	
	# Total sum of ans Node = total sum of
	# left Node + total sum of right Node
	ans._sum = l._sum + r._sum
	
	# The max sum of ans Node stores the answer
	# which is the maximum value among:
	# prefix sum of ans Node
	# suffix sum of ans Node
	# maximum value of left Node
	# maximum value of right Node
	# prefix value of left Node + suffix value of right Node
	ans._max = max(ans._pre, ans._suf, ans._sum,
					l._max, r._max, l._suf+r._pre)

	# Return the ans Node
	return ans

# Function for calculating the
# max_sum_subArray using divide and conquer
def getMaxSumSubArray(l, r, ar):

	if l == r: return Node(ar[l])

	mid = (l + r) // 2
	
	# Call method to return left Node:
	left = getMaxSumSubArray(l, mid, ar)
	
	# Call method to return right Node:
	right = getMaxSumSubArray(mid+1, r, ar)
	
	# Return the merged Node:
	return merg(left, right)

# Driver code
if __name__ == "__main__":

	ar = [-2, -5, 6, -2, -3, 1, 5, -6]
	n = len(ar)
	ans = getMaxSumSubArray(0, n-1, ar)
	print("Answer is", ans._max)