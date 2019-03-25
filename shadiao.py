from turtle import*
setup(1600,800,0,0)#sheding pinmu daxiao
pensize(10)#bi de kuandu
pencolor("red")#pens color
penup()
goto(-100,100)#set yuandian
pendown()
left(45)
fd(100)
circle(50,180)
penup()
goto(-100,100)#return yuandian
down()
right(90)
fd(100)
left(180)
circle(50,-180)
penup()
goto(-300,-100)
pendown()
write("你就是个大煞笔！！！！",font=("snap itc",20,"normal"))
hideturtle()
