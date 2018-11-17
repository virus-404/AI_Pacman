class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
		self.state = state
		self.parent = parent
		self.action = action
		self.cost = cost

    def path(self):
        pa= []
        while self.parent != None:
            pa.append(self.action)
            self=self.parent
        return list(reversed(pa))

	def __str__(self):
return "--Node: {0} --\n Parent: {1}\n Action: {2}\n Cost: {3}".format(self.state, self.parent, self.action, self.cost)
