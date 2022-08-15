### Description
Wavefunction Collapse Map is a simple, pseudo-random map generator, created using Python with NumPy and Pillow. Its purpose is to create a 2D map made up of tiles, done on a 24 x 24 grid, which is rendered using Pillow.

### How to Run
Run wavefunction.py and navigate to output.png to see the generated image.

### Rules
The map generator was constructed as to generate a result which adheres to a set of constraints. Those
rules are as follows:
* Flower tiles may only occur on the edges of the map and never next to a water tile.
* Rock tiles may occur anywhere except for directly next to each other, and always have a weightage of 20%.
* Water tiles may only occur next to a coast tile, a rock tile, or another water tile.
* Coast tiles may occur anywhere.
* Land tiles cannot touch water tiles.
