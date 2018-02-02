# matplotlib.py demo
import matplotlib.pyplot as plot

def f(x):
    # code that calculates values
    return x

xs = range(-3, 4) # our x-axis values
ys = []
for x in xs:
    ys.append(f(x)) # generate our y-axis values

plot.bar(xs, ys) # draw a bar graph
plot.show() # show the graph window
