# BookBot
BookBot is a command-line application in Python that does static analysis on text files, or rather, entire novels like "Frankenstein".

Currently the application only accepts hard-coded file paths. This will be changed in the future to accept input when running the application.

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
Update the `book_path` variable at the top of main function with the path of the document you would like to analyse.
```bash
$ python3 main.py
```
