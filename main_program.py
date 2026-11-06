from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import hub_menu, multitask, run_task, wait

import robot_settings
# Add new runs here with import
import rock
import house
import seeds
import tree_and_roots
import drone
import fungus


async def exit(robot: robot_settings.Robot):
  """Stops the program and exits it.
  
  Args:
    robot: Robot for compatibility
  """
  exit()

# Add new runs here with the program to run
RUNS = [
  exit,
  rock.go,
  seeds.go,
  tree_and_roots.go,
  drone.go,
  house.go,
  fungus.go
]


def run_select(run_number: int | None) -> int | None:
  """Returns the next run, even if `run_number` was stopped before finishing
  for convenience.
  
  Drivers only need to use the arrow keys to redo a past run
  or skip runs. Runs are numbered, and "X" is the program that exits the main
  program.

  Args:
    run_number: Run that just finished, or None at the start of the program
  
  Returns:
    The next run, or None to end the program
  """

  # Fills up the menu slots with the runs starting at the next run.
  run_number = 0 if run_number is None else run_number
  number_of_runs = len(RUNS)
  run_number = (run_number + 1) % number_of_runs # advances to the next run
  run_options = []
  for _ in range(number_of_runs):
    run_options.append("X" if run_number == 0 else str(run_number))
    run_number = (run_number + 1) % number_of_runs

  # Reuse normal menu selection programs.
  selected_run = hub_menu(*run_options)
  return None if selected_run == "X" else int(selected_run)

async def graph(robot: robot_settings.Robot):
  """Prints distance moved and current angle to the datalog tab below

  Prints data as a graph in the "plot:" format that is used by BlocklyPy
  Commander. Never stops montioring the data until the main program ends
  (Not a run).

  Args:
    robot: Robot to get data from.
  """
  print(f"plot: start Angle,Distance")
  while True:
    print(f"plot: {robot.drive.angle()},{robot.drive.distance()}")
    await wait(50)


async def cancel_current_run(robot: robot_settings.Robot):
  """Waits for a button press to cancel a program.

  This function returns on a button press, which cancels the current run
  because `multitask(..., race=True)` stops all other programs in the
  parenthesis when any of them return.

  Args:
    robot: Robot whose button (Any button) should be pressed,
  """
  while not robot.hub.buttons.pressed():  # Waits for any button to be pressed.
    await wait(10)
  while robot.hub.buttons.pressed():  # Now waits for the button to be released.
    await wait(10)


def main():
  "Runs a menu over all runs in `RUNS`"
  robot = robot_settings.Robot()
  # Fun rainbow lights.
  for i in range(360):
    if i < 180:
      value = i
    elif i >= 260:
      value = 360 - i
    else:
      value = 100
    robot.hub.light.on(Color(h=(i * 5) % 360, s=100, v=value))
    wait(5)
  
  run_number = None  # Starting dummy run number.
  while True:
    run_number = run_select(run_number)
    if run_number is None:
      break
    run_task(
      multitask(
        RUNS[run_number](robot),
        graph(robot),
        cancel_current_run(robot),
        race=True  # Cancels monitoring when finished.
      ),
    )
    # Prevent the robot from trying to hold its yaw angle between runs.
    robot.drive.stop()


if __name__ == "__main__":
  main()