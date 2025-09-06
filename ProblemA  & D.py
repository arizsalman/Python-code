flour, sugar = 550, 250

cake = min(flour//100, sugar//50)
remaining_flour = flour - cake*100
remaining_sugar = sugar - cake*50

print(cake)
print(remaining_flour)
print(remaining_sugar)


"""Description:
The baker can bake 5 cakes because flour is the limiting ingredient.
After baking, 50 units of flour and 70 units of sugar remain.
The algorithm ensures resources are used optimally.
Complexity: O(1) — constant time calculations"""

grid = [
    ["L", "E", "A", "R", "N"],
    ["S", "C", "I", "E", "N"],
    ["F", "U", "N", "A", "B"]
]


words = ["LEARN", "FUN"]

directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
]


def find_word(word):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                for dr, dc in directions:
                    rr, cc, k = r, c, 0
                    while (0 <= rr < rows and 0 <= cc < cols and
                           k < len(word) and grid[rr][cc] == word[k]):
                        rr += dr
                        cc += dc
                        k += 1
                    if k == len(word):
                        return True
    return False


for w in words:
    print(w, "found" if find_word(w) else "not found")


"""A Word Search Puzzle is a game where words are hidden inside a 2D grid of letters.
 The words can appear in any direction: horizontally, vertically, or diagonally (forward or backward).
 The goal is to find all the given words inside the grid.
"""
