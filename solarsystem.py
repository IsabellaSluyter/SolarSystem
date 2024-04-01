import math
import turtle

# Solar System Bodies
class SolarSystemBody(turtle.Turtle):
  min_display_size = 20
  display_log_base = 1.1
  
  def __init__(self, solar_system, mass, position=(0,0), velocity=(0,0)):
    super().__init__()
    self.mass = mass
    self.setposition(position)
    self.velocity = velocity
    self.display_size = max(math.log(self.mass, self.display_log_base), self.min_display_size)

    #removes lines
    self.penup()
    #hides object that draws
    self.hideturtle()

    solar_system.add_body(self)

  def draw(self):
    self.clear()
    self.dot(self.display_size)

  def move(self):
    self.setx(self.xcor() + self.velocity[0])
    self.sety(self.ycor() + self.velocity[1])

class Sun(SolarSystemBody):
  def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(solar_system, mass, position, velocity)
        self.color("yellow")

class Planet(SolarSystemBody):
  ...

# Solar System
class SolarSystem:
  def __init__(self, width, height):
    self.solar_system = turtle.Screen()
    self.solar_system.tracer(0)
    self.solar_system.setup(width, height)
    self.solar_system.bgcolor("black")

    #stores list of bodies present
    self.bodies = [0]
    
  def add_body(self, body):
    self.bodies.append(body)

  def remove_body(self, body):
    self.bodies.remove(body)

  def update_all(self):
      for body in self.bodies:
        body.move()
        body.draw()
      self.solar_system.update()

