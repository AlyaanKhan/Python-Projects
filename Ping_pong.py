import tkinter as tk
import random
import time

class PingPong:
    def __init__(self, master):
        self.master = master
        self.master.title("Ping Pong")
        self.master.geometry("600x400")
        self.canvas = tk.Canvas(master, width=600, height=400, bg="black")
        self.canvas.pack()

        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill="white")
        self.paddle_left = self.canvas.create_rectangle(50, 150, 70, 250, fill="white")
        self.paddle_right = self.canvas.create_rectangle(530, 150, 550, 250, fill="white")

        self.ball_dx = 2
        self.ball_dy = 2

        self.master.bind("<KeyPress-Up>", self.move_paddle_up)
        self.master.bind("<KeyPress-Down>", self.move_paddle_down)

        self.update()

    def update(self):
        self.move_ball()
        self.check_collisions()
        self.master.after(10, self.update)

    def move_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
    
    def check_collisions(self):
        ball_coords = self.canvas.coords(self.ball)
        paddle_left_coords = self.canvas.coords(self.paddle_left)
        paddle_right_coords = self.canvas.coords(self.paddle_right)

        if ball_coords[0] <= 0 or ball_coords[2] >= 600:
            self.ball_dx *= -1

        if ball_coords[1] <= 0 or ball_coords[3] >= 400:
            self.ball_dy *= -1

        if ball_coords[0] <= paddle_left_coords[2] and paddle_left_coords[1] <= ball_coords[1] <= paddle_left_coords[3]:
            self.ball_dx *= -1

        if ball_coords[2] >= paddle_right_coords[0] and paddle_right_coords[1] <= ball_coords[1] <= paddle_right_coords[3]:
            self.ball_dx *= -1

    def move_paddle_up(self, event):
        paddle_left_coords = self.canvas.coords(self.paddle_left)
        if paddle_left_coords[1] > 0:
            self.canvas.move(self.paddle_left, 0, -20)

    def move_paddle_down(self, event):
        paddle_left_coords = self.canvas.coords(self.paddle_left)
        if paddle_left_coords[3] < 400:
            self.canvas.move(self.paddle_left, 0, 20)

def main():
    root = tk.Tk()
    ping_pong = PingPong(root)
    root.mainloop()

if __name__ == "__main__":
    main()
