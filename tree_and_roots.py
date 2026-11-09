from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait, multitask

import robot_settings


async def go(robot: robot_settings.Robot):
  """Runs missions 5, 8, and 9
  
  Temporarily a dummy run.
  """
  robot.drive.reset(0)
  robot.drive.settings(straight_speed=300)
  robot.left_attachment_motor.reset_angle(0)
  robot.right_attachment_motor.reset_angle(0)
  robot.right_attachment_motor.run_until_stalled(speed=-500, duty_limit=40)
  await robot.drive.straight(-5)
  robot.drive.settings(straight_speed=500)
  await robot.drive.straight(100)
  await robot.drive.turn(-10)
  await robot.drive.straight(300)
  await robot.drive.turn(10)
  await robot.drive.straight(410)
  robot.drive.settings(straight_speed=300)
  await robot.right_attachment_motor.run_angle(speed=100, rotation_angle=35)
  await robot.right_attachment_motor.run_angle(speed=100, rotation_angle=100)
  await robot.right_attachment_motor.run_angle(speed=100, rotation_angle=-100)
  await robot.right_attachment_motor.run_angle(speed=1000, rotation_angle=200)
  await robot.right_attachment_motor.run_angle(speed=1000, rotation_angle=-200)
  await robot.drive.straight(40)
  await robot.right_attachment_motor.run_angle(speed=1000, rotation_angle=250)
  await robot.right_attachment_motor.run_angle(speed=1000, rotation_angle=-200)
  await robot.drive.straight(-100)
  await robot.drive.turn(90)
  await robot.drive.straight(290)
  await robot.drive.turn(-90)
  await robot.drive.straight(35)
  await robot.left_attachment_motor.run_angle(speed=1000, rotation_angle=-7200)
  await robot.drive.straight(-20)
  await robot.drive.turn(45)
  robot.drive.settings(straight_speed=500)
  robot.right_attachment_motor.run_angle(speed=1000, rotation_angle=250)
  robot.left_attachment_motor.run_angle(speed=1000, rotation_angle=7200)
  await robot.drive.straight(-900)


if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))