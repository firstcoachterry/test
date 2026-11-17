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

  async def drive_until_color(self, *, speed: int, left: bool, right: bool, color: Color=Color.WHITE):
    self.drive.settings(turn_acceleration=500)
    """Drives until it sees a color.
    
    Args:
      speed: The speed in mm/s, negative for backwards.
      left: Whether or not to use the left color sensor.
      right: Whether or not to use the right color sensor.
      color: The color the robot stops moving on when it sees it. It defaults 
        to white, so only put in Color.RED or some other color if you don't want
        white.
    """
    self.drive.drive(speed,0)
    while True:
      left_color = await self.left_color_sensor.color() if left else None
      right_color = await self.right_color_sensor.color() if right else None
      print(f"{left_color=}, {right_color=}")
      if left_color == color or right_color == color:
        break
      await wait(10)

  async def drive_until_reflection(self, *, speed: int, left: bool, right: bool, min_reflection: int=-999, max_reflection: int=-998):
    """Drives until it sees a certain amount of total reflection.
    
    Args:
      speed: The speed in mm/s, negative for backwards.
      left: Whether or not to use the left color sensor.
      right: Whether or not to use the right color sensor.
      reflection: The total reflection the robot stops moving on when it sees
        that much reflection. Must be 0-100.
    """
    left_reflection = 0
    right_reflection = 0
    self.drive.drive(speed,0)
    while True:
      if left:
        left_reflection = await self.left_color_sensor.reflection()
        if min_reflection <= left_reflection <= max_reflection:
          break
      if right:
        right_reflection = await self.right_color_sensor.reflection() 
        if min_reflection <= right_reflection <= max_reflection:
          break
      print(f"{left_reflection=}, {right_reflection=}")
      await wait(10)
    self.drive.hold()