# Wumpus World with User Input

# Get board size
N = int(input("Enter board size (e.g., 4 for 4x4): "))

# Create empty board
board = [["." for _ in range(N)] for _ in range(N)]

# Get Wumpus position
wx, wy = map(int, input("Enter Wumpus position (row col): ").split())
board[wx][wy] = "W"

# Get Gold position
gx, gy = map(int, input("Enter Gold position (row col): ").split())
board[gx][gy] = "G"

# Get pits count
num_pits = int(input("Enter number of pits: "))
pits = []
for i in range(num_pits):
    px, py = map(int, input(f"Enter Pit {i+1} position (row col): ").split())
    pits.append((px, py))
    board[px][py] = "P"

# Print board
print("\nWumpus World (hidden to agent):")
for row in board:
    print(" ".join(row))

# Agent starts at (0,0)
agent_pos = (0, 0)
print("\nAgent starting at (0,0)")

# Simple agent logic
if agent_pos == (gx, gy):
    print("Agent found the gold at start! 🎉")
else:
    print("Agent explores safely...")
    if (gx, gy) not in pits and (gx, gy) != (wx, wy):
        print("Agent eventually finds the gold at:", (gx, gy))
    else:
        print("Agent cannot safely reach the gold ❌")
