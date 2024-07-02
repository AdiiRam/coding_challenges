"""
Challenge   : Build Your own wc tool 
Description : To build own version of the Unix command line tool wc 
"""
import argparse
import os 

def get_file_size(fname):
    """
    This will get the Size of the file in bytes 
    """
    file_stats = os.stat(fname)
    size_bytes = file_stats.st_size

    return size_bytes

def get_no_of_lines(fname):
    """
    This will get the No of lines in the file 
    """
    line_count = 0
    with open(fname) as fin:        
        for line in fin:
            line_count +=1 

    return line_count

def get_no_of_words(fname):
    """
    This will get the No of Words in the file 
    """
    word_count = 0
    with open(fname) as fin:
        for line in fin:
            words = line.split(' ')
            word_count += len(words)
    
    return word_count

def get_no_of_characters(fname):
    """
    This will get the No of Characters in the file
    """
    char_count = 0
    with open(fname) as fin:
        for line in fin:
            char_count += len(line)
            char_count += 1
    
    return char_count

if __name__ == '__main__': 

    # Read the command line arguments 
    parser = argparse.ArgumentParser(
        prog='Unix_wc',
        description='Unix version of wc tool'
    )
    parser.add_argument('filename')
    parser.add_argument('-c', action='store_true', dest='get_size')
    parser.add_argument('-l', action='store_true', dest='get_no_of_lines')
    parser.add_argument('-w', action='store_true', dest='get_no_of_words')
    parser.add_argument('-m', action='store_true', dest='get_no_of_characters')
    args = parser.parse_args()

    default_mode = True

    fname = args.filename
    if args.get_size:
        print(f"{get_file_size(fname)} {fname}")
        default_mode = False
    
    if args.get_no_of_lines:
        print(f"{get_no_of_lines(fname)} {fname}")
        default_mode = False
    
    if args.get_no_of_words:
        print(f"{get_no_of_words(fname)} {fname}")
        default_mode = False
    
    if args.get_no_of_characters:
        print(f"{get_no_of_characters(fname)} {fname}")
        default_mode = False
    
    # Check if options were provided or not . If no option given , then command has to run 
    # in default mode i.e. 
    # wc -c -l -w <filename> 

    if default_mode is True:
        (l,w,c) = get_no_of_lines(fname), get_no_of_words(fname), get_file_size(fname)
        print(f"{l} {w} {c} {fname}")