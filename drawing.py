import turtle
t = turtle.Turtle()
win = turtle.Screen()
win.bgcolor("white")
t.speed(0)
colors=['red','orange','yellow','green','blue','purple']
t.hideturtle()
t.up()
t.left(90)
t.forward(300)
your_name=turtle.textinput('put in your name','whats your name?')
t.showturtle()
t.down()
t.write(your_name, font=('Arial',20))
t.up()
t.hideturtle()
t.right(180)
t.forward(300)
t.down()
t.showturtle()
colorc=turtle.textinput('color','red,orange,yellow,green,blue,or purple')
if colorc=='red':
    t.color('red')
if colorc=='orange':
    t.color('orange')
if colorc=='yellow':
    t.color('yellow')
if colorc=='green':
    t.color('green')
if colorc=='blue':
    t.color('blue')
if colorc=='purple':
    t.color('purple')
while 1<2:
    move=turtle.textinput('draw','forward,backward,left,or right')
    if move=='forward':
        t.forward(20)
    if move=='backward':
        t.backward(20)
    if move=='left':
        t.left(90)
    if move=='right':
        t.right(90)
colorc=turtle.textinput('color','red,orange,yellow,green,blue,or purple')
if colorc=='red':
    t.color('red')
if colorc=='orange':
    t.color('orange')
if colorc=='yellow':
    t.color('yellow')
if colorc=='green':
    t.color('green')
if colorc=='blue':
    t.color('blue')
if colorc=='purple':
    t.color('purple')
