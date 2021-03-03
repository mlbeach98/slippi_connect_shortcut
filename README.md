# slippi_connect_shortcut
Python script to create a gecko code to allow left, right, and down d-pad presses as shortcuts for typing in a player's connect code.

# About the Gecko Code

When going into direct connect on Slippi and pressing Start to enter a player's connect code, the game will appear to freeze. While frozen, press left on the d-pad to prefill opponent 1's connect code, press right to prefill opponent 2's connect code, press down to have a blank connect code entry, or press up to have the last code stay filled in. Opponent 1 and 2's codes will be entered as arguments for the python script that creates the gecko codes.


# About the Python Script

This script creates a gecko code with the above functionality when inputting one or two player's connect codes (functionality with only one code hasn't been tested much, so to be safe it is recommended to just use the same code twice if you only have one you want to enter). 

The script will output the gecko code in one of two ways. If you specify the folder name where Slippi is located, then this code will write the gecko code directly to the "GALE01r2.ini" file in the "./Sys/GameSettings" directory. If a folder name is not specified or the program cannot find this file, it will write the gecko code to a file named "tempCode.txt" in the same directory where the program is run from.



This program and code is a work in progress, so if you encounter any errors or have suggestions for how to make this code/program better feel free to add to it or leave comments.
