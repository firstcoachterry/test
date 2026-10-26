from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  robot.drive.reset()
  robot.drive.settings(300)
  await robot.drive.straight(-5)
  await robot.drive.straight(85)
  await robot.drive.turn(47.5)
  await robot.drive.straight(330)
  await robot.left_attachment_motor.run_until_stalled(500)
  await robot.drive.straight(-450)




if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))