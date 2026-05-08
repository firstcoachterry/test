from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Color, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import hub_menu, multitask, run_task, wait

import base
import run1
import run2
import run3


async def quit(robot: base.Robot):
  """Stops the program.
  
  Args:
    robot: Ignored, present for API compatibility with other run functions.
  """
  exit()


RUNS = [
    quit,
    run1.go,
    run2.go,
    run3.go,
]


def select_run(run_id: int | None) -> int | None:
  """Returns the next selected run, assuming `run_id` just finished.

  If there are 3 runs, this will present the menu options [1, 2, 3, Q], where
  Q quits the program.  The menu can be cycled using the arrow keys to select
  any option.  For convenience, the default selection is set to the run after
  `run_id` so drivers only have to push the main button to advance.

  Args:
    run_id: Run number that just finished (e.g., 1, 2, 3) or None at start.

  Returns:
    Selected run number, or None to stop.
  """
  run_id = 0 if run_id is None else run_id

  # Fill the menu options with the cycle starting at the next run.
  run_id = (run_id + 1) % len(RUNS)  # advance to the next run
  menu_options = []
  for _ in range(len(RUNS)):
    menu_options.append("Q" if run_id == 0 else str(run_id))

    # Subtract to run the cycle backwards, because with the hub sideways the up
    # arrow is actually the left (i.e., back) arrow.
    run_id = (run_id - 1) % len(RUNS)

  # Reuse the standard menu selection routine.
  selection = hub_menu(*menu_options)
  return None if selection == "Q" else int(selection)


async def monitor(robot: base.Robot):
  """Continuously prints sensor values to stdout.

  Prints using the "plot:" format that BlocklyPy Commander uses, so sensor
  readings can be plotted in the extension.  Never stops monitoring, since
  `multitask(..., race=True)` will stop all parallel tasks when any of them
  stop (e.g., when the actual robot run stops).
  
  Args:
    robot: Robot to gather sensor values from.,
  """
  # This `plot:` format is load-bearing for BlocklyPy Commander.
  print(f"plot: start Angle,Distance")
  while True:
    print(f"plot: {robot.drive.angle()},{robot.drive.distance()}")
    await wait(50)


async def cancel(robot: base.Robot):
  """Waits for a button press.

  This function simply returns upon the first button press, which cancels the
  current run because `multitask(..., race=True)` stops all other coroutines
  once any of them returns.
  
  Args:
    robot: Robot whose button should be pressed.
  """
  while not robot.hub.buttons.pressed():  # wait for any button to be pressed
    await wait(10)
  while robot.hub.buttons.pressed():  # now wait for them to be released
    await wait(10)


def main():
  """Runs a menu over all available runs."""
  robot = base.Robot()

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

  run_id = None  # dummy run ID at start
  while True:
    run_id = select_run(run_id)
    if run_id is None:
      break
    run_task(
        multitask(
            RUNS[run_id](robot),
            monitor(robot),
            cancel(robot),
            race=True,  # cancel monitoring when run finishes
        ),
    )


if __name__ == "__main__":
  main()