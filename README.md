# rock-paper-scissors-exercise
Repo Setup

Use the GitHub online interface to create a new remote project repository called something like "rock-paper-scissors-exercise". When prompted by the GitHub online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub at an address like https://github.com/YOUR_USERNAME/rock-paper-scissors-exercise.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

cd ~/Desktop/rock-paper-scissors-exercise
Use your text editor or the command-line to create a file in that repo called "game.py", and then place the following contents inside:

# game.py

print("Rock, Paper, Scissors, Shoot!")
Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file.

Environment Setup

FYI: Only because we're going to be working with environment variables and requiring a third-party package called "python-dotenv" to read them from the ".env" file (see details below), we'll want to use a new project-specific Python environment within which to install any required packages. Otherwise we could do this exercise in the "base" environment.
Create and activate a new project-specific Anaconda virtual environment:

conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

python game.py
If you see the "Rock, Paper, Scissors, Shoot!" message, you're ready to move on to project development. This would be a great time to make any desired modifications to your project's "README.md" file (like adding instructions for how to setup and run the app like you've just done), and then make your first commit, with a message like "Setup the repo".