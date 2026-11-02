from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings

async def go(robot: robot_settings.Robot):
  robot.left_attachment_motor.reset_angle()
  robot.right_attachment_motor.reset_angle()
  await robot.right_attachment_motor.run_until_stalled(-1000)


if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))