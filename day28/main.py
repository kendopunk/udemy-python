import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"

# ---------------------------- VARS ------------------------------- #
num_cycles = 0
countdown_running = False

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
  global countdown_running
  countdown_running = False
  v = '00:00'
  canvas.itemconfig(countdown_value, text = v)

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(timer_string):
  global num_cycles, countdown_running

  if countdown_running:
    parts = [int(x) for x in timer_string.split(":")]
    minutes = parts[0]
    seconds = parts[1]

    if minutes == 0 and seconds == 0:
      new_timer = '00:00'
      num_cycles = num_cycles + 1
      canvas.itemconfig(checks, text = num_cycles * CHECK_MARK)
      countdown_running = False
    elif seconds == 0:
      new_timer = str(minutes - 1).zfill(2) + ':10'
    else:
      new_timer = str(minutes).zfill(2) + ':' + str(seconds - 1).zfill(2)

    canvas.itemconfig(countdown_value, text = new_timer)
    window.after(1000, countdown, new_timer)

def start():
  global countdown_running
  countdown_running = True
  v = str(WORK_MIN) + ':10'
  canvas.itemconfig(countdown_value, text = v)
  countdown(v)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(bg=YELLOW)

# canvas
img = tkinter.PhotoImage(file = "tomato.png")
canvas_width = img.width() * 2
canvas_height = img.height() * 1.5
canvas = tkinter.Canvas(width = canvas_width, height = canvas_height, bg=YELLOW, border=0, highlightthickness=0)

# tomato image
canvas.create_image(canvas_width/2, canvas_height/2, image=img)

# timer / countdown value
countdown_value = canvas.create_text(canvas_width/2, canvas_height/2 + 25, text = "00:00", fill="#fff", font=(FONT_NAME, 35, "bold"))
canvas.grid(column = 2, row=1)

# "Timer" (0, 1)
timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_label.grid(column=2, row=0);

# start button
start_button = tkinter.Button(text="Start", bg=YELLOW, border=0, padx=4, pady=4, highlightthickness=0, command=(start))
start_button.grid(column =0, row = 2)

# reset button
reset_button = tkinter.Button(text = "Reset", bg=YELLOW, border=0, padx=4, pady=4, highlightthickness=0, command=reset)
reset_button.grid(column=3, row=2)

# check marks
checks = canvas.create_text(canvas_width/2, canvas_height - 25, text = "DFD", fill=GREEN, font=(FONT_NAME, 22))
canvas.grid(column=2, row=4)


# always has to be at the bottom of the program
window.mainloop()