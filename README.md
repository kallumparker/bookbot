# BookBot
BookBot is a command-line application in Python that does static analysis on text files, or rather, entire novels like "Frankenstein".

BookBot accepts a text file path as a command-line argument and reports its word count and alphabetic character counts.

## Getting Started
Please, follow the instructions below for installing and running BookBot.

### Pre-requisites
Make sure you have installed Python 3.0 or later:
```bash
$ sudo apt update
$ sudo apt install -y python3
```

### Installing
```bash
$ git clone https://github.com/kallumparker/bookbot.git
$ cd bookbot
$ chmod +x main.py
```

### Usage
```bash
$ python3 main.py books/frankenstein.txt
```

Other text files can be analyzed by passing their paths as arguments.
