#solarsystem.py

import turtle

class SolarSystemBody(turtle.Turtle):
  ...

class Sun(SolarSystemBody):
  ...

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

