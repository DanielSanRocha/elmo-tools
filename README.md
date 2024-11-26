# ELMO Tools

A bunch of useful tools for making your life easier! Tested on python 3.12.7.

## Setup

Clone the repo anywhere and add it folder you cloned to your **PATH** environment variable. For example, if you clone in a folder called `elmo-tools` in your home directory and use bash you can add

```bash
export "~/elmo-tools:$PATH"
```
at the end of your `.bashrc`.

To install all python deps, run (WARNING: This will install all deps in your system with --user and --break-system-packages!)
```bash
make setup
```

## copy

A simple command to copy from stdout of other program. You need **xclip** installed in your system to this to work properly. Example:

```
echo "1234" | copy
```

After that, you can paste "1234" anywhere else.

## paste

You need *xclip* to this to work properly. A simple command to print what is copied in your clipboard. For example, you could copy a link somewhere, then run in bash

```bash
curl $(paste)
```

to make a simple GET request to the url you copied. You can also pipe the currente clipboard to other commands!

## docker-clean

Kill all containers, remove all containers, delete all images the purge docker cache. Very useful when you want to free up space on your computer. Usage:

```bash
docker-clean
```

## size

A very cool utility to calculate with more precision the size of file and folders and find folders/files that are occupying too much space. For more info, run

```bash
size --help
```
