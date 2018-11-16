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

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

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
    gen = {}
    fringe = util.Stack()#Use of stack since it's DFS
    fringe.push(node.Node(problem.getStartState()))
    while True:
        if fringe.isEmpty():
            print 'No solution'
            sys.exit(-1)
        n = fringe.pop()
        gen[n.state] = []
        for s, a, c in problem.getSuccessors(n.state):
            ns = node.Node(s,n,a,c)
            if ns.state not in gen.keys():
                if problem.isGoalState(s):
                    return ns.path()
                fringe.push(ns)
                gen[ns.state] = []

def breadthFirstSearch(problem):
    gen = {}
    fringe = util.Queue()#Use of a queue since it is a BFS
    fringe.push(node.Node(problem.getStartState()))
    while True:
        if fringe.isEmpty():
            print 'No solution'
            sys.exit(-1)
        n = fringe.pop()
        gen[n.state] = []
        for s, a, c in problem.getSuccessors(n.state):
            ns = node.Node(s,n,a,c)
            if ns.state not in gen.keys():
                if problem.isGoalState(s):
                    return ns.path()
                fringe.push(ns)
                gen[ns.state] = []

def uniformCostSearch(problem):
    gen = {}
    fringe = util.PriorityQueue()
    rootNode = node.Node(problem.getStartState())
    fringe.push(rootNode, 0)
    gen[rootNode.state] = [rootNode, 0]
    while True:
        if fringe.isEmpty():
            print 'No solution'
            sys.exit(-1)
        n = fringe.pop()
        if problem.isGoalState(n.state):
            return n.path()
        if gen[n.state][1] == 0: #0 means it hasn't been expanded yet.
            gen[n.state] = [n, 1]
            for s, a, c in problem.getSuccessors(n.state):
                ns = node.Node(s,n,a,n.cost+c)
                if (ns.state not in gen.keys()) or (gen[ns.state][0].cost > ns.cost and gen[ns.state][1] == 0):
                    fringe.push(ns, ns.cost)
                    gen[ns.state] = [ns, 0]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    gen = {}
    fringe = util.PriorityQueue()
    rootNode = node.Node(problem.getStartState())
    fringe.push(rootNode, 0)
    gen[rootNode.state] = [rootNode, 0]
    while True:
        if fringe.isEmpty():
            print 'No solution'
            sys.exit(-1)
        n = fringe.pop()
        if problem.isGoalState(n.state):
            return n.path()
        if gen[n.state][1] == 0: #0 means it hasn't been expanded yet.
            gen[n.state] = [n, 1]
            for s, a, c in problem.getSuccessors(n.state):
                ns = node.Node(s,n,a,n.cost+c+heuristic(s, problem))
                if (ns.state not in gen.keys()) or (gen[ns.state][0].cost > ns.cost and gen[ns.state][1] == 0):
                    fringe.push(ns, ns.cost)
                    gen[ns.state] = [ns, 0]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
