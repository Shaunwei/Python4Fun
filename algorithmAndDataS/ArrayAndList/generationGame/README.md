Basic Rules
================
1. If a cell is alive and has either two or three live neighbors, the cell remains
alive in the next generation. The neighbors are the eight cells immediately
surrounding a cell: vertically, horizontally, and diagonally.
2. A living cell that has no live neighbors or a single live neighbor dies from
isolation in the next generation.
3. A living cell that has four or more live neighbors dies from overpopulation in
the next generation.
4. A dead cell with exactly three live neighbors results in a birth and becomes
alive in the next generation. All other dead cells remain dead in the next
generation.