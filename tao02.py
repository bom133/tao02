import turtle
tao = turtle.Pen()
tao.shape('turtle')
def Rec():
    for i in range(4):
        tao.forward(100)
        tao.right(90)
    
  
def go(x,y):
    tao.clear()
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
    for i in range(4):
        tao.right(90)
        Rec()
        
        

go(0,0)
