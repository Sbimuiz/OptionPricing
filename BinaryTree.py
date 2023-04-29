class Node:

    def __init__(self, isECC, r, u, d, T, optionPayOff):
        self.isECC = isECC
        self.r = r
        self.u = u 
        self.d = d
        self.T = T
        self.time = 0
        self.prevNode = None
        self.nextNodeUp = None
        self.nextNodeDown = None
        self.S = 0
        self.Y = 0
        self.V = 0
        self.U = 0
        self.alpha = 0
        self.beta = 0
        self.delta = 0
        self.Tau = ''
        self.Tau_max = ''
        self.optionPayOff = optionPayOff
        self.omega = 'S_0'
        self.stringsForPrint = dict()

    def createNextNodes(self):
        if self.time < self.T:

            self.nextNodeUp = Node(self.isECC, self.r, self.u, self.d, self.T, self.optionPayOff)
            self.nextNodeUp.prevNode = self
            self.nextNodeUp.time = self.time+1
            self.nextNodeUp.S = self.S * self.u
            self.nextNodeUp.omega = ''.join([self.omega, 'u'])
            self.nextNodeUp.createNextNodes()

            self.nextNodeDown = Node(self.isECC, self.r, self.u, self.d, self.T, self.optionPayOff)
            self.nextNodeDown.prevNode = self
            self.nextNodeDown.time = self.time+1
            self.nextNodeDown.S = self.S * self.d
            self.nextNodeDown.omega = ''.join([self.omega, 'd'])
            self.nextNodeDown.createNextNodes()

        self.computeNode()

    def computeNode(self):
        # compute payoff
        self.Y = self.optionPayOff(self)
        #compute U, alpha and beta
        if self.time == self.T:
            self.V = self.Y
            self.U = self.Y
        else:
            p_star = (1 + self.r - self.d) / (self.u - self.d)

            self.V = 1 / (1 + self.r) * (p_star * self.nextNodeUp.U + (1 - p_star) * self.nextNodeDown.U)
            if self.isECC == True:
                self.U = self.V
            else:
                self.U = max(self.Y, self.V)
                self.delta = pow((1 + self.r), -self.time) * (self.U - self.V)

            self.alpha = (self.nextNodeUp.U - self.nextNodeDown.U) / ((self.u - self.d) * self.S)
            self.beta = pow((1 + self.r), -(self.time + 1)) * (self.u * self.nextNodeDown.U - self.d *  self.nextNodeUp.U) / (self.u - self.d)

        self.stringsForPrint['S'] = f' S={self.S:.2f} '
        self.stringsForPrint['Y'] = f' Y={self.Y:.2f} '
        self.stringsForPrint['V'] = f' V={self.V:.2f} '
        self.stringsForPrint['U'] = f' U={self.U:.2f} '

    def computeTau(self):
        #compute tau*_o
        if self.time > 0 and self.prevNode.Tau != '':
            self.Tau = self.prevNode.Tau
        elif round(self.Y, 10) == round(self.U, 10):
            self.Tau = self.time
        
    def computeTau_max(self):
        #compute tau_max
        if self.time < self.T and self.delta != 0:
            self.Tau_max = self.time
        elif self.time > 0 and self.time < self.T:
            self.Tau_max = self.prevNode.Tau_max
        elif self.time == self.T:
            if self.prevNode.Tau_max == '':
                self.Tau_max = self.time
            else:
                self.Tau_max = self.prevNode.Tau_max

    def getPrevStockPrices(self):
        if self.time == 0:
            return [self.S]
        else:
            l = self.prevNode.getPrevStockPrices()
            l.append(self.S)
            return l

    def getPrice(self, omega):
        if len(omega) == self.time:
            tmp = ''.join(omega)
            print(f'Fair_Price( S_0{tmp} ) = {self.U:.3f}', '\n')
        else:
            if omega[self.time] == 'u':
                self.nextNodeUp.getPrice(omega)
            elif omega[self.time] == 'd':
                self.nextNodeDown.getPrice(omega)
            else:
                print('Not a valid input\n')

    def getAlphaBeta(self, omega):
        if len(omega) == self.time:
            print(f'{self.omega} : alpha = {self.alpha:.3f}, beta = {self.beta:.3f}', '\n')
        else:
            if omega[self.time] == 'u':
                self.nextNodeUp.getAlphaBeta(omega)
            elif omega[self.time] == 'd':
                self.nextNodeDown.getAlphaBeta(omega)
            else:
                print('Not a valid input')

    def getAlphaBetaSuperHedging(self, omega, time, sumDeltas):
        if self.time >= time:
            sumDeltas += self.delta
        if len(omega) == self.time:
            print(f'{self.omega} : alpha = {self.alpha:.3f}, beta = {self.beta + sumDeltas:.3f}', '\n')
        else:
            if omega[self.time] == 'u':
                self.nextNodeUp.getAlphaBetaSuperHedging(omega, time, sumDeltas)
            elif omega[self.time] == 'd':
                self.nextNodeDown.getAlphaBetaSuperHedging(omega, time, sumDeltas)
            else:
                print('Not a valid input')

    def getTau(self):
        self.computeTau()
        #print tau*_max
        if self.time == self.T:
            print('tau_0(',self.omega,')', ' = ', self.Tau)
        elif self.time < self.T:
            self.nextNodeUp.getTau()
            self.nextNodeDown.getTau()

    def getTau_max(self):
        self.computeTau_max()
        #print tau_max
        if self.time == self.T:
            print('tau_max(',self.omega,')', ' = ', self.Tau_max)
        elif self.time < self.T:
            self.nextNodeUp.getTau_max()
            self.nextNodeDown.getTau_max()

    def getMaxLengthString(self, strType):
        maxlen = len(self.stringsForPrint[strType])
        if self.time == self.T:
            return maxlen
        maxup = self.nextNodeUp.getMaxLengthString(strType)
        maxdown = self.nextNodeDown.getMaxLengthString(strType)
        return max(maxlen, maxup, maxdown)

    def printNode(self, depth, leaves, prevPosition, path, tree, maxlen, strType):
        if self.time <= depth:
            if path == '':
                position = leaves - 1
            if path == 'u':
                position = prevPosition + (leaves / pow(2, self.time)) 
            if path == 'd':
                position = prevPosition - (leaves / pow(2, self.time))

            diff =  maxlen - len(self.stringsForPrint[strType])
            tree[self.time][int(position)] = self.stringsForPrint[strType] + diff * ' '

            if self.time < self.T:
                self.nextNodeDown.printNode(depth, leaves, position, 'd', tree, maxlen, strType)
                self.nextNodeUp.printNode(depth, leaves, position, 'u', tree, maxlen, strType)

class BinaryTree:

    def __init__(self, optionType, S_zero, r, u, d, T, optionpayOff):
        if optionType == 'ECC':
            self.root = Node(True, r, u, d, T, optionpayOff)
        elif optionType == 'ACC':
            self.root = Node(False, r, u, d, T, optionpayOff)
        else:
            print('Only Option Typ ECC or ACC allowed. Use ECC as default.')
            self.root = Node(True, r, u, d, T, optionpayOff)
        self.root.S = S_zero
        self.root.createNextNodes()
        self.T = T

    def getPrice(self, omega):
        if len(list(omega)) > self.T:
            return
        else:
            self.root.getPrice(list(omega))

    def getAlphaBeta(self, omega):
        if len(list(omega)) >= self.T:
            return
        else:
            self.root.getAlphaBeta(list(omega))

    def getAlphaBetaSuperHedging(self, omega, time):
        if len(list(omega)) < time:
            print(f'You need to choose a node at a time point bigger than {time}')
            return
        elif len(list(omega)) >= self.T:
            return
        else:
            self.root.getAlphaBetaSuperHedging(list(omega), time, 0)

    def getTau(self):
        print('tau_0( omega ):')
        self.root.getTau()
        print('\n')

    def getTau_max(self):
        print('tau_max( omega ):')
        self.root.getTau_max()
        print('\n')

    def printTree(self, depth, strType):
        tree = dict()
        maxlen = self.root.getMaxLengthString(strType)

        for i in range(0, depth + 1):
            tree[i] = list()
            for j in range(0, pow(2, depth + 1)):
                tmp = ''.join('_' * int(maxlen))
                tree[i].append(tmp)

        self.root.printNode(depth, pow(2, depth), 0, '', tree, maxlen, strType)

        for i in range(0, depth + 1):
            print(''.join(tree[i]))
        print('\n')
        





