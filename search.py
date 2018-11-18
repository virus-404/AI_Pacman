# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sys
import node

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def getGoalState(self):
        """
        Returns the goal state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    #def setGoalState(self,state):

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    start = node.Node(problem.getStartState())
    fringe = util.Stack()
    fringe.push(start)

    if problem.isGoalState(start):
        return start.path()

    expanded  = set()

    while True:
        if fringe.isEmpty():
            return self.fail('Solution not found')
        n=fringe.pop()
        expanded.add(n.state)
        for succ, action, cost in problem.getSuccessors(n.state):
            ns=node.Node(succ,n,action,cost)
            if ns.state not in expanded:
                if problem.isGoalState(succ):
                    return ns.path()
                fringe.push(ns)
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    start = node.Node(problem.getStartState())
    fringe = util.Queue()
    fringe.push(start)

    if problem.isGoalState(start):
        return start.path()

    expanded  = set()

    while True:
        if fringe.isEmpty():
            return self.fail('Solution not found')
        n=fringe.pop()
        expanded.add(n.state)
        for succ, action, cost in problem.getSuccessors(n.state):
            ns=node.Node(succ,n,action,cost)
            if ns.state not in expanded:
                if problem.isGoalState(succ):
                    return ns.path()
                fringe.push(ns)
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    start = node.Node(problem.getStartState())
    fringe=util.PriorityQueue()
    fringe.push(start,0)

    expanded = {}

    while True:
        if fringe.isEmpty():
            return self.fail('Solution not found')
        n = fringe.pop()
        if problem.isGoalState(n.state):
            return n.path()
        expanded[n.state] = n
        for succ, action, cost in problem.getSuccessors(n.state):
            ns=node.Node(succ,n,action,cost)
            if ns.state not in expanded.keys():
                fringe.push(ns, ns.cost)
            elif ns.state in expanded.keys() and expanded[ns.state].cost > ns.cost:
                fringe.update(ns,ns.cost)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start = node.Node(problem.getStartState())
    fringe=util.PriorityQueue()
    fringe.push(start,0)

    expanded = {}

    while True:
        if fringe.isEmpty():
            return self.fail('Solution not found')
        n = fringe.pop()
        if problem.isGoalState(n.state):
            return n.path()
        expanded[n.state] = n
        for succ, action, cost in problem.getSuccessors(n.state):
            ns=node.Node(succ,n,action,cost)
            if ns.state not in expanded.keys():
                fringe.push(ns,ns.cost + heuristic(succ, problem))
            elif ns.state in expanded.keys() and expanded[ns.state].cost > ns.cost:
                fringe.update(ns, ns.cost)
    util.raiseNotDefined()

def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    """It makes a locally-optimal choice in the hope that this choice will lead to a globally-optimal solution. """
    start = node.Node(problem.getStartState())
    fringe=util.PriorityQueue()
    fringe.push(start,0)

    expanded = {}

    while True:
        if fringe.isEmpty():
            return self.fail('Solution not found')
        n = fringe.pop()
        if problem.isGoalState(n.state):
            return n.path()
        expanded[n.state] = n
        for succ, action, cost in problem.getSuccessors(n.state):
            ns=node.Node(succ,n,action,cost)
            if ns.state not in expanded.keys() and heuristic(succ, problem) < heuristic(n.state, problem):
                fringe.push(ns, 0)
                fringe.push(n, 1)
            elif ns.state not in expanded.keys():
                fringe.push(ns, heuristic(succ, problem))
    util.raiseNotDefined()

def bidirectionalSearch(problem):
    start = node.Node(problem.getStartState())
    end = node.Node(problem.getGoalState())

    fringe_start = util.Queue()
    fringe_start.push(start)
    fringe_end = util.Queue()
    fringe_end.push(end)

    if start == end:
        return start.path()

    expanded_start  = {}
    expanded_end  = {}

    while True:
        if fringe_start.isEmpty() or fringe_end.isEmpty():
            return self.fail('Solution not found')

        n_start=fringe_start.pop()
        expanded_start[n_start.state] = n_start
        for succ, action, cost in problem.getSuccessors(n_start.state):
            ns=node.Node(succ,n_start,action,cost)
            if ns.state not in expanded_start.keys():
                fringe_start.push(ns)
                if ns.state in expanded_end.keys():
                    tmp = ns.path()
                    end = expanded_end[ns.state].parent
                    tmp.append(reversed(end.path()))
                    return tmp
        n_end=fringe_end.pop()
        expanded_end[n_end.state] = n_end
        for succ, action, cost in problem.getSuccessors(n_end.state):
            ns=node.Node(succ,n_end,action,cost)
            if ns.state not in expanded_end.keys():
                fringe_end.push(ns)
                if ns.state in expanded_start.keys():
                    tmp = ns.path()
                    start = expanded_start[ns.state].parent
                    tmp.append(reversed(start.path()))
                    return tmp
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
bds = bidirectionalSearch
bfsh = greedyBestFirstSearch
