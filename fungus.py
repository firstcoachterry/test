from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  robot.drive.reset()
  robot.drive.settings(100)
  robot.drive.drive(-50, 0)
  #await robot.drive.straight(-5)
  #await robot.drive.straight(700, Stop.HOLD)
  #robot.drive.drive(100,0)
  #while True:
    #color = await robot.left_color_sensor.color()
    #print(f"{color=}")
    #if color == Color.WHITE:
      #break
    #wait(10)
  #robot.drive.hold()
  #await robot.drive.turn(-90)
  #await robot.drive.straight(450)


if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))