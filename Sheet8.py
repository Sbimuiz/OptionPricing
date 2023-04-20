from BinaryTree import BinaryTree, Node

print('------ Sheet 8: ------\n')
print('------ Excercise 8.1: ------\n')
#------------------- Sheet 8: Excercise 1 ----------------------

def Sheet8_payoff(node: Node):
    return min(max(node.S, 2), 5)

TreeSheet8ACC = BinaryTree('ACC', 4, 0.5, 2, 0.5, 2, Sheet8_payoff)
print('Evolution of S:')
TreeSheet8ACC.printTree(2, 'S')
print('Evolution of Y:')
TreeSheet8ACC.printTree(2, 'Y')
print('Evolution of V (= 1/(1 + r) * E[U_t|F_t-1]):')
TreeSheet8ACC.printTree(2, 'V')

print('8.1.1:')
print('Evolution of U:')
TreeSheet8ACC.printTree(2, 'U')

print('8.1.2:')
print('Alpha and beta without excess wealth:')
TreeSheet8ACC.getAlphaBeta('')
TreeSheet8ACC.getAlphaBeta('u')
TreeSheet8ACC.getAlphaBeta('d')

print('Alpha and beta with excess wealth:')
TreeSheet8ACC.getAlphaBetaSuperHedging('',   0)
TreeSheet8ACC.getAlphaBetaSuperHedging('u',  0)
TreeSheet8ACC.getAlphaBetaSuperHedging('d',  0)

print('8.1.3:')
print('I assume it is meant to calculate the ECC price of the option?')
TreeSheet8ECC = BinaryTree('ECC', 4, 0.5, 2, 0.5, 2, Sheet8_payoff)
TreeSheet8ECC.getPrice('')

print('8.1.4:')
print('If the price from 8.1.3 were the market price, one could buy the option at this price and excercise it at t=0 with a certain gain.')
