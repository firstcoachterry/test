from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  """Addresses Mission 3."""
  robot.drive.reset()
  robot.drive.settings(300)
  await robot.drive.straight(260)
  await robot.drive.straight(-300)


if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))