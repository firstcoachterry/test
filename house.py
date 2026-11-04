from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  """ Runs mission 15"""
  robot.drive.reset(0)
  robot.left_attachment_motor.reset_angle(0)
  robot.drive.settings(straight_speed=300)
  robot.left_attachment_motor.run_until_stalled(-250)
  await robot.drive.straight(-5)
  await robot.drive.straight(100)
  await robot.drive.turn(58)
  robot.drive.settings(straight_speed=500)
  await robot.drive.straight(450)
  robot.drive.settings(straight_speed=300)
  await robot.drive.turn(32)
  await robot.drive.straight(460)
  await robot.drive.turn(-90)
  await robot.drive.straight(200)
  await robot.drive.turn(-90)
  await robot.drive.straight(100)
  await robot.left_attachment_motor.run_until_stalled(250)
  await robot.drive.straight(-75)
  await robot.drive.turn(45)
  robot.drive.settings(straight_speed=500)
  await robot.drive.straight(-750)

if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))