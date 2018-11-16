class Node:
    def __init__(self, _state, _parent=None, _action=None, _cost=0):
        self.state = _state
        self.parent = _parent
        self.action = _action
        self.cost = _cost

    def path(self):
        pa= []
        curr = self
        while curr.parent != None:
            pa.append(curr.action)
            curr=curr.parent
        return list(reversed(pa))
