import tkinter as tk

WIDTH = 900
HEIGHT = 500

root = tk.Tk()
root.title("Koax kábel animáció")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# --------------------
# TV
# --------------------

canvas.create_rectangle(450, 120, 800, 340, fill="black", outline="gray", width=4)
canvas.create_rectangle(470, 140, 780, 320, fill="#3da8ff", outline="")

canvas.create_text(
    625,
    230,
    text="TV",
    fill="white",
    font=("Arial", 40, "bold")
)

# TV talp
canvas.create_rectangle(610, 340, 640, 375, fill="gray20")
canvas.create_rectangle(570, 375, 680, 385, fill="gray30")

# Koax csatlakozó
connector_x = 450
connector_y = 240

canvas.create_oval(
    connector_x - 6,
    connector_y - 6,
    connector_x + 6,
    connector_y + 6,
    fill="gold",
    outline="black"
)

# Kábel vége pozíció
plug_x = connector_x
plug_y = connector_y

direction = -1
speed = 3

MAX_DISTANCE = 250

# kábel és dugó
cable = canvas.create_line(
    120,
    connector_y,
    plug_x,
    plug_y,
    width=8,
    fill="black",
    smooth=True
)

plug = canvas.create_rectangle(
    plug_x - 12,
    plug_y - 7,
    plug_x + 12,
    plug_y + 7,
    fill="silver",
    outline="black"
)

pin = canvas.create_line(
    plug_x + 12,
    plug_y,
    plug_x + 22,
    plug_y,
    fill="gold",
    width=3
)


def update():
    global plug_x, direction

    plug_x += direction * speed

    if plug_x <= connector_x - MAX_DISTANCE:
        direction = 1

    if plug_x >= connector_x:
        direction = -1

    # kábel
    canvas.coords(
        cable,
        120,
        connector_y,
        (120 + plug_x) / 2,
        connector_y + 30,
        plug_x,
        plug_y
    )

    # dugó
    canvas.coords(
        plug,
        plug_x - 12,
        plug_y - 7,
        plug_x + 12,
        plug_y + 7
    )

    # középső ér
    canvas.coords(
        pin,
        plug_x + 12,
        plug_y,
        plug_x + 22,
        plug_y
    )

    root.after(20, update)


update()
root.mainloop()