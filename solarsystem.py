#solarsystem.py

import math
import turtle

class SolarSystemBody(turtle.Turtle):
  minDisplaySize = 20
  displayLogBase = 1.1
  
  def __init__(self, solarSystem, mass, position=(0,0), velocity=(0,0)):
    super().__init__()
    self.mass = mass
    self.setposition(position)
    self.velocity = velocity
    self.displaySize = max(math.log(self.mass, self.displayLogBase), self.minDisplaySize)

    #removes lines
    self.penup()
    #hides object that draws
    self.hideturtle()

    solarSystem.addBody(self)

  def draw(self):
    self.dot(self.displaySize)

class Sun(SolarSystemBody):
  def __init__(self, solarSystem, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(solarSystem, mass, position, velocity)
        self.color("yellow")

class Planet(SolarSystemBody):
  ...

class SolarSystem:
  def __init__(self, width, height):
    self.solarSystem = turtle.Screen()
    self.solarSystem.tracer(0)
    self.solarSystem.setup(width, height)
    self.solarSystem.bgcolor("black")

    #stores list of bodies present
    self.bodies = [0]
    
  def addBody(self, body):
    self.bodies.append(body)

  def removeBody(self, body):
    self.bodies.remove(body)

