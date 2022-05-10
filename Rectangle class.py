class rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height
  def set_width(self,width):
    self.width=width
  def set_height(self):
    self.height=height
  def rect(self):
    print('Rectangle(width=',self.width,'heigh=',sself.height)
  def get_area(self):
    x=self.width*self.height
    return x
  def get_perimeter(self):
    f=2*self.width+2*self.height
    return f
  def get_diagonal(self):
    h=(self.width**2+self.height**2)**0.5
    return h
  def get_picture(self):
    if((self.height>50)or(self.height>50)):
      return 'Too big for picture'
    else:
      for i in range(self.height):
        for j in range(self.width):
          print('*',end=" ")
        print()
  def get_amount_inside(self,smallw=-1,smallh=-1):
    return (self.width*self.height)//(smallh*smallw)         
class Square:
  def __init__(self):
    self.side=-1
  def set_side(self,x):
    self.side=x
  def sq(self):
    print('square(side=',self.side)
        
