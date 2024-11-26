# ELMO Tools

A bunch of useful tools for making your life easier! Tested on python 3.12.7.

![image](assets/elmo-burning.gif)

- [ELMO Tools](#elmo-tools)
  - [Setup](#setup)
    - [Shell (bash,zsh,xonsh...)](#shell-bashzshxonsh)
    - [Installing dependencies](#installing-dependencies)
      - [Python requirements](#python-requirements)
      - [xclip](#xclip)
  - [Commands](#commands)
    - [copy](#copy)
    - [paste](#paste)
    - [docker-clean](#docker-clean)
    - [size](#size)
    - [try](#try)
  - [TODOs](#todos)
  - [Acknowledgements](#acknowledgements)

## Setup

### Shell (bash,zsh,xonsh...)
Clone the repo anywhere and add it folder you cloned to your **PATH** environment variable. For example, if you clone in a folder called `elmo-tools` in your home directory and use **bash** you can add

```bash
export "~/elmo-tools:$PATH"
```
at the end of your `.bashrc`. The same is true for **zsh**.

For **xonsh** you can add 

```python
$PATH.insert(0, "~/elmo-tools")
```

to your `.xonshrc` file.

### Installing dependencies

#### Python requirements

To install all python deps, run (WARNING: This will install all deps in your system with --user and --break-system-packages!)
```bash
make setup
```

#### xclip

Some commands also need *xclip*. You can install it on:

1) Ubuntu, Debian or Linux Mint:
```bash
sudo apt update
sudo apt install xclip
```

2) Fedora, CentOS, AlmaLinux or Red Hat:
```bash
sudo dnf install xclip
```

3) Arch linux with
```bash
sudo pacman -Sy
sudo pacman -S xclip
```

## Commands

### copy

A simple command to copy from stdout of other program. You need **xclip** installed in your system to this to work properly. Example:

```
echo "1234" | copy
```

After that, you can paste "1234" anywhere else.

### paste

You need *xclip* to this to work properly. A simple command to print what is copied in your clipboard. For example, you could copy a link somewhere, then run in bash

```bash
curl $(paste)
```

to make a simple GET request to the url you copied. You can also pipe the currente clipboard to other commands!

### docker-clean

Kill all containers, remove all containers, delete all images the purge docker cache. Very useful when you want to free up space on your computer. Usage:

```bash
docker-clean
```

### size

A very cool utility to calculate with more precision the size of file and folders and find folders/files that are occupying too much space. For more info, run

```bash
size --help
```

### try

Try any command until it works. For example

```bash
try curl -f localhost:1234
```

Will try to access localhost:1234 until it reply an acceptable HTTP status code. Useful for checking if a service is up, for example.

## TODOs

1) Make it easier to run all commands inside a virtualenv (pyenv,poetry,venv...)
2) All python code is linted with ruff. Enforce this in the repo.
3) All bash code is linted with shfmt. Enforce this in the repo.
4) Add a development guide.

## Acknowledgements

For now just some simple tools. In the future I intend to add some crazy stuff I created to make my life easier =).

Made with love by Daniel Santana!
