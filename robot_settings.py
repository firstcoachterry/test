from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Side
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import hub_menu, wait

class Robot:
  def __init__(self):
    self.hub = PrimeHub(Axis.Z, Axis.Y)
    self.hub.display.orientation(Side.FRONT)
    # Makes the center button no longer cancel the whole code.
    self.hub.system.set_stop_button(None)
    # Setting all the devices.
    self.left_color_sensor = ColorSensor(Port.A)
    self.right_color_sensor = ColorSensor(Port.B)
    self.left_attachment_motor = Motor(Port.C)
    self.right_attachment_motor = Motor(Port.D)
    self.left_drive_wheel = Motor(Port.E, Direction.COUNTERCLOCKWISE)
    self.right_drive_wheel = Motor(Port.F, Direction.CLOCKWISE)

    # Sets the drive method.
    self.drive = DriveBase(
      self.left_drive_wheel,
      self.right_drive_wheel,
      wheel_diameter=62.4,
      axle_track=135
    )
    self.drive.use_gyro(True)
    self.drive.settings(turn_acceleration=500)