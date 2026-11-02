from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  """ Runs mission 15"""
  # TODO: tobykoo - Add 'arc' to make the run smoother.
  robot.drive.reset(0)
  robot.left_attachment_motor.reset_angle(0)
  robot.drive.settings(straight_speed=250)
  # FIXME: tobykoo - Remove await to run in parallel.
  await robot.left_attachment_motor.run_until_stalled(-250)
  await robot.drive.straight(-5)
  await robot.drive.straight(300)
  await robot.drive.turn(90)
  await robot.drive.straight(465)
  await robot.drive.turn(-90)
  await robot.drive.straight(330)
  await robot.drive.turn(90)
  await robot.drive.straight(115)
  await robot.drive.straight(-115)
  await robot.drive.turn(90)
  await robot.drive.straight(290)
  await robot.drive.turn(-90)
  await robot.drive.straight(410)
  await robot.drive.turn(-90)
  await robot.drive.straight(190)
  await robot.drive.turn(-90)
  await robot.drive.straight(75)
  await robot.left_attachment_motor.run_until_stalled(250)
  await robot.drive.straight(-75)
  await robot.drive.turn(45)
  robot.drive.settings(straight_speed=500)
  await robot.drive.straight(-750)

if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))