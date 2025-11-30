import tkinter as tk
from processes import processes, get_current_process
root = tk.Tk()
root.title("OS Interrupt Simulator")


log_box = tk.Text(root, height=15, width=60)
log_box.grid(row=0, column=0, padx=10, pady=10)

process_table = tk.Text(root, height=10, width=60)
process_table.grid(row=1, column=0, padx=10, pady=10)


def update_gui_log(msg):
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)


def update_process_table():
    process_table.delete(1.0, tk.END)
    process_table.insert(tk.END, "PID | PC | ACC | STATE\n")
    process_table.insert(tk.END, "-" * 30 + "\n")
    for p in processes:
        process_table.insert(
            tk.END,
            f"{p['pid']}   | {p['pc']}  | {p['acc']}   | {p['state']}\n"
        )


def start_gui_loop(update_func):
    def loop():
        update_func()
        root.after(1000, loop)

    loop()
    root.mainloop()