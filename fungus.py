from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  """ Runs missions 6, 7, and 11."""
  # TODO: tobykoo - Change normal speed to 300. Don't spend a long time on it.
  robot.drive.reset(0)
  robot.drive.settings(straight_speed=300)
  await robot.drive.straight(-5)
  robot.drive.settings(straight_speed=500)
  await robot.drive.straight(700, Stop.HOLD)
  robot.drive.settings(straight_speed=300)
  await robot.drive_until_color(250, True, False)
  await robot.drive.straight(125)
  await robot.drive.straight(-100)
  await robot.drive.straight(85)
  await robot.drive.straight(-140)  
  await robot.drive.turn(-90)
  await robot.drive.straight(200)
  await robot.drive.turn(45)
  await robot.drive.straight(180)
  await robot.drive.turn(90)
  robot.drive.settings(straight_speed=100)
  await robot.drive.straight(115)
  robot.drive.settings(straight_speed=300)
  await robot.drive.straight(-90)
  await robot.drive.turn(90)
  robot.drive.settings(500)
  await robot.drive.straight(850)

if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))