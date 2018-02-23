import turtle  
  
num = int(input('Please input the num of the polygon:'))  
color = input('Please input the color of the fillcolor:')  
turtle.fillcolor(color)  
angel = 180 - (num - 2) * 180 / num  
turtle.begin_fill()  
for i in range(num):  
    turtle.forward(160)  
    turtle.right(angel)  
turtle.end_fill()  
turtle.done()
