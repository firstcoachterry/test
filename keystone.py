from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  robot.drive.reset()
  robot.drive.settings(400)
  await robot.drive.straight(725, Stop.HOLD)
  robot.drive.settings(straight_speed=250)
  await robot.drive_until_color(250, True, False)
  await robot.drive.turn(angle=30)
  await robot.drive.straight(145)
  await robot.right_attachment_motor.run_angle(speed=700, rotation_angle=-200)
  await robot.right_attachment_motor.run_angle(speed=700, rotation_angle=200)
  await robot.drive.straight(-220)
  await robot.left_attachment_motor.run_angle(speed=700, rotation_angle=-270)
  await robot.drive.turn(angle=55)
  await robot.drive.straight(155)
  await robot.left_attachment_motor.run_angle(speed=125, rotation_angle=85)
  await robot.drive.turn(18)
  await robot.left_attachment_motor.run_angle(speed=700, rotation_angle=-200)
  await robot.drive.straight(-115)
  await robot.drive.turn(angle=70)
  robot.drive.settings(800)
  await robot.drive.straight(600)
  return
  await robot.drive.straight(-135)
  await robot.drive.turn(angle=-30)
  robot.drive.settings(straight_speed=500)
  await robot.drive.straight(-725)
  await robot.right_attachment_motor.run_angle(speed=700, rotation_angle=--200)
  #await robot.drive.straight()




if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))