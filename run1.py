from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import base


async def go(robot: base.Robot):
  robot.hub.light.on(Color.RED)
  robot.drive.reset()
  await robot.drive.straight(300)
  await robot.drive.turn(90)
  await robot.drive.straight(300)
  await robot.drive.turn(90)
  await robot.drive.straight(300)
  await robot.drive.turn(90)
  await robot.drive.straight(300)
  await robot.drive.turn(90)


if __name__ == "__main__":
  run_task(go(base.Robot()))