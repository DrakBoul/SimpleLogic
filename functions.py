from sympy.logic import POSform, SOPform
from itertools import product

def evaluate_expression(expression, variables, assignment):
    """Evaluate the boolean expression for a given variable assignment."""
    substitution = dict(zip(variables, assignment))
    return eval(expression, {}, substitution)

#might need to keep this function. needs more testing
# def evaluate_expression(expression, variables, assignment):
#     """Evaluate the boolean expression for a given variable assignment."""
#     substitution = dict(zip(variables, assignment))

#     return eval(expression, substitution)

def generate_minterms(expression, variables):
    """Generate all minterms for a boolean expression."""
    num_variables = len(variables)
    minterms = []

    for i in range(2**num_variables):
        binary_str = format(i, '0' + str(num_variables) + 'b')
        assignments = [int(binary_str[j]) for j in range(len(binary_str))]   
        if evaluate_expression(expression, variables, assignments):
            minterms.append(i)

    return minterms 


def convert_to_pos(content):
    """Converts to POS using built in method from sympy POSform"""
    expr_str, var_str = content.split(',')
    var_list = var_str.split()
    minterms = generate_minterms(expr_str, var_list)
    pos_form = POSform(var_list, minterms)
    
    return pos_form

def convert_to_sop(content):
    """Converts to POS using built in method from sympy POSform"""
    expr_str, var_str = content.split(',')
    var_list = var_str.split()
    minterms = generate_minterms(expr_str, var_list)
    pos_form = SOPform(var_list, minterms)

    return pos_form

def generate_truth_table(expression, variables):
    """Generate the truth table for a boolean expression."""
    num_variables = len(variables)
    truth_table = []

    for assignment in product([0, 1], repeat=num_variables):
            row = list(assignment)
            row.append(str(evaluate_expression(expression, variables, assignment)))
            truth_table.append(row)
    return truth_table

# variables = ["A", "B", "C"]
# expression = "~A & B | C & B"
# print(generate_truth_table(expression, variables))
# print(generate_minterms(expression, variables))