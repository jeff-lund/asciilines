# (c) Jeff Lund 2019
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE in the source distribution
# of this software for details

# Function to display a rendering of a text vector graphic image (tvg)

from sys import argv

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def invalid(msg="Invalid TVG file"):
    print("Error: " + msg)
    return False

def validate_tvg(tvg):
    # vaildate file exists
    if len(tvg) == 0:
        return invalid()

    # validate canvas size
    if len(tvg[0]) != 2:
        return invalid("Line 1: Canvas expects only two arguments")
    try:
        tvg[0] = list(map(int, tvg[0]))
    except ValueError:
        return invalid("Line 1: Canvas sizes must be integers")
    if any(val <= 0 for val in tvg[0]):
        return invalid("Line 1: Canvas size must be greater than 0")
    # Validate drawing lines
    # must be formatted:
    # <char: symbol> <int: row> <int: column> <{h, v}: axis> <int: length>
    for i, line in enumerate(tvg[1:]):
        if len(line) != 5:
            return invalid("Line {}: invalid number of arguments".format(i + 2))
        symb, row, col, axis, length = line
        if len(symb) != 1:
            return invalid("Line {}: Symbol to print must be a single character.".format(i + 2))
        if not all(is_digit(x) for x in (row, col, length)):
            return invalid("Line {}: Row, column, and length must all be integers".format(i + 2))
        row, col, length = map(int, (row, col, length))
        if length <= 0:
            return invalid("Line {}: Length must be greater than 0".format(i + 2))
        if axis != 'v' and axis != 'h':
            return invalid("Line {}: Line axis (h)orizontal or (v)ertical.".format(i + 2))
    return True

def pprint(field):
    ''' Prints out a tvg canvas line by line '''
    for line in field:
        print(''.join(line))

def read(line):
    ''' Converts relevant symbols from a tvg line '''
    symbol, row, col, direction, length = line
    return symbol, int(row), int(col), direction, int(length)

def convert_tvg(fname):
    # check file type is correct
    if fname[-3:] != 'tvg':
        invalid('incorrect file type')
        return

    with open(fname, 'r') as f:
        text = [line.strip().split(' ') for line in f]
    # Validate that the tvg file is correctly formatted
    if not validate_tvg(text):
        return
    # Set up canvas
    x, y = map(int, text[0])
    field =[['.' for __ in range(y)] for _ in range(x)]
    # Render each line
    for line in text[1:]:
        symbol, row, col, direction, length = read(line)
        if direction == 'h':
            for i in range(length):
                if col + i >= 0 and col + i < y:
                    field[row][col + i] = symbol
        elif direction == 'v':
            for i in range(length):
                if row + i >= 0 and row + i < x:
                    field[row + i][col] = symbol
    pprint(field)

if __name__ == '__main__':
    if len(argv) == 3 and ' '.join((argv[1], argv[2])) == 'run tests':
        dir = 'tests'
        tests = ['test1.tvg', 'test2.tvg', 'test3.tvg', 'test4.tvg', 'test5.tvg']
        fail_tests = ['test_f1.tvg', 'test_f2.tvg', 'test_f3.tvg', 'test_f4.tvg', 'test_f5.tvg']
        for i, t in enumerate(tests + fail_tests):
            print("-" * 30)
            print("Test", i)
            print("-" * 30)
            convert_tvg(dir + '/' + t)
    elif len(argv) != 2:
        print('Usage: python3', argv[0], '<tvg file>')
    else:
        convert_tvg(argv[1])
