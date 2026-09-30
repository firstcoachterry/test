from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import hub_menu, multitask, run_task, wait

import robot_settings
# Add new runs here with import
import fungus


async def exit(robot: robot_settings.Robot):
  "Stops the program and exits it"
  exit()

# Add new runs here with the program to run
MISSION_RUNS = [
    exit,
    fungus.go
]


def run_select(run_number: int) -> int | None:
  """Returns the next run, even if `run_number` was stopped before finishing
  for convenience.
  
  Drivers only need to use the arrow keys to redo a past run
  or skip runs. Runs are numbered, and "X" is the program that exits the main
  program.

  Args:
    run_number: Run that just finished, or 0 at the start of the program
  
  Returns:
    The next run, or None to end the program
  """

  # Fills up the menu slots with the runs starting at the next run.
  number_of_runs = len(MISSION_RUNS)
  run_number = (run_number + 1) % number_of_runs # advances to the next run
  run_options = []
  for _ in range(number_of_runs):
    run_options.append("X" if run_number == 0 else str(run_number))
    run_number = (run_number + 1) % number_of_runs

  # Reuse normal menu selection programs.
  selected_run = hub_menu(*run_options)
  return None if selected_run == "X" else int(selected_run)

async def datalog(robot: robot_settings.Robot):
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
  because `multitask(...race=True)` stops all other programs in the parenthesis
  when any of them return.

  Args:
    robot: Robot whose button (Any button) should be pressed,
  """
  while not robot.hub.buttons.pressed():  # Waits for any button to be pressed.
    await wait(10)
  while robot.hub.buttons.pressed():  # Now waits for the button pressed to be
    #released.
    await wait(10)


def main(robot=robot_settings.Robot):
  "Runs a menu over all runs in `MISSION_RUNS`"
  
  run_number = 0  # Starting run number
  while True:
    run_number = run_select(run_number)
    if run_number is None:
      break
    run_task(
      multitask(
        MISSION_RUNS[run_number](robot),
        datalog(robot),
        cancel_current_run(robot),
        race=True  # Cancels monitoring when finished.
      ),
    )


if __name__ == "__main__":
  main()