# ------ Calculate binomial model with simple python implementation ------
#
# 1. Define option payoff (see also Examples below):
#    - Define function which takes as argument an object of class Node
#    - Attribute S in class Node stores value of stock
#    - Use function getPrevStockPrices() if your payoff depends on previous prices
#
# 2. Define Binary Tree:
#    - Initialize tree as follows: Tree = BinaryTree('ECC' or 'ACC', S_zero, r, u, d, T, your_payoff)
#
# 3. Methods of class Tree:
#    - Get price of option at a specific node (e.g. first up then down) in the tree: Tree.getPrice('ud') (for price at t = 0 use empty string '')
#    - Get values of alpha and beta at a specific node (e.g. first up then down) in the tree: Tree.getAlphaBeta('ud')
#    - !! getAlphaBeta() does as of yet not give the correct values in case of an ACC, i.e. it computes values only without excess wealth !!
#    - Compute Tau for tree: Tree.getTau()
#    - Print values of Tree (S, Y, U) up to a specific depth: Tree.printTree(depth, 'S' or 'Y' or 'U')
#    - !! printTree is constraint by width of screen, causes ugly prints if depth or values are too big!!
#

from BinaryTree import BinaryTree, Node


print('------ Sheet 7: ------\n')
#------------------- Sheet 7: Example at beginning of excecise Sheet (call option, strike price = 80) ----------------------

def call_payoff(node: Node):
    return max(0, node.S - 80)

print('------ Example: ------\n')
print('ACC:')
TreeCallOptionACC = BinaryTree('ACC', 80, 0, 1.5, 0.5, 3, call_payoff)
TreeCallOptionACC.getPrice('')
TreeCallOptionACC.getTau()
TreeCallOptionACC.printTree(3, 'Y')
TreeCallOptionACC.printTree(3, 'U')
print('ECC:')
TreeCallOptionECC = BinaryTree('ECC', 80, 0, 1.5, 0.5, 3, call_payoff)
TreeCallOptionECC.getPrice('')

#------------------- Sheet 7: Excercise 1 ----------------------
def Exercise1_payoff(node: Node):
    if node.S > 100:
        return node.S - 100
    elif 60 <= node.S <= 100:
        return 0
    else:
        return 60 - node.S

print('------ Excercise 7.1: ------\n')
TreeExcercise1ACC = BinaryTree('ACC', 80, 0, 1.5, 0.5, 3, Exercise1_payoff)

print('7.1.1:')
TreeExcercise1ACC.getPrice('')

print('7.1.2:')
TreeExcercise1ACC.getTau()

print('7.1.3:')
TreeExcercise1ECC = BinaryTree('ECC', 80, 0, 1.5, 0.5, 3, Exercise1_payoff)
TreeExcercise1ECC.getPrice('')

#------------------- Sheet 7: Excercise 2 ----------------------
def Exercise2_payoff(node: Node):
    stockPrices = node.getPrevStockPrices()
    return max(stockPrices)

print('------ Excercise 7.2: ------\n')
TreeExcercise2ACC = BinaryTree('ACC', 80, 0, 1.5, 0.5, 3, Exercise2_payoff)

print('7.2.1:')
TreeExcercise2ACC.getPrice('')

print('7.2.2:')
TreeExcercise2ACC.getTau()

print('7.2.3:')
TreeExcercise2ECC = BinaryTree('ECC', 80, 0, 1.5, 0.5, 3, Exercise2_payoff)
TreeExcercise2ECC.getPrice('')


print('------ Sheet 6: ------\n')
#------------------- Sheet 6: Excercise 1 ----------------------
def call_payoff(node: Node):
    return max(0, node.S - 1)

print('------ Excercise 6.1: ------\n')
TreeCallOption = BinaryTree('ECC', 1, 0, 2, 0.5, 3, call_payoff)

print('6.1.2:')
TreeCallOption.getPrice('')
TreeCallOption.getPrice('u')
TreeCallOption.getPrice('d')
TreeCallOption.getPrice('ud')
TreeCallOption.getPrice('uu')
TreeCallOption.getPrice('dd')
TreeCallOption.getPrice('uuu')
TreeCallOption.getPrice('uud')
TreeCallOption.getPrice('udd')
TreeCallOption.getPrice('ddd')

print('6.1.3:')
TreeCallOption.getAlphaBeta('')
TreeCallOption.getAlphaBeta('u')
TreeCallOption.getAlphaBeta('d')
TreeCallOption.getAlphaBeta('uu')
TreeCallOption.getAlphaBeta('ud')
TreeCallOption.getAlphaBeta('dd')

#------------------- Sheet 6: Excercise 2 ----------------------
print('------ Excercise 6.2: ------\n')

#------------------- ECC: lookback option ------------------------------------
def lookback_payoff(node: Node):
    stockPrices = node.getPrevStockPrices()
    m = 0
    for S in stockPrices:
        m = max(m, S - node.S)
    return m

print('6.2.1:')
TreeLoockback = BinaryTree('ECC', 4, 0.25, 2, 0.5, 2, lookback_payoff)

TreeLoockback.getPrice('')
TreeLoockback.getPrice('u')
TreeLoockback.getPrice('d')
TreeLoockback.getPrice('uu')
TreeLoockback.getPrice('dd')
TreeLoockback.getPrice('ud')
TreeLoockback.getPrice('du')

TreeLoockback.getAlphaBeta('')
TreeLoockback.getAlphaBeta('u')
TreeLoockback.getAlphaBeta('d')

#------------------- ECC: asian option ------------------------------------
def asian_payoff(node: Node):
    stockPrices = node.getPrevStockPrices()
    return max(sum(stockPrices) / 3 - node.S, 0)

print('6.2.2:')
TreeAsian = BinaryTree('ECC', 4, 0.25, 2, 0.5, 2, asian_payoff)

TreeAsian.getPrice('')
TreeAsian.getPrice('u')
TreeAsian.getPrice('d')
TreeAsian.getPrice('uu')
TreeAsian.getPrice('dd')
TreeAsian.getPrice('ud')
TreeAsian.getPrice('du')

TreeAsian.getAlphaBeta('')
TreeAsian.getAlphaBeta('u')
TreeAsian.getAlphaBeta('d')






