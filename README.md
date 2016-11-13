# The-Cove

## Summary

This is a YHack 2016 project and submission.

The Cove is a 2D Survival Game that employs an emotionally adaptive artificial intelligence. The goal of the game is simple: the player is stranded on an island, trying to build a boat to escape. However, there is a mysterious being on the island, called The Hound, that has the one final piece you need to finish the boat. Upon interacting with it, the player is presented with four options:

#### Run
If the player changes his or her mind, try to leave the interaction and see if The Hound allows it.

#### Trade
The player has some items he or she can attempt to give The Hound. It may respond favorably. 

#### Talk
Want to smooth talk The Hound? Anger it? Plead with it? Go ahead! The Cove employs NLP and ML to teach The Hound to respond emotionally to text from the player.

#### Battle
Think you can directly beat The Hound in one-on-one battle? If you defeat it, victoriously take the item you need.

## Installation

The game is built and compiled in Game Maker: Studio. We provide the .exe game for you in this repo, no installation necessary. (For Mac users, this program works perfectly with your favorite Windows program emulator, such as Wine or CrossOver).

The backend of the game is written in Python 2, where a web server is hosted that the game can make HTTP requests to. The user has to manually set this up before starting the game. 

First, the necessary Python modules to install using pip:

```sh
# 1) install Python numerical and ML packages
pip install sklearn scipy numpy

# 2) install Flask (the web server)
pip install flask

# 3) install Indico API wrapper (text analysis)
pip install indicoio
```

Next, to run this game yourself, you need to aquire a free Indico API key [here] (https://indico.io/non-commercial) to allow the program to use their API (for talking with The Hound).

In [src/config.json] (https://github.com/coreycle/The-Cove/blob/master/src/config.json), change the `indico_api_key` to the one you aquired above.

That's it! You should be ready to run the server and play the game!

## Running the Server

Simply start [src/app.py] (https://github.com/coreycle/The-Cove/blob/master/src/app.py) using the following:

```sh
python app.py
```

and the webserver will be initialized and hosted locally, so the game can utilize the Python scripts for its logic.

## Playing the Game

Here are the necessary keybindings and points one needs to play:

#### Moving Around
Using the four arrow keys, you can move your character around the map.

#### Attacking
If you find yourself in a fight with the hound, the `V` key will swing a sword in the direction you are facing, causing damage.

#### Anything Else?
All other important instructions are stated in the game. Enjoy!