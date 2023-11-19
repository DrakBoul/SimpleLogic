import matplotlib.pyplot as plt
from functions import generate_truth_table


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

