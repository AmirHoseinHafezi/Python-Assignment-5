import turtle
poly = turtle.Turtle()
sides = int(input('Enter the number of sides: '))
while True:
    color = input('Enter the color(red, blue, green, yellow, black, purple): ')
    if color == 'red' or color == 'blue' or color == 'green' or color == 'yellow' or color == 'black' or color == 'purple' :
        poly.color(color)
        break
    else:
        print('you have to choose between "red", "blue", "green" or "yellow" or "black" or "Purple" ')
        continue
for i in range(sides):
    poly.forward(180)
    poly.right(360 / sides)
turtle.done()