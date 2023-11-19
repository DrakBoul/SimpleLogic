import matplotlib.pyplot as plt
import numpy as np
from functions import generate_minterms, evaluate_expression, generate_truth_table




# def plot_timing_diagram(variables, expression):
#     """Plot the timing diagram for a boolean expression."""

#     truth_table = generate_truth_table(expression, variables)
#     num_variables = len(variables)
#     num_rows = 2**num_variables

    # plt.figure(figsize=(10, 6))

    # for i in range(num_variables):
    #     plt.subplot(num_variables + 1, 1, i + 1)
    #     plt.step(range(num_rows), [row[i] for row in truth_table], where='post', label=f'Input {i + 1}')
    #     plt.yticks([0, 1], [f'{variables[i]} = {val}' for val in [0, 1]])

    # plt.subplot(num_variables + 1, 1, num_variables + 1)
    # plt.step(range(num_rows), [row[num_variables] for row in truth_table], 'r', where='post', label='Output')
    # plt.yticks([0, 1], [f'Output = {val}' for val in [0, 1]])

    # for i in range(num_variables + 1):
    #     plt.subplot(num_variables + 1, 1, i + 1)
    #     plt.grid(True, axis='x', linestyle='--', linewidth=0.5)

    # plt.ylim([-0.1, 1.1])
    # plt.gca().axis('off')
    # plt.legend()
    # # plt.show()

def plot_timing_diagram(ax, variables, expression):
    """Plot the timing diagram for a boolean expression on the given Axes instance."""

    truth_table = generate_truth_table(expression, variables)
    num_variables = len(variables)
    num_rows = 2**num_variables

    for i in range(num_variables):
        ax[i].step(range(num_rows), [row[i] for row in truth_table], where='post', label=f'Input {i + 1}')
        ax[i].set_yticks([0, 1])
        ax[i].set_yticklabels([f'{variables[i]} = {val}' for val in [0, 1]])

    ax[num_variables].step(range(num_rows), [row[num_variables] for row in truth_table], 'r', where='post', label='Output')
    ax[num_variables].set_yticks([0, 1])
    ax[num_variables].set_yticklabels([f'Output = {val}' for val in [0, 1]])

    for i in range(num_variables + 1):
        ax[i].grid(True, axis='x', linestyle='--', linewidth=0.5)

    ax[num_variables].set_ylim([-0.1, 1.1])
    ax[num_variables].axis('off')
    ax[num_variables].legend()

# Usage example:

# Test case 1
variables_1 = ["A", "B", "C"]
expression_1 = "~A & B | C & B"

# Test case 2
variables_2 = ["X", "Y"]
expression_2 = "~X | Y"

# Test case 3
variables_3 = ["P", "Q", "R"]
expression_3 = "(P & Q) | (~R)"

# Test case 4
variables_4 = ["D", "E", "F", "G"]
expression_4 = "D | (E & ~F) | (G & F)"

# Test case 5
variables_5 = ["W", "X", "Y", "Z"]
expression_5 = "~W | (X & Y) | (Z & ~Y)"

# Test case 6
variables_6 = ["A", "B", "C", "D"]
expression_6 = "(A & B) | (~C & D)"

# Test case 7
variables_7 = ["X", "Y", "Z"]
expression_7 = "(X | Y) & ~Z"

# Test case 8
variables_8 = ["P", "Q"]
expression_8 = "P & Q"

# Test case 9
variables_9 = ["A", "B", "C", "D", "E"]
expression_9 = "(A & B & C) | (~D & E)"

# Test case 10
variables_10 = ["P", "Q", "R", "S"]
expression_10 = "(P & Q) | (R & ~S)"

# plot_timing_diagram(variables_1, expression_1)
# plot_timing_diagram(variables_2, expression_2)
# plot_timing_diagram(variables_3, expression_3)
# plot_timing_diagram(variables_4, expression_4)
# plot_timing_diagram(variables_5, expression_5)
# plot_timing_diagram(variables_6, expression_6)
# plot_timing_diagram(variables_7, expression_7)
# plot_timing_diagram(variables_8, expression_8)
# plot_timing_diagram(variables_9, expression_9)
# plot_timing_diagram(variables_10, expression_10)