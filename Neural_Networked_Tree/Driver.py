# This is a modified version of the online available Monte Carlo Search Tree
# at https://github.com/int8/monte-carlo-tree-search
# This has been changed and commented to increase readablity while also changing some functions
# to fit Exploding Kittens rather than Tic Tac Toe.
from Tree.MonteCarloTreeSearchNode import TwoPlayersGameMonteCarloTreeSearchNode as node
from Tree.MonteCarloTreeSearch import MonteCarloTreeSearch as tree
from Game.Gamestate import ExplodingKittensAbstractGameState as gs
from Models.Training import training
import sys
import os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

# Does a pretty print of the search tree.
def pprint_tree(node, file=None, _prefix="", _last=True):
    print(_prefix, "`- " if _last else "|- ", "P:", node.state.game.currentPlayer, " ",
        node.state.get_obsersavtion_space(), "#'s visited: ", node.n, " #'s wins: ",\
        list(node._results.values())[node.state.game.currentPlayer], " #'s loses: ", list(node._results.values())[node.state.game.currentPlayer - 1], " Action: ", node.action, sep="", file=file)
    _prefix += "   " if _last else "|  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        pprint_tree(child, file, _prefix, _last)


model_fpath = 'C:/Users/flesk/Desktop/qlearning/Git Exploding Kittens/Reinforcement_Learning_Capstone/Neural_Networked_Tree/Models/Exploding_Cat_Model.h5'
data_fpath = 'C:/Users/flesk/Desktop/qlearning/Git Exploding Kittens/Reinforcement_Learning_Capstone/Neural_Networked_Tree/Models/big-data.csv'
t = training(model_fpath)
t.train(data_fpath)


