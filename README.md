# asciilines

Copyright (c) 2019 Jeff Lund

This program takes in a Text Vector Graphics (.tvg) file and displays the rendering.

## TVG Format
A Text Vector Graphic file takes the following form:
The first line consists of two numbers to represent the length and width respectively of the graphic to be rendered. Each following line will fill the canvas with a line of a characters. Each line is drawn sequentially so later lines will overwrite earlier ones. The format of each line is : `symbol` `row index` `column index` `axis` `length`
`symbol` : A single character to render.
`row index` : The starting row position of the line to render. Can start the canvas, only points within the canvas will be rendered.
`column index` : The starting column position of the line to render. Can start the canvas, only points within the canvas will be rendered.  
`axis` : Controls whether to draw a veritcal or horizontal line. Accepts `h` or `v` as arguments.
`length` : Length of the line to draw. Can extend outside the canvas, only points within the canvas will be rendered.

Incorrectly formatted TVG files will output an error.

## Usage

`python3 tvgconveter.py <tvg file>`

## Examples
Sample TVG file:

`3 4
\* 1 -1 h 5
\# -1 1 v 5`

Output:

`.#..
*#**
.#..`

## License
This program is licensed under the "MIT License". Please see the file LICENSE in the source distribution of this software for license terms.
