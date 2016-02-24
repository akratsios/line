from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    if (y1 >= y0):
        if y1 - y0 > x1 - x0:
            draw_line2( screen, x0, y0, x1, y1, color )
        else:
            draw_line1( screen, x0, y0, x1, y1, color )
    else:
        if y0 - y1 > x1 - x0:
            draw_line8( screen, x0, y0, x1, y1, color )
        else:
            draw_line7( screen, x0, y0, x1, y1, color )

#slope 0 < M <= 1
def draw_line1( screen, x0, y0, x1, y1, color ):
    B = x1 - x0
    A = y1 - y0
    d = B * 2
    d2 = 2 * (A - B)
    k = (A * 2) - B
    y = y0
    for x in range (x0, x1 + 1):
        if (k < 0):
            k += d
            plot(screen, color, x, y)
        else:
            k += d2
            y += 1
            plot(screen, color, x, y)


#slope M > 1
def draw_line2( screen, x0, y0, x1, y1, color ):
    B = x1 - x0
    A = y1 - y0
    d = B * 2
    d2 = 2 * (B - A)
    k = (B * 2) - A
    x = x0
    for y in range (y0, y1 + 1):
        if (k < 0):
            k += d
            plot(screen, color, x, y)
        else:
            k += d2
            x += 1
            plot(screen, color, x, y)


#slope 0 > M > -1
def draw_line8( screen, x0, y0, x1, y1, color ):
    y0, y1 = -1*y0, -1*y1
    B = x1 - x0
    A = y1 - y0
    d = B * 2
    d2 = 2 * (B - A)
    k = (B * 2) - A
    x = x0
    for y in range (y0, y1 + 1):
        if (k < 0):
            k += d
            plot(screen, color, x, -1*y)
        else:
            k += d2
            x += 1
            plot(screen, color, x, -1*y)


#slope M < -1
def draw_line7( screen, x0, y0, x1, y1, color ):
    y0, y1 = -1*y0, -1*y1
    B = x1 - x0
    A = y1 - y0
    d = B * 2
    d2 = 2 * (A - B)
    k = (A * 2) - B
    y = y0
    for x in range (x0, x1 + 1):
        if (k < 0):
            k += d
            plot(screen, color, x, -1*y)
        else:
            k += d2
            y += 1
            plot(screen, color, x, -1*y)