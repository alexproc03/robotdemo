# robotdemo
This repository contains the TextX and Python file defining a simple Robot interpreted language. diagonal.rbt, enderman.rbt, and noscope.rbt are my sample programs that incorporate my new features. Sample program output is in output.pdf
## Features added by me
### constraint: initial position must be 0, 0
this is enforced by a simple if statement in the implementation python file
### upleft, upright, downleft, downright
moves n in both the x and y directions
### 360
rotates 360 * n degrees. No actual movement on the grid
### Special feature: random
moves randomly in both directions, with max movement on each axis equivalent to n
