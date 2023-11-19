import sympy as sp

a, b, c = sp.symbols("a, b, c")


truth_table = {
    (0,0,0,0):None
    (0,0,0,1):None
    (0,0,1,0):None
    (0,0,1,1):None
    (0,1,0,0):None
    (0,1,0,1):None
    (0,1,1,0):None
    (0,1,1,1):None
    (1,0,0,0):None
    (1,0,0,1):None
    (1,0,1,0):None
    (1,0,1,1):None
    (1,1,0,0):None
    (1,1,0,1):None
    (1,1,1,0):None
    (1,1,1,1):None
}
#make the letter in the expression equal to whatever the value is in that tuple
for key in truth_table:
    A,B,C,D, = key
    result = boolean_function(A,B,C,D)#whatever our simplified function is
    truth_table[key]=result

#use liams or my timing diagram along with this to present the truth table and a timing diagram to display