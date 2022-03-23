print('S -> A\nA -> aB | bC\nB -> b\nC -> g')

def match(val):
    global inp
    global index
    if index >= len(inp):
        return False
    elif inp[index] == val:
        index+=1
        return True
    else:
        return False

def S():
    if A():
        return True
    else:
        return False

def A():
    if match('a'):
        if B():
            return True
        else:
            return False
    elif match('b'):
        if C():
            return True
        else:
            return False
    else:
        return True

def B():
    if match('b'):
        return True
    return False

def C():
    if match('g'):
        return True
    return False

if __name__ == '__main__':
    global inp
    inp = input('Input String: ')
    inp = list(inp)
    global index
    index = 0
    if S():
        if index == len(inp):
            print('String Accepted.')
        else:
            print('String Not Accepted.')
    else:
        print('String Not Accepted.')