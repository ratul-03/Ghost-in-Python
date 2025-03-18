# Pygame Scary Sound & Image Script

## Description
This Python script uses **Pygame** to create a scary effect by playing eerie sounds and displaying a horror image in fullscreen mode.

## Features
- Runs in **fullscreen mode**.
- Plays two consecutive **scary sound effects**.
- Displays a **horror image** after the second sound effect.

## Prerequisites
- Python 3 installed on your system.
- **Pygame library** installed.
  
  Install Pygame using:
  ```bash
  pip install pygame
  ```

## How to Run
1. Clone this repository or download the `main.py` file.
2. Place the required assets (`ratsasan.mp3`, `scary.mp3`, and `scr.jpg`) inside an **`assets/`** folder.
3. Open a terminal or command prompt.
4. Navigate to the script directory.
5. Run the script using:
   ```bash
   python main.py
   ```
6. The script will:
   - Play `ratsasan.mp3`.
   - Play `scary.mp3`.
   - Display `scr.jpg` in fullscreen mode.

## File Structure
```
project-folder/
│── main.py
│── assets/
│   ├── ratsasan.mp3
│   ├── scary.mp3
│   ├── scr.jpg
```

## Example Behavior
1. The screen turns **black** initially.
2. The first sound (`ratsasan.mp3`) plays.
3. The second sound (`scary.mp3`) plays.
4. The horror image (`scr.jpg`) appears suddenly.

## Future Improvements
- Add an **exit condition** (e.g., pressing a key to close the window).
- Use **randomized images and sounds** for variation.
- Enhance user experience with animations.

## License
This project is open-source and available under the MIT License.
