# Snake_Game

## Description
A classic Snake game implemented in Python using the Turtle graphics library. Control the snake to eat food and grow longer, but avoid running into walls or colliding with its own body.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Shriram-11/Snake_Game.git
   cd Snake_Game
```markdown


2. Install Python 3.x:
   - Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

3. Install dependencies:
   - This game uses the built-in `turtle` module and SQLite. No additional dependencies are required.

## How to Play
1. Run the game:
   ```bash
   python game.py
   ```

2. Use the **arrow keys** to control the snake:
   - **Up**: Move up
   - **Down**: Move down
   - **Left**: Move left
   - **Right**: Move right

3. Objective:
   - Eat the food (yellow circle) to grow the snake and increase your score.
   - Avoid hitting the walls or colliding with the snake's own body.

4. High Score:
   - Your highest score is saved and displayed at the top of the game screen.

## File Structure
- `game.py`: The main Python script for the Snake game.
- `snake_game.db`: SQLite database for storing the high score.

## Future Improvements
- Add levels with increasing difficulty.
- Implement additional power-ups or obstacles.
- Add a pause and resume feature.

```
