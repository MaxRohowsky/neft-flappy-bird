# Neuro Evolution with Fixed Topologies (NEFT) Algorithm in Flappy Bird (from scratch without ML Libraries)

![Preview](/preview.gif)
<br>
<br>

##  Neural Evolution with Fixed Topologies Algorithm in Flappy Bird 

**Show support:** 
<br>
Star 🌟 the Project: ![GitHub stars](https://img.shields.io/github/stars/maxrohowsky/neft-flappy-bird.svg?style=social&label=Star)
<br>
Follow 🤝 on GitHub: ![GitHub followers](https://img.shields.io/github/followers/maxrohowsky.svg?style=social&label=Follow)
<br>

Made by [maxrohowsky](https://twitter.com/maxrohowsky)

## Table of contents

- [Description](#description)
- [YouTube Video](#youtube-video)
- [Installation](#installation)
- [Controls](#controls)
- [Libraries](#libraries)
- [FAQ](#faq)
- [Contact](#contact)

## Description

This is the **Flappy Bird Game** using **NEFT** and **Pygame** written in **Python**.
NEFT stands for neuro evolution of fixed topologies and is a genetic algorithm that creates artificial neural networks.

In contrast to the NEAT algorithm, NEFT does not change the topology of the neural network, but only the weights.
In this project, NEFT is used to train an AI to play the Flappy Bird Game. See how far your AI can Fly!


## YouTube Video

If you want to see how this project was built, you can watch the video here:
[Building the Flappy Bird A.I. without LIBRARIES](https://youtu.be/zsGvCwaaMOI)


## Installation

Requirements: You must have [Python](https://www.python.org/downloads/) installed and preferably a code editor like [PyCharm](https://www.jetbrains.com/pycharm/download/).

1. Clone the repository 
2. In the terminal, navigate to the directory where the repository was cloned, e.g., `C:\Users\Max\PycharmProjects\neft-flappy-bird`
3. Create a virtual environment, activate it, and install pygame by running the following commands in the terminal:
    ```bash
    python -m venv venv #This creates a virtual environment
    venv\Scripts\activate #This activates the virtual environment
    pip install -r requirements.txt #This installs the required libraries
    ```
4. Run the game by running the following command in the terminal:
    ```bash
    python main.py
    ```
Note on PyCharm: Often PyCharm detects the requirements.txt file and asks you to install its contents and create a virtual env.
That's the easiest way to get started. If you want to do it manually, you can follow the steps above.

## Controls

You don't need to control the bird. The AI will do that for you :)

## Libraries

Alight, I confess, although I said "without libraries" in the video title, I did use the pygame library to create the game.
However, the NEFT algorithm is implemented from scratch.

- [pygame](https://www.pygame.org/news): Pygame is a cross-platform set of Python modules designed for writing video games.

## FAQ

- How to Open GitHub Projects in PyCharm? [Explained Here](https://youtu.be/cAnWazo5pFU)
- How to use Virtual Environments? [Explained Here](https://youtu.be/2P30W3TN4nI)
- How to install PyCharm and Python? [Explained Here](https://youtu.be/XsL8JDkH-ec)
- How to set PyCharm Config. and Interpreter? [Explained Here](https://youtu.be/OajNS-WHiUI)

## Contact

Feel free to reach out to me [on Twitter](https://twitter.com/max_on_tech) if you have any questions or feedback! Hope you find this useful!
