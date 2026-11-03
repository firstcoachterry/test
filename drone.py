from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  # Copied from `fungus.py`, please replace.
  robot.drive.reset(0)
  robot.drive.settings(300)
  await robot.drive.straight(500)
  await robot.drive.arc(-600, angle=25, then=Stop.HOLD, wait=True)
  await robot.drive.straight(-50)
  await robot.drive.turn(-25)
  await robot.drive.straight(-20)
  await robot.drive.turn(45)
  robot.drive.settings(600)
  await robot.drive.straight(-700)

#   await robot.drive.straight(700, Stop.HOLD)
#   await robot.drive_until_white(1)
#   await robot.drive.straight(125)
#   await robot.drive.straight(-100)
#   await robot.drive.straight(85)
#   await robot.drive.straight(-140)  
#   await robot.drive.turn(-90)
#   await robot.drive.straight(200)
#   await robot.drive.turn(45)
#   await robot.drive.straight(180)
#   await robot.drive.turn(90)
#   robot.drive.settings(straight_speed=100)
#   await robot.drive.straight(115)
#   robot.drive.settings(straight_speed=250)
#   await robot.drive.straight(-90)
#   await robot.drive.turn(90)
#   robot.drive.settings(500)
#   await robot.drive.straight(850)

if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))