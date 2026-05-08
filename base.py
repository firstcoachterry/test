from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Side
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import hub_menu, wait


class Robot:
  def __init__(self):
    self.hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
    self.hub.display.orientation(Side.LEFT)
    self.left_wheel = Motor(
        Port.E,
        positive_direction=Direction.COUNTERCLOCKWISE,
    )
    self.right_wheel = Motor(
        Port.D,
        positive_direction=Direction.CLOCKWISE,
    )
    self.drive = DriveBase(
        self.left_wheel,
        self.right_wheel,
        wheel_diameter=62.4,
        axle_track=87,  # distance between wheel midpoints
    )
    self.drive.use_gyro(True)

    self.left_attachment = Motor(Port.F)
    self.right_attachment = Motor(Port.B)