
# Game of Life


This project is an implementation of **Conway's Game of Life** in Python, using the `pygame` library for visual rendering. In this cellular automaton, cells in a grid evolve over iterations according to simple rules, creating complex and often fascinating patterns.

## Rules of the Game

In the Game of Life, each cell has two states: alive or dead. The evolution of cells over each iteration is governed by the following rules:
1. A living cell with fewer than 2 living neighbors dies (underpopulation).
2. A living cell with 2 or 3 living neighbors survives.
3. A living cell with more than 3 living neighbors dies (overpopulation).
4. A dead cell with exactly 3 living neighbors becomes alive (reproduction).

## Features

- **Interactive Setup**: Select the initial alive cells by clicking on them. Dead cells will toggle to alive (and vice versa) on each click.
- **Simulation Start**: Press the spacebar to begin the simulation based on the selected initial configuration.
- **Iteration Counter**: Tracks and displays the number of iterations in the simulation.

## Requirements

- Python 3.x
- `pygame` library
- `numpy` library
- `time` library

To install library, run:
```bash
pip install pygame
pip install numpy
```

## Usage

1. **Run the Game**:
   ```bash
   python GameOfLife.py
   ```

2. **Select Cells**:
   - Click on any cell to toggle it between alive (white) and dead (black).
   - Configure the grid as desired before starting the simulation.

3. **Start Simulation**:
   - Press the **spacebar** to start the Game of Life simulation.
   - Observe the evolution of the cells over each iteration.

4. **Exit**:
   - Close the game window to exit the program.

## Code Overview

The implementation is divided into these main sections:
- **Grid Initialization**: Sets up an empty grid.
- **Cell Selection**: Allows the user to click cells to set the initial configuration.
- **Game Rules**: Applies the Game of Life rules at each iteration.
- **Display**: Uses `pygame` to render cells and display iteration counts.

## Example

After running `game_of_life.py`, a window will appear where you can click to select initial live cells. Press the **spacebar** to start the evolution, and watch the cells change over each generation according to Conway’s rules.
