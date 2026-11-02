from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import run_task, wait

import robot_settings


async def go(robot: robot_settings.Robot):
  """This is just an example to illustrate usage."""
  ### DRIVING ##################################################################
  # For more info on what `robot.drive` can do, go here:
  # https://docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase

  # This resets the robot's measured distance and angle to 0.  You should do
  # this at the start of every mission.
  robot.drive.reset()
  # This sets the default speed, acceleration etc.
  robot.drive.settings(straight_speed=300)

  # Note: Most commands require `await`.  This basically tells the code to wait
  # until the driving, turning, etc. is finished.  Otherwise, the program will
  # jump right to the next command.

  # Drive straight, using the yaw sensor and PID control to maintain heading.
  # Distance is measured in millimeters.  Negative distance drives backwards.
  #
  # There are other arguments, see here:
  # https://docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.straight
  await robot.drive.straight(distance=100)

  # Turn in place tank-style.  Turn is measured in degrees.  Positive angle is
  # right, negative angle is left.
  #
  # There are other arguments, see here:
  # https://docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.turn
  await robot.drive.turn(angle=45)

  # Drive along a curving path, like how a car turns (vs tank).  Can be useful
  # when approaching a tight space or cutting corners.  The radius defines the
  # size of the circle the robot drives on---smaller radius for tighter turns.
  # The angle defines how far to turn.  Positive radius means the robot circles
  # to its right, negative circles to the left.  Positive angle means the robot
  # drives forward, negative angle means the robot drives backwards.
  #
  # There are other arguments, see here:
  # https://docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.arc
  await robot.drive.arc(radius=200, angle=90)

  # Most driving commands have an optional `then` argument that tells the robot
  # what to do at the end.  The default is `Stop.HOLD` which makes robot slow to
  # a stop at the desired distance, and then actively try to stay put.  Another
  # useful setting is `Stop.NONE`, which means the robot continues at full speed
  # without attempting to slow or stop.  This setting is intended for "chaining"
  # movement commands like `straight()` and `arc()`.
  #
  # For example, the following commands drive the robot in a path like a square
  # with rounded corners.  Critically, while chaining `straight()` and `turn()`
  # commands forces the robot to stop at each corner, this will drive smoothly
  # without stopping.
  #
  # Note: You likely still want `Stop.HOLD` on the last driving command, so the
  # robot stops on the mark instead of coasting, which may introduce errors.
  await robot.drive.arc(radius=150, angle=90, then=Stop.NONE)
  await robot.drive.straight(distance=200, then=Stop.NONE)
  await robot.drive.arc(radius=150, angle=90, then=Stop.NONE)
  await robot.drive.straight(distance=200, then=Stop.NONE)
  await robot.drive.arc(radius=150, angle=90, then=Stop.NONE)
  await robot.drive.straight(distance=200, then=Stop.NONE)
  await robot.drive.arc(radius=150, angle=90, then=Stop.NONE)
  await robot.drive.straight(distance=200)  # NB: Defaults to `Stop.HOLD`

  ### ATTACHMENTS ##############################################################
  # Use `robot.left_attachment_motor` and `robot.right_attachment_motor` to
  # control the attachments.  The examples below use the left motor, but the
  # commands apply universally.
  #
  # For more info on controlling attachment motors, see:
  # https://docs.pybricks.com/en/latest/pupdevices/motor.html
  #
  # Turn the left attachment motor by a fixed amount from its current position.
  # The speed is measured in degrees per second.  The angle defines the number
  # of degrees to turn, with sign indicating direction.
  #
  # Note: The speed and angle are defined in terms of motor rotations.  Your
  # attachment will respond in a unique way depending on how its gearbox has
  # been set up.  Use trial and error to understand out how your attachment
  # responds to different speeds and angles.
  #
  # IMPORTANT: By default, the command does *NOT* stop until the requested angle
  # has been reached.  If your attachment gets blocked, the robot will get stuck
  # waiting for the motor to turn.
  #
  # There are other arguments, see here:
  # https://docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run_angle
  await robot.left_attachment_motor.run_angle(speed=100, rotation_angle=90)

  # Turn the left attachment motor at a fixed speed until it stalls.  Note that
  # a "stall" is when the motor is delivering power, but cannot turn---usually
  # because your attachment is blocked.  Can be useful in situations where you
  # want the attachment to move until it is physically stopped.
  #
  # IMPORTANT: This approach has the opposite hazard to `run_angle()` above.  If
  # the attachment never gets blocked, then the robot will be stuck waiting for
  # the motor to get blocked.  Make sure your attachment has a bounded range of
  # motion; e.g.,, the arm eventually hits the floor or the back of the robot.
  #
  # There are other arguments, see here:
  # https://docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run_until_stalled
  await robot.left_attachment_motor.run_until_stalled(speed=100)


if __name__ == "__main__":
  run_task(go(robot_settings.Robot()))