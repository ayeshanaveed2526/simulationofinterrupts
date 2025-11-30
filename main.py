# # main.py

# from interrupts import raise_interrupt, handle_interrupts
# from scheduler import run_scheduler
# from gui import start_gui_loop, update_gui_log, update_process_table
# import random


# def update_every_tick():
#     update_process_table()
#     run_scheduler()

#     # random interrupt trigger
#     intr = random.choice([None, 0, 1])
#     if intr is not None:
#         raise_interrupt(intr)

#     handle_interrupts()


# if __name__ == "__main__":
#     update_gui_log("Starting OS Interrupt Simulator...")
#     start_gui_loop(update_every_tick)
