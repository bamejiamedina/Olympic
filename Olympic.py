import sys
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
  
class Olympic(QWidget):
    
  def __init__(self):
    super().__init__()           
    self.setGeometry(300, 300, 550, 600)  # 0 <= x <= 550, 0 <= y <= 600
    self.setWindowTitle('Olympic Rings')
    self.isBlue = False
    self.isYellow = False
    self.isBlack = False
    self.isGreen = False
    self.isRed = False
    self.show()    
    
  def mousePressEvent(self, event):
    self.x = event.x()
    self.y = event.y()
    
    def point_is_in_the_circle(origin_x, origin_y, radius, x, y):
      d = ((x - origin_x)**2 + (y - origin_y)**2)**(1/2)
      if (d < radius):  
        return True
      return False 
      
    self.isBlue = False
    self.isYellow = False
    self.isBlack = False
    self.isGreen = False
    self.isRed = False    
    if(point_is_in_the_circle(149, 200, 50, self.x, self.y)): 
      self.isBlue = True
    if(point_is_in_the_circle(211.5, 250, 50, self.x, self.y)):
      self.isYellow = True
    if(point_is_in_the_circle(274, 200, 50, self.x, self.y)):
      self.isBlack = True
    if(point_is_in_the_circle(336.5, 250, 50, self.x, self.y)):
      self.isGreen = True
    if(point_is_in_the_circle(399, 200, 50, self.x, self.y)):
      self.isRed = True
    self.update()
    
  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    bluePen = QPen(QBrush(Qt.blue), 5)
    yellowPen = QPen(QBrush(Qt.yellow), 5)
    blackPen = QPen(QBrush(Qt.black), 5)
    greenPen = QPen(QBrush(Qt.green), 5)
    redPen = QPen(QBrush(Qt.red), 5)
    qp.setPen(bluePen)
    qp.drawEllipse(99, 150, 100, 100)
    qp.setPen(yellowPen)
    qp.drawEllipse(161.5, 200, 100, 100)
    qp.setPen(bluePen)
    qp.drawArc(99, 150, 100, 100, 345*16, 30*16)
    qp.setPen(blackPen)
    qp.drawEllipse(224, 150, 100, 100)
    qp.setPen(yellowPen)
    qp.drawArc(161.5, 200, 100, 100, 70*16, 15*16)
    qp.setPen(greenPen)
    qp.drawEllipse(286.5, 200, 100, 100)
    qp.drawArc(286.5, 200, 100, 100, 160*16, 30*16)
    qp.setPen(blackPen)
    qp.drawArc(224, 150, 100, 100, 345*16, 30*16)
    qp.setPen(redPen)
    qp.drawEllipse(349, 150, 100, 100)
    qp.setPen(greenPen)
    qp.drawArc(286.5, 200, 100, 100, 70*16, 15*16)
    
    if((self.isBlue) or (self.isYellow) or (self.isBlack) or (self.isGreen) or (self.isRed)):
      if(self.isBlue):
        qp.fillRect(100, 450, 350, 100, Qt.blue)
      if(self.isYellow):
        qp.fillRect(100, 450, 350, 100, Qt.yellow)
      if((self.isBlue) and (self.isYellow)):
        qp.fillRect(100, 450, 175, 100, Qt.blue)
        qp.fillRect(275, 450, 175, 100, Qt.yellow)
      if(self.isBlack):
        qp.fillRect(100, 450, 350, 100, Qt.black)
      if((self.isBlack) and (self.isYellow)):
        qp.fillRect(100, 450, 175, 100, Qt.yellow)
        qp.fillRect(275, 450, 175, 100, Qt.black)
      if(self.isGreen):
        qp.fillRect(100, 450, 350, 100, Qt.green)
      if((self.isBlack) and (self.isGreen)):
        qp.fillRect(100, 450, 175, 100, Qt.black)
        qp.fillRect(275, 450, 175, 100, Qt.green)
      if(self.isRed):
        qp.fillRect(100, 450, 350, 100, Qt.red)
      if((self.isGreen) and (self.isRed)):
        qp.fillRect(100, 450, 175, 100, Qt.green)
        qp.fillRect(275, 450, 175, 100, Qt.red)
      
    qp.end()
    
if __name__ == '__main__':  
  app = QApplication(sys.argv)
  ex = Olympic()
  sys.exit(app.exec_())