from sys import argv, exit

def pprint(field):
    for line in field:
        print(''.join(line))

def read(line):
    symbol, row, col, direction, length = line
    return symbol, int(row), int(col), direction, int(length)

def convert_tvg(fname):
    # check file type is correct
    if fname[-3:] != 'tvg':
        print('Error: incorrect file type')
        return
    
    with open(fname, 'r') as f:
        text = [line.strip().split(' ') for line in f]
    
    # set up canvas
    x, y = map(int, text[0])
    field =[['.' for __ in range(y)] for _ in range(x)]
    
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
    if len(argv) != 2:
        print('Usage: python3', argv[0], '<tvg file>')
    else:
        convert_tvg(argv[1])
