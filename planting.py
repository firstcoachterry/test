from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  """ Runs mission 15"""
  robot.drive.reset(0)
  robot.right_attachment_motor.reset_angle(0)
  robot.drive.settings(straight_speed=(300))
  await robot.drive.straight(260)
  await robot.right_attachment_motor.run_until_stalled(80)
  await robot.drive.turn(3)
  await robot.drive.turn(-6)
  await robot.drive.turn(3)
  robot.drive.settings(straight_speed=(150))
  await robot.right_attachment_motor.run_angle(1,80)
  await robot.drive.straight(-500)
  

if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))
