from solarsystem import SolarSystem, Sun

solar_system = SolarSystem(width=1400, height=900)

sun = Sun(solar_system, mass=10_000, velocity=(2, 1))

while True:
  solar_system.update_all()
