# SimpleLogic
## Introduction
SimpleLogic is a Python 3.12 utility program used to visualize and simplify combinational logic expressions. Given an unsimplified boolean expression SimpleLogic gives the simplified expression in both SOP (Sum of Products) and POS (Product Of Sums) form, along with useful information such as the number of gates and the number of gate inputs for each implementation. Similarly SimpleLogic can generate timing diagrams for boolean expressions, giving the user a useful tool for visualizing and troubleshooting combinational logic circuits. SimpleLogic uses popular python libraries such as tkinter (building GUI), matplotlib (generating timing diagram figures), and Sympify (used for simplification algorithms).

## Dependencies
* Python (3.12.0)
* Matplotlib (3.8.2)
* SymPy (1.12)
## Getting Started
Start by opening command prompt and enter the following commands.

__Clone the repository within your desired directory.__
```
git clone git@github.com:DrakBoul/SimpleLogic.git
```
__Install dependencies.__
```
pip install -r requirements.txt
```
__Execute main.py file.__
```
python main.py
```

## How to Use SimpleLogic
Here we will show an example usage of SimpleLogic, after completing the directions from the "Getting Started" Section above.

__Once you execute the main.py file you should see the starting screen for SimpleLogic.__

[![Screenshot-2023-12-28-152323.png](https://i.postimg.cc/qvdKtXBB/Screenshot-2023-12-28-152323.png)](https://postimg.cc/KRJjwTgC)

__Start by clicking on the "Visualize Expressions" button.__

__Note: If you ever want to quit SimpleLogic, click the "Quit Program" button or click the "X" button in the top right corner of the applications window.__

[![Screenshot-2023-12-28-152349.png](https://i.postimg.cc/L4vRgjtk/Screenshot-2023-12-28-152349.png)](https://postimg.cc/DmWRtJYm)

__You may click the "instructions" button for information about syntax when entering expressions, and what SimpleLogic is capable of handling. If at any point you want to remove the instructions you can click the instructions button again to toggle the instruction text off.__

__Now we can enter a valid boolean expression (see instructions for what is considered a valid boolean expression) into the text box and hit the "Visualize Expression" button. Performing this action for any boolean expression will give the expressions timing diagram.__

[![Screenshot-2023-12-28-152553.png](https://i.postimg.cc/Y9gWrMh9/Screenshot-2023-12-28-152553.png)](https://postimg.cc/S2SsV0LF)

__Next we will look at how we can Simplify boolean expressions using SimpleLogic.__

__Start by navigating back to the main screen of SimpleLogic by clicking the "Go Back" button. Once you are on the main page hit the "Simplify Expressions" button.__

__Now you can enter in a boolean expression you want to simplify and hit the "Simplify Expressions" button to get both the SOP and POS implementation as well as valuble engineering information such as the nummber of gates used for each implementation.__

[![Screenshot-2023-12-28-160545.png](https://i.postimg.cc/44HjvMh1/Screenshot-2023-12-28-160545.png)](https://postimg.cc/NLYNBdDy)

__Note: You may hit the "Clear" button to remove the current timing diagram figure or simplified function information. Although clicking the "Clear" button before entering a new boolean expression to simplify or visualize is not necessary as clicking the "Simplify Expression" or "Visualize Expression" already performs the "Clear" action before displaying new data.__

## Whats Next?
SimpleLogic is a work in progress and it's developers aim to continue to add new features in the near future. Here are some features to look forward to!

* Realization of boolean expressions as logic networks
    * Transistor Level Realization of Logic Network
* Web application version of SimpleLogic
* Sequential logic support

## More About SimpleLogic
SimpleLogic was developed by two Computer Engineering students at the University of Alberta as a submission for the HackED Beta programming contest hosted by the Universitiy's Computer Engineering club. In the contest, SimpleLogic was awarded third place, and was later invited to present the program at democamp 55. SimpleLogic was inspired by a digital logic design course, required as a part of the two developer's degrees. In this course simplifying combinational logic expressions is routine, but can be time consuming, so the process of doing this task was streamlined using python and turned into SimpleLogic.  