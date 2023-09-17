def multiply_by_five():
    x = None
    while True:
        x = yield x
        x *= 5


g = multiply_by_five()
next(g)
g.send(4)
g.send('You all awesome python devs')
