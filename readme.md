# 2D Football

2D Football is a simple two-player football simulation game built with Pygame and Firebase. It features basic player movements, ball control, shooting, and scoring.

## How to Play

### Controls

#### Player 1:
- **W**: Move up
- **S**: Move down
- **A**: Move left
- **D**: Move right
- **SPACE**: Shoot

#### Player 2:
- **UP_ARROW**: Move up
- **DOWN_ARROW**: Move down
- **LEFT_ARROW**: Move left
- **RIGHT_ARROW**: Move right
- **NUMPAD_0**: Shoot

#### Goalkeepers:
- Scripted movment.

## Installation

### Requirements
- Python 3.x
- Pygame
- firebase

### Running the Game

1. create env folder using `py -m virtualenv env` and activate by using `env\Scripts\activate`.
2. Clone the repository.
3. Go to 2DFootball_Firebase file using `cd ./2DFootball_Firebase` and install the requirements using `pip install -r .\requirements.txt`.
4. Run the script `py ./main.py`.

## Gameplay

- Both players can control the movement of their respective characters.
- Players can take control of the ball if they're close to it.
- Players can shoot the ball in any direction.
- Score a goal by getting the ball into the opponent's net.
- First player to reach five goals wins the game.

## Classes and Components

- `Pitch`: Handles the drawing of the pitch including goals.
- `Player`: Handles the movement and actions of the player's character.
- `Opponent`: Handles the movement and actions of the opponent's character.
- `Ball`: Controls the movement and mechanics of the ball.
- `Score`: Manages and displays the current score.
- `Func`: Manages all the functions.
- `Database`: Setting the Firebase database.
- `GameLoop`: Manages the game itself.
- `Main`: The main component of the app, this is the component that you need to run in oreder to start the game.
- `Goalkeeper`: Handles the movment and actions of the goalkeepers.
- `Menu`: Manages the menu loop.
- `Screen`: Sets the screen for all the other components.
- `VictoryScreen`: Manages the victory screen, shows who won and moves you back into the main menu.
- `Sounds`: Manages the sound effects across the program.
- `Static folder`: Holds the sound effects files.

## Game picture
![2D_Football_img](https://github.com/ronxzone/2DFootball_Firebase/blob/4c9d65a3d842a98d1eab9bf45d13fdd53f1437c1/2D_Football_gh.jpg)

## Acknowledgments

The game is created as part of an educational project, and all the resources used are either built-in or created by the author.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

"# 2D_Football" "# 2DFootball_Firebase" 
