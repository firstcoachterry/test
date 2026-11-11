from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  robot.drive.reset()
  robot.drive.settings(300)
  await robot.drive.straight(725, Stop.HOLD)
  robot.drive.settings(straight_speed=250)
  await robot.drive_until_color(250, True, False)
  await robot.drive.turn(angle=30)
  await robot.drive.straight(145)
  await robot.right_attachment_motor.run_angle(speed=700, rotation_angle=-200)
  await robot.right_attachment_motor.run_angle(speed=700, rotation_angle=200)
  await robot.drive.straight(-200)
  await robot.left_attachment_motor.run_angle(speed=700, rotation_angle=-300)
  await robot.drive.turn(angle=50)
  await robot.drive.straight(100)
  await robot.left_attachment_motor.run_angle(speed=150, rotation_angle=75)
  await robot.drive.turn(25)
  await robot.left_attachment_motor.run_angle(speed=700, rotation_angle=-200)
  await robot.drive.straight(-80)
  await robot.drive.turn(angle=90)
  await robot.drive.straight(600)
  return
  await robot.drive.straight(-135)
  await robot.drive.turn(angle=-30)
  await robot.drive.straight(-725)
  await robot.right_attachment_motor.run_angle(speed=700, rotation_angle=--200)
  #await robot.drive.straight()




if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))