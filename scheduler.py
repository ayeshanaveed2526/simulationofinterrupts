from processes import get_current_process, save_context, switch_process
from gui import update_gui_log, update_process_table

def run_scheduler():
    p = get_current_process()
    update_gui_log(f"Running Process {p['pid']}")

    save_context()
    update_process_table()

    switch_process()
    update_gui_log("Context switch completed")
    update_process_table()