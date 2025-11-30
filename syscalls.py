

from gui import update_gui_log
from scheduler import run_scheduler

def sys_write(text):
    update_gui_log(f"[SYSCALL WRITE] {text}")


def sys_exit():
    update_gui_log("[SYSCALL EXIT] Process ended")
    run_scheduler()


syscalls = {
    1: lambda: sys_write("Hello from process"),
    2: sys_exit
}
