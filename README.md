# OptionPricing
------ Calculate binomial model with simple python implementation ------

1. Define option payoff (see also Examples):
   - Define function which takes as argument an object of class Node
   - Attribute S in class Node stores value of stock
   - Use function getPrevStockPrices() if your payoff depends on previous prices

2. Define Binary Tree:
   - Initialize tree as follows: Tree = BinaryTree('ECC' or 'ACC', S_zero, r, u, d, T, your_payoff)

3. Methods of class Tree:
   - Get price of option at a specific node (e.g. first up then down) in the tree: Tree.getPrice('ud') (for price at t = 0 use empty string '')
   - Get values of alpha and beta at a specific node (e.g. first up then down) in the tree: Tree.getAlphaBeta('ud')
   - Compute Tau for tree: Tree.getTau()
   - Print values of Tree (S, Y, V, U) up to a specific depth: Tree.printTree(depth, 'S' or 'Y' or 'V' or 'U')
   - !! printTree is constraint by width of screen, causes ugly prints if depth or values are too big!!
