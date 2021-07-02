# genetic-sudoku

In this project I deployed a genetic algorithm to solve a suduko puzzles. A 2D array (grid) or an image of a suduko puzzle can be provided to be solved. 
The program makes use of OpenCV and Tessaract for character recognition on images. If the suduko puzzle has all 10 digits, copies will be made of each one 
and used to display the end result as an image or via the terminal as text. Matplotlib is used to display a graph of the error rate over all generations. 

## Dependencies
### Imports
  - pytesseract
  - cv2 
  - numpy 
  - matplotlib.pyplot 
  - time
  - operator
  
## How to use

In main.py fill in the suduko puzzle in the problem_grid array.

```
problem_grid = np.array([
        [4,0,0, 6,0,0, 3,0,0],
        [0,0,2, 8,0,0, 4,0,0],
        [3,0,0, 5,9,0, 0,0,0],

        [0,7,0, 0,0,0, 0,0,2],
        [0,2,0, 0,3,0, 0,1,5],
        [1,0,0, 9,0,0, 0,0,4],

        [0,0,0, 1,7,0, 9,0,0],
        [0,0,0, 0,0,0, 0,2,8],
        [0,9,0, 0,0,0, 0,0,3],
        ])
   ```
   
  A jpg or png file can also be provided.
  
  ```
  img = 'puzzle.png' 
  ```
  The following parameters can be toggled.
   ```
   population_total = 250     
   mutation_rate    = 0.45    
   crossover_rate   = 1       
   ```
