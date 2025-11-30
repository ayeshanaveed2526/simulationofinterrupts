
from interrupts import raise_interrupt, handle_interrupts
from scheduler import run_scheduler
from gui import start_gui_loop, update_gui_log, update_process_table
import random


def update_every_tick():
    update_process_table()
    run_scheduler()

    # Only timer interrupts are raised automatically.
    # Keyboard interrupts are raised manually by the user via the GUI key binding.
    intr = random.choice([None, 0])  # 0 = timer
    if intr is not None:
        raise_interrupt(intr)

    handle_interrupts()


if __name__ == "__main__":
    update_gui_log("Starting OS Interrupt Simulator...")
    # Pass a keyboard callback that raises keyboard interrupt (id=1) when any key
    # is pressed in the GUI window.
    start_gui_loop(update_every_tick, keyboard_callback=lambda: raise_interrupt(1))
