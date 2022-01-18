import turtle as trtl

trtl.bgcolor("Black")
trtl.pensize(2)
trtl.speed(0)

for i in range(6):
    for colors in ["Red", "Green", "Blue", "Purple", ]:
        trtl.color(colors)
        trtl.circle(100000)
        trtl.left(10)


wn = trtl.Screen()
wn.mainloop()


trtl.hideturtle()