
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


# A Word Search Puzzle is a game where words are hidden inside a 2D grid of letters.
#  The words can appear in any direction: horizontally, vertically, or diagonally (forward or backward).
#  The goal is to find all the given words inside the grid.

def func(num_final):
    seem = set()
    for i in num_final:
        if i in seem:
            return True
        else:
            seem.add(i)
    return False


num_final = []
while True:
    nums = input("Enter your number & Exit Type 'done':")
    if nums.strip().lower() == "done":
        break
    try:
        value = int(nums)
        print(f'Your entered {value}')
    except ValueError:
        print("Please Enter in valiad Value")

    num_final.append(value)
    print(f'Your Value {num_final}')

    if func(num_final):
        print(f'Duplicate Found ')
    else:
        print(f' No Duplicate')
