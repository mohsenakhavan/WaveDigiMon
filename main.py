import serial
import tkinter as tk
from threading import Thread
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

SERIAL_PORT = 'COM9'
BAUD_RATE = 115200
MAX_POINTS = 100

data_queue = deque(maxlen=MAX_POINTS)

def read_serial():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
        while True:
            line = ser.readline().decode('utf-8').strip()
            try:
                value = int(line)
                data_queue.append(value)
            except ValueError:
                pass
    except serial.SerialException as e:
        print(f"Serial connection error: {e}")

def update_plot(frame):
    if data_queue:
        ax.clear()
        ax.plot(list(data_queue), label="Sound Level", color="cyan")
        ax.set_ylim(0, 1023)
        ax.set_facecolor("black")
        ax.set_title("Sound Level Chart", color="white")
        ax.set_xlabel("Time", color="white")
        ax.set_ylabel("Sound Level", color="white")
        ax.tick_params(colors="white")
        ax.legend(facecolor="black", edgecolor="white", labelcolor="white")

def create_gui():
    root = tk.Tk()
    root.title("Sound Level Monitor")
    root.configure(bg="black")

    tk.Label(root, text="Terminal Output:", fg="white", bg="black").pack(pady=10)
    terminal = tk.Text(root, height=15, width=50, bg="black", fg="white", insertbackground="white")
    terminal.pack(pady=5)

    def update_terminal():
        if data_queue:
            terminal.insert(tk.END, f"{data_queue[-1]}\n")
            terminal.see(tk.END)
        root.after(100, update_terminal)

    update_terminal()
    root.mainloop()

if __name__ == "__main__":
    serial_thread = Thread(target=read_serial, daemon=True)
    serial_thread.start()

    fig, ax = plt.subplots()
    fig.patch.set_facecolor("black")
    ani = animation.FuncAnimation(fig, update_plot, interval=100, cache_frame_data=False)

    gui_thread = Thread(target=create_gui, daemon=True)
    gui_thread.start()

    plt.show()
