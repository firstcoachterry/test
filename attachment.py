from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import base

async def go(robot: base.Robot):
    robot.left_attachment.reset_angle()
    robot.right_attachment.reset_angle()
    await robot.left_attachment.run_target(500, 720)
    await robot.right_attachment.run_target(500, 720)
    await robot.left_attachment.run_target(500, -720)
    await robot.right_attachment.run_target(500, -720)


if __name__ == "__main__":
  run_task(go(base.Robot()))