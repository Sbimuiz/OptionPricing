from BinaryTree import BinaryTree, Node

print('Code base: https://github.com/Sbimuiz/OptionPricing\n')

print('------ Sheet 9: ------\n')
print('------ Excercise 9.2: ------\n')
#------------------- Sheet 9: Excercise 2 ----------------------

def Sheet9_payoff(node: Node):
    if node.omega == 'S_0':
        return 2/3
    elif node.omega == 'S_0u':
        return 5/3
    elif node.omega == 'S_0d':
        return 1/6
    elif node.omega == 'S_0uu':
        return 0
    elif node.omega == 'S_0ud':
        return 2/3
    elif node.omega == 'S_0dd':
        return 0
    elif node.omega == 'S_0du':
        return 2/3
    elif node.omega == 'S_0uuu':
        return 0
    elif node.omega == 'S_0uud':
        return 0
    elif node.omega == 'S_0udu':
        return 5/3
    elif node.omega == 'S_0udd':
        return 1/6
    elif node.omega == 'S_0ddd':
        return 0
    elif node.omega == 'S_0ddu':
        return 1/6
    elif node.omega == 'S_0dud':
        return 1/6
    elif node.omega == 'S_0duu':
        return 5/3
    else:
        return

TreeSheet9ACC = BinaryTree('ACC', 1, 0, 2, 0.5, 3, Sheet9_payoff)

print('Evolution of S:')
TreeSheet9ACC.printTree(3, 'S')
print('Evolution of Y:')
TreeSheet9ACC.printTree(3, 'Y')

print('9.1.1:')
print('Evolution of U:')
TreeSheet9ACC.printTree(3, 'U')

print('9.1.2:')
TreeSheet9ACC.getTau()
TreeSheet9ACC.getTau_max()
print('According to the lecture all stopping times tau such that tau_0 <= tau <= tau_max are optimal.\n')
