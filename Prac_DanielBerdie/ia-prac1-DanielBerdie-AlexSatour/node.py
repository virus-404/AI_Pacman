class Node:

	def __init__(self, state, parent=None, action=None, cost=0):
		self.state = state
		self.parent = parent
		self.action = action
		self.cost = cost
	def path (self):
		res = []
		while self.action != None:
			res.append(self.action)
			self = self.parent
		res.reverse()
		return res
	def __str__(self):
		return "--Node: {0} --\n Parent: {1}\n Action: {2}\n Cost: {3}".format(self.state, self.parent, self.action, self.cost)

if __name__ == '__main__':
	n1 = Node('state1', None, 'South', 0)
	n2 = Node('state2', n1, 'West', 0)
	n3 = Node('state3', n2, 'North', 0)
	print n3.path()
	print n3
