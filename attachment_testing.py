from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings

async def go(robot: robot_settings.Robot):
  """Use this program to test attachments."""
  robot.drive.reset(0)
  robot.drive.settings(straight_speed=300)
  robot.left_attachment_motor.reset_angle(0)
  robot.right_attachment_motor.reset_angle(0)
  await robot.right_attachment_motor.run_until_stalled(speed=-1000, duty_limit=40)
  await robot.right_attachment_motor.run_angle(speed=100, rotation_angle=30)
  await robot.drive.straight(80)
  await robot.right_attachment_motor.run_angle(speed=100, rotation_angle=95)
  await robot.right_attachment_motor.run_angle(speed=100, rotation_angle=-95)
  await robot.right_attachment_motor.run_angle(speed=1000, rotation_angle=200)
  await robot.right_attachment_motor.run_angle(speed=1000, rotation_angle=-200)
  await robot.drive.straight(50)
  await robot.right_attachment_motor.run_angle(speed=1000, rotation_angle=250)
  await robot.right_attachment_motor.run_angle(speed=1000, rotation_angle=-250)


if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))