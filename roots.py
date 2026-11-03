from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  """Addresses Mission 3.b"""
  robot.drive.reset()
  robot.drive.settings(300)
  await robot.drive.straight(distance=500)
  await robot.drive.turn(angle=-7)
  await robot.drive.straight(distance=330)
  await robot.drive.turn(angle=29)
  await robot.right_attachment_motor.run_until_stalled(500)


if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))