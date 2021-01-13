SIG_DIGITS = 2

def validateEq(eq):
    """ Helper function for getEq to validate user input. """
    if 'x' not in eq:
        print("no x")
        return False
    if 'y' not in eq:
        print("no y")
        return False
    if '+' not in eq and '-' not in eq:
        print("no valid operator") 
        return False
    if '=' not in eq:
        print("no =")
        return False
    else:
        return True

def extractCoefficient(x, eq_var='x'):
    """ This is a helper function so users can input x or -x
        instead of 1x, -1x. """
    if x == eq_var:
        return 1
    elif x == '-' + eq_var:
        return -1
    else:
        return x[:-1]

def getEq():
    """ This function prompts the user for a linear equation
        ax + by = z and returns a, b, and z as integers.
        Whitespace between factors is required. """
    input_flag = False
    while not input_flag:
        eq = input("Enter an equation in the form ax + by = z\n")
        if validateEq(eq) == True:
            input_flag = True
        else:
            continue
    return(eq)

def prepareEq(eq):
    """ This function prepares an equation string with the same
        format as getEq() for further computation. """
    info = eq.split(' ')
    x = info[0]
    x = extractCoefficient(x, 'x')
    op = info[1]
    y = info[2]
    y = extractCoefficient(y, 'y')
    if op == '-':
        y *= -1
    z = info[-1]

    return (int(x), int(y), int(z))

def findVal(x1, x2):
    v = float(x2 / x1)
    return v

def findY(y1, y2, z1, z2):
    y_f = (z1 - z2)/(y1 - y2)
    return y_f

def findX(x1, y1, y_f, z1):
    sub_y = y1 * y_f
    z1 = z1 - sub_y
    x_f = z1/x1
    return x_f

def multiplyEq(x, y, z, c):
    x *= c
    y *= c
    z *= c
    return x, y, z

def printEq(x, y, z, eq_num):
    print(str(round(x, SIG_DIGITS)) + "*x + " + str(round(y, SIG_DIGITS)) + "*y = " + str(round(z, SIG_DIGITS)) + "\t\t#" + str(eq_num))
    
def confirmValidPair(x1, y1, z1, x2, y2, z2):
    if (z1 != z2):
        if (x1 == x2) and (y1 == y2):
            return False
        else:
            return True
    else:
        return True

def stylizedElimination(x1, y1, z1, x2, y2, z2):
    printEq(x1, y1, z1, 1)
    printEq(x2, y2, z2, 2)
    if not (confirmValidPair(x1, y1, z1, x2, y2, z2)):
        print(confirmValidPair(x1, y1, z1, x2, y2, z2))
        print("this is not a valid simultaneous system of equations")
        return 1
    print("\n")
    v = findVal(x1, x2)
    if (x2 % x1 == 0):
        print("Multiply both sides of Eq. 1 by " + str(v))
    else:
        print("Multiply both sides of Eq. 1 by " + str(x2) + "/" + str(x1))
    x3, y3, z3 = multiplyEq(x1, y1, z1, v)
    printEq(x3, y3, z3, 3)
    print("\n")

    print("Substract Eq. 3 from Eq. 2")
    y_f = findY(y2, y3, z2, z3)
    print("Find that y = " + str(round(y_f, SIG_DIGITS)))

    print("Substitute y = " + str(round(y_f, SIG_DIGITS)) + " in Eq. 1")
    x_f = findX(x1, y1, y_f, z1)

    if (abs((x1*x_f + y1*y_f) - z1) < SIG_DIGITS):
        print("Answer\t x = " + str(round(x_f, SIG_DIGITS)) + "\t y = " + str(round(y_f, SIG_DIGITS)))
    return 0

# sample code
"""
eq1 = getEq()
eq2= getEq()
x1, y1, z1 = prepareEq(eq1)
x2, y2, z2 = prepareEq(eq2)
print("\n")
stylizedElimination(x1, y1, z1, x2, y2, z2)
"""