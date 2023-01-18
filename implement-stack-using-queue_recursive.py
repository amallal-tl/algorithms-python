from _collections import deque

# Stack Class that acts as a queue


class Stack:
	def __init__(self):
		self.q = deque()

	# Push operation
	def push(self, data, c):

		# Push the current element
		self.q.append(data)

		# Return if size becomes 0
		if c <= 0:
			return

		# Store and then pop the current front
		x = self.q.popleft()

		# Decrement size by 1 in every recursion
		c = c-1
		self.push(x, c)

	# Removes the top element
	def pop(self):
		if (not self.q):
			print("No elements")
		else:
			self.q.popleft()

	# Returns top of stack
	def top(self):
		if (not self.q):
			return
		return self.q[0]

	def size(self):
		return len(self.q)


if __name__ == '__main__':
	st = Stack()
	st.push(1, st.size())
	st.push(2, st.size())
	st.push(3, st.size())
	print("current size: ", st.size())
	print(st.top())
	st.pop()
	print(st.top())
	st.pop()
	print(st.top())
	print("current size: ", st.size())