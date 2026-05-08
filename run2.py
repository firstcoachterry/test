from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import base


async def go(robot: base.Robot):
  robot.hub.light.on(Color.GREEN)
  robot.drive.reset()
  await robot.drive.straight(100, then=Stop.NONE)
  await robot.drive.curve(100, 90, then=Stop.NONE)
  await robot.drive.straight(100, then=Stop.NONE)
  await robot.drive.curve(100, 90, then=Stop.NONE)
  await robot.drive.straight(100, then=Stop.NONE)
  await robot.drive.curve(100, 90, then=Stop.NONE)
  await robot.drive.straight(100, then=Stop.NONE)
  await robot.drive.curve(100, 90)


if __name__ == "__main__":
  run_task(go(base.Robot()))