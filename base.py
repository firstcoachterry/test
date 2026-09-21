from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Side
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import hub_menu, wait


class Robot:
  def __init__(self):
    self.hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
    self.hub.display.orientation(Side.FRONT)

    # Normally, the center button ends the whole program, but this is harmful
    # because we combine all runs in a single program.  We disable the default
    # center button behavior so we can make it cancel the current run without
    # quitting the whole program.
    self.hub.system.set_stop_button(None)

    self.left_sensor = ColorSensor(Port.A)
    self.right_sensor = ColorSensor(Port.B)
    self.left_attachment = Motor(Port.C)
    self.right_attachment = Motor(Port.D)
    self.left_wheel = Motor(Port.E, Direction.COUNTERCLOCKWISE)
    self.right_wheel = Motor(Port.F, Direction.CLOCKWISE)

    self.drive = DriveBase(
        self.left_wheel,
        self.right_wheel,
        wheel_diameter=62.4,  # in mm
        axle_track=135,  # mm between wheel midpoints
    )
    self.drive.use_gyro(True)
