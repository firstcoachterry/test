from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings

async def go(robot: robot_settings.Robot):
  """Use this program to test driving sequences."""
  robot.drive.reset(0)
  robot.drive.settings(straight_speed=250)
  await robot.drive.arc(radius=10, angle=90, then=Stop.NONE)
  await robot.drive.straight(2000)
  await robot.drive.arc(radius=10, angle=180, then=Stop.NONE)
  await robot.drive.straight(2000)
  await robot.drive.arc(radius=-10, angle=90)

if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))