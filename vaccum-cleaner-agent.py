import random

class SimpleVacuumCleanerAgent:
    def __init__(self, grid):
        self.grid = grid  # 2D grid representing the environment
        self.position = self.find_start_position()  # Initial position of the vacuum cleaner

    def find_start_position(self):
        # Find the starting position of the vacuum cleaner (the first '0' in the grid)
        for i, row in enumerate(self.grid):
            for j, value in enumerate(row):
                if value == 0:  # Assuming 0 represents an empty space
                    return (i, j)
        return None

    def clean(self):
        # Clean the current position
        if self.grid[self.position[0]][self.position[1]] == 1:  # 1 represents dirty
            self.grid[self.position[0]][self.position[1]] = 0  # Set to clean (0)
            print(f"Cleaned position: {self.position}")

    def move(self):
        # Define possible moves (up, down, left, right)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(moves)  # Shuffle to add randomness in movement

        for move in moves:
            new_position = (self.position[0] + move[0], self.position[1] + move[1])
            if self.is_within_bounds(new_position):
                self.position = new_position
                print(f"Moved to position: {self.position}")
                break

    def is_within_bounds(self, position):
        # Check if the position is within the bounds of the grid
        return 0 <= position[0] < len(self.grid) and 0 <= position[1] < len(self.grid[0])

    def run(self):
        # Main loop for the vacuum cleaner agent
        while True:
            self.clean()
            self.move()

            if not any(1 in row for row in self.grid):  # Check if there's any dirty spot left
                print("All positions cleaned!")
                break

# Example grid (0 = empty, 1 = dirty)
grid = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

# Create vacuum cleaner agent and run it
vacuum = SimpleVacuumCleanerAgent(grid)
vacuum.run()
