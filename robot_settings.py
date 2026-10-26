from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port, Side
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import hub_menu, wait

class Robot:
  def __init__(self):
    self.hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
    self.hub.display.orientation(Side.FRONT)

    # Makes the center button no longer cancel the whole code, which is useful
    # because we don't want to restart the whole program every single run.
    # Otherwise, the center button would stop the whoe program. This is bad, as
    # all of the runs are on 1 program.
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
  async def drive_until_color(self, speed: int, sensor: str, color: Color=Color.WHITE):
    # Put a number for speed in mm per second, positive for forwards, negative
    # for backwards.
    # Put "left", "right", or "both" in sensor.
    # Put in a color if you don't want white.
    self.drive.drive(speed,0)
    if sensor == "left":
      left_color = await self.left_color_sensor.color()
      right_color = None
    elif sensor == "right":
      left_color = None
      right_color = await self.right_color_sensor.color()
    else:
      left_color = await self.left_color_sensor.color()
      right_color = await self.right_color_sensor.color()
    while True:
      print(f"{left_color=}, {right_color=}")
      if left_color == color or right_color == color:
        break
      wait(10)
    self.drive.hold()