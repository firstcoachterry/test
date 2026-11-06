from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  """ Runs missions 6, 7, and 11."""
  robot.drive.reset(0)
  robot.drive.settings(straight_speed=300)
  await robot.drive.straight(125)
  await robot.drive.straight(850)

if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))