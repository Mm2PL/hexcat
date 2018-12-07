#!/usr/bin/python3
# Copyright (C) 2018 Maciej Marciniak
import argparse
import time
from os import path
import os
try:
    import psutil
except ImportError:
    psutil = None

CUSTOM_RULES = {
    '\n': '↲',
    '\r': '↵',
    '\t': '⇥',
    '\a': '␇',  # Bell
    '\x00': '␀',  # NULL
    '\033': '␛'  # Escape character
}
p = argparse.ArgumentParser(description='cat, but displays hexadecimal representations of characters.',
                            epilog='hexcat Copyright (C) 2018 Maciej Marciniak')
p.add_argument('file', metavar='FILE', help='File to cat')
p.add_argument('-nt', '--no-translate', action='store_true', dest='no_trans', help='Don\'t show the characters')
p.add_argument('--all', '-a', dest='read_all', action='store_true', help='Read the WHOLE file. '
                                                                         'Requires confirmation on big files')
p.add_argument('-nl', '--no-line-numbers', dest='show_line_nums', action='store_false',
               help='Don\'t show the line numbers')
args = p.parse_args()

if not path.isfile(args.file):
    print('Argument 0 (file): Path must lead to a file')
    exit(os.EX_USAGE)

file_size = path.getsize(args.file)  # In bytes
file_size /= 1000  # In kilobytes
file_size /= 1000  # In megabytes
if args.read_all:
    if file_size > 1:
        size_word = 'megabytes'
        if file_size*10 > 1000:
            size_word = 'gigabytes'
        if file_size*10 > (1000*1000):
            size_word = 'terabytes'
        print('WARNING: This will load the WHOLE file into memory. Are you sure you want to continue?')
        print('This action will print {} of data to STDOUT and use the same amount of RAM\n'.format(size_word))
        ans = 'n'
        while 1:
            try:
                ans = input('\033[A[Y/n]').lower()
            except (KeyboardInterrupt, EOFError) as e:
                print('\n\033[A[Y/n] No ({})'.format('^C' if isinstance(e, KeyboardInterrupt) else
                                                     ('^D' if os.name == 'posix' else '^Z\\n')))
                exit()
            if len(ans) == 0:
                continue
            if ans[0] == 'n':
                print('\033[A[Y/n] No')
                exit()
            elif ans[0] == 'y':
                print('\033[A[Y/n] Yes')
                break
try:
    tsize = os.get_terminal_size()
    cols = tsize[0]/(1 if args.no_trans else 1.32)
except OSError:
    cols = 80/(1 if args.no_trans else 1.32)
line_num = 0
line_num_size = round(len(str(file_size*1000000))/1.32) if args.show_line_nums else 0

with open(args.file, 'rb') as plik:
    line = ''
    print('Loading file....')
    print('  File size: {0:.2f} megabytes'.format(file_size))
    print('  Dumping: {}'.format('all' if args.read_all else 'first 4096 bytes'))
    pre_load = time.time()
    data = plik.read(4096 if not args.read_all else int(file_size*1000000))
    print('   -> Loaded (This took {0:.2f} seconds)'.format(time.time()-pre_load))
    del pre_load
    if psutil:
        self = psutil.Process(os.getpid())
        ram_used = self.memory_info().rss
        ram_total = psutil.virtual_memory().total
        print('   -> Using: {0:.2f} megabytes of RAM ({1:.2f} %)'.format(ram_used / 1000 / 1000,
                                                                         ram_used / ram_total * 100))
    else:
        print('   -> Cannot check ram usage: psutil is not installed.')

    print('Press ^C to exit')
    try:
        print('Waiting {} second{}'.format(5 if args.read_all else 1, 's' if args.read_all else ''))
        time.sleep(5 if args.read_all else 1)
    except KeyboardInterrupt:
        exit()
    if args.show_line_nums:
        print((line_num_size - 1) * ' ', 0, sep='', end=' ')
    curr_col = line_num_size
    for l in data:
        if curr_col >= cols-5:
            line_num += 1
            if args.no_trans:
                print('\n', (' '*(line_num_size-len(str(line_num)))+str(line_num)+' ' if args.show_line_nums else ''), flush=True, end='')
            else:
                print(' ', line, '\n', (' '*(line_num_size-len(str(line_num)))+str(line_num)+' ' if args.show_line_nums else ''), sep='', end='')
            line = ''

            curr_col = line_num_size+1

        print('{0:0=2X}'.format(l), end=' ')
        ch = chr(l)
        if ch.isprintable():
            line += ch
        else:
            if ch in CUSTOM_RULES:
                line += CUSTOM_RULES[ch]
            else:
                line += '.'
        curr_col += 3
    if not args.no_trans:
        print(round(cols-curr_col)*' ', line, sep='')
print()
