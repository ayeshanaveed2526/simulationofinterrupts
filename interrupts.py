from gui import update_gui_log
from scheduler import run_scheduler

interrupt_queue = []
def timer_isr():
    update_gui_log(" [TIMER] Timer Interrupt Received")
    run_scheduler()

def keyboard_isr():
    update_gui_log(" [KEYBOARD] Keyboard Interrupt Received")
    run_scheduler()

IVT ={
    0: timer_isr,
    1: keyboard_isr
}

def raise_interrupt(interrupt_id):
    interrupt_queue.append(interrupt_id)
    update_gui_log(f"Interrupt {interrupt_id} raised")


def handle_interrupts():
    if interrupt_queue:
        intr = interrupt_queue.pop(0)
        IVT[intr]()