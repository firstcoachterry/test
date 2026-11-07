from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait, multitask

import robot_settings


async def go(robot: robot_settings.Robot):
  """Runs missions 5, 8, and 9"""
  robot.drive.reset(0)
  robot.drive.settings(straight_speed=300)
  robot.left_attachment_motor.reset_angle(0)
  robot.right_attachment_motor.reset_angle(0)
  robot.left_attachment_motor.run_until_stalled(-500)
  await robot.drive.straight(-5)
  robot.drive.settings(straight_speed=500)
  robot.left_attachment_motor.run_until_stalled(400)
  await robot.drive.straight(840)
  robot.drive.settings(straight_speed=300)
  await robot.drive.turn(90)
  await robot.left_attachment_motor.run_until_stalled(-1000)


if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))