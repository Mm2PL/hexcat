# HEXCAT
Cat, but works like a hex viewer. Written in Python 3
### INSTALATION
1. _Optional_ Run `pip install psutil` to install psutil
   - psutil is required to show you how much RAM is used.
2. Make it executable everywhere
(Pick one)
   * **linux only** Create a link in /usr/bin/ to hexcat.py
   * Add to your PATH
   * Skip this step
3. It's done.
### Usage
```
hexcat [-h] [-nt] [--all] [-nl] FILE
  FILE                    File to cat

  -h, --help              show this help message and exit
  -nt, --no-translate     Don't show the characters
  --all, -a               Read the WHOLE file. Requires confirmation on big
                          files
  -nl, --no-line-numbers  Don't show the line numbers

```
### Features

- Confirmation on big files (more than 1 megabyte)
    - Note: this program shows approximately 3 times the size of the file.
- You can disable the translation of the data to printable characters and the line numbers

### Examples
```
// File 0
This is a text file
Some data
spam
spam
spam
monty python
spam
spam
spam
spam
spam
we serve only spam here
spam
spam
spam
spam

```
- `hexcat file0` <br>
Output:
```
Loading file....
  File size: 0.00 megabytes
  Dumping: first 4096 bytes
   -> Loaded (This took 0.00 seconds)
   -> Using: 13.05 megabytes of RAM (0.16 %)
Press ^C to exit
Waiting 1 second
             0 2F 2F 20 46 69 6C 65 20 30 0A 54 68 69 73  // File 0↲This
             1 20 69 73 20 61 20 74 65 78 74 20 66 69 6C   is a text fil
             2 65 0A 53 6F 6D 65 20 64 61 74 61 0A 73 70  e↲Some data↲sp
             3 61 6D 0A 73 70 61 6D 0A 73 70 61 6D 0A 6D  am↲spam↲spam↲m
             4 6F 6E 74 79 20 70 79 74 68 6F 6E 0A 73 70  onty python↲sp
             5 61 6D 0A 73 70 61 6D 0A 73 70 61 6D 0A 73  am↲spam↲spam↲s
             6 70 61 6D 0A 73 70 61 6D 0A 77 65 20 73 65  pam↲spam↲we se
             7 72 76 65 20 6F 6E 6C 79 20 73 70 61 6D 20  rve only spam 
             8 68 65 72 65 0A 73 70 61 6D 0A 73 70 61 6D  here↲spam↲spam
             9 0A 73 70 61 6D 0A 73 70 61 6D 0A 0A           ↲spam↲spam↲↲
```
 - `hexcat file0 --no-line-numbers` <br>
 Output:
```
Loading file....
  File size: 0.00 megabytes
  Dumping: first 4096 bytes
   -> Loaded (This took 0.00 seconds)
   -> Using: 13.04 megabytes of RAM (0.16 %)
Press ^C to exit
Waiting 1 second
2F 2F 20 46 69 6C 65 20 30 0A 54 68 69 73 20 69 73 20 61  // File 0↲This is a
20 74 65 78 74 20 66 69 6C 65 0A 53 6F 6D 65 20 64 61 74   text file↲Some dat
61 0A 73 70 61 6D 0A 73 70 61 6D 0A 73 70 61 6D 0A 6D 6F  a↲spam↲spam↲spam↲mo
6E 74 79 20 70 79 74 68 6F 6E 0A 73 70 61 6D 0A 73 70 61  nty python↲spam↲spa
6D 0A 73 70 61 6D 0A 73 70 61 6D 0A 73 70 61 6D 0A 77 65  m↲spam↲spam↲spam↲we
20 73 65 72 76 65 20 6F 6E 6C 79 20 73 70 61 6D 20 68 65   serve only spam he
72 65 0A 73 70 61 6D 0A 73 70 61 6D 0A 73 70 61 6D 0A 73  re↲spam↲spam↲spam↲s
70 61 6D 0A 0A                                              pam↲↲

```
 - `hexcat file0 -nt -nl` <br>
 Output:
```
 Loading file....
  File size: 0.00 megabytes
  Dumping: first 4096 bytes
   -> Loaded (This took 0.00 seconds)
   -> Using: 13.01 megabytes of RAM (0.16 %)
Press ^C to exit
Waiting 1 second
2F 2F 20 46 69 6C 65 20 30 0A 54 68 69 73 20 69 73 20 61 20 74 65 78 74 20 
66 69 6C 65 0A 53 6F 6D 65 20 64 61 74 61 0A 73 70 61 6D 0A 73 70 61 6D 0A 
73 70 61 6D 0A 6D 6F 6E 74 79 20 70 79 74 68 6F 6E 0A 73 70 61 6D 0A 73 70 
61 6D 0A 73 70 61 6D 0A 73 70 61 6D 0A 73 70 61 6D 0A 77 65 20 73 65 72 76 
65 20 6F 6E 6C 79 20 73 70 61 6D 20 68 65 72 65 0A 73 70 61 6D 0A 73 70 61 
6D 0A 73 70 61 6D 0A 73 70 61 6D 0A 0A
```
### Big files
 - `hexcat a_big_file` <br>
```
WARNING: This will load the WHOLE file into memory. Are you sure you want to continue?
This action will print megabytes of data to STDOUT and use the same amount of RAM
[Y/n] yes
Loading file....
  File size: 1.50 megabytes
  Dumping: all
   -> Loaded (This took 0.00 seconds)
   -> Using: 14.59 megabytes of RAM (0.18 %)
Press ^C to exit
Waiting 5 seconds
      0 2F 2F 20 46 69 6C 65 20 30 0A 0A 54 68 69 73 20 69  // File 0↲↲This i
      1 73 20 61 20 74 65 78 74 20 66 69 6C 65 0A 0A 53  s a text file↲↲S
      2 6F 6D 65 20 64 61 74 61 0A 0A 73 70 61 6D 0A 0A  ome data↲↲spam↲↲
      3 73 70 61 6D 0A 0A 73 70 61 6D 0A 0A 6D 6F 6E 74  spam↲↲spam↲↲mont
      4 79 20 70 79 74 68 6F 6E 0A 0A 73 70 61 6D 0A 0A  y python↲↲spam↲↲
      5 73 70 61 6D 0A 0A 73 70 61 6D 0A 0A 73 70 61 6D  spam↲↲spam↲↲spam
      6 0A 0A 73 70 61 6D 0A 0A 77 65 20 73 65 72 76 65  ↲↲spam↲↲we serve
      7 20 6F 6E 6C 79 20 73 70 61 6D 20 68 65 72 65 0A   only spam here↲
      8 0A 73 70 61 6D 0A 0A 73 70 61 6D 0A 0A 73 70 61  ↲spam↲↲spam↲↲spa
      9 6D 0A 0A 73 70 61 6D 0A 0A 0A 30 30 30 30 30 30  m↲↲spam↲↲↲000000
     10 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30  0000000000000000

...

  93758 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30  0000000000000000
  93759 30 30 30 30 30 30 30 30 30 30 0A                     0000000000↲
```
