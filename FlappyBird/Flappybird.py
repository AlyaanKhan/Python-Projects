import tkinter as tk
import random

class FlappyBirdGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Flappy Bird")
        self.master.geometry("400x400")

        self.canvas = tk.Canvas(master, width=400, height=400, bg="sky blue")
        self.canvas.pack()

        self.bird = self.canvas.create_rectangle(50, 200, 70, 220, fill="yellow")

        self.pipe_width = 50
        self.pipe_gap = 150
        self.pipe_speed = 5
        self.pipe_interval = 1000
        self.pipes = []

        self.score = 0
        self.score_text = self.canvas.create_text(50, 50, text=f"Score: {self.score}", font=("Arial", 16), fill="black")

        self.jump_speed = -10
        self.gravity = 1
        self.jump_pressed = False

        self.master.bind("<space>", self.jump)
        self.master.bind("<Up>", self.jump)

        self.game_over = False
        self.update()

    def update(self):
        if not self.game_over:
            self.move_bird()
            self.move_pipes()
            self.check_collisions()
            self.master.after(20, self.update)

    def move_bird(self):
        if self.jump_pressed:
            self.canvas.move(self.bird, 0, self.jump_speed)
            self.jump_speed += self.gravity
        else:
            self.canvas.move(self.bird, 0, self.gravity)
            self.jump_speed = 0

    def move_pipes(self):
        for pipe in self.pipes:
            self.canvas.move(pipe, -self.pipe_speed, 0)
            if self.canvas.coords(pipe)[2] < 0:
                self.canvas.delete(pipe)
                self.pipes.remove(pipe)
                self.score += 1
                self.canvas.itemconfigure(self.score_text, text=f"Score: {self.score}")

        if len(self.pipes) == 0 or self.canvas.coords(self.pipes[-1])[2] < 400 - self.pipe_interval:
            self.create_pipe()

    def create_pipe(self):
        top_height = random.randint(50, 200)
        bottom_height = 400 - self.pipe_gap - top_height

        top_pipe = self.canvas.create_rectangle(400, 0, 400 + self.pipe_width, top_height, fill="green")
        bottom_pipe = self.canvas.create_rectangle(400, 400 - bottom_height, 400 + self.pipe_width, 400, fill="green")

        self.pipes.append(top_pipe)
        self.pipes.append(bottom_pipe)

    def jump(self, event):
        self.jump_pressed = True
        self.jump_speed = -10

    def check_collisions(self):
        bird_coords = self.canvas.coords(self.bird)
        for pipe in self.pipes:
            pipe_coords = self.canvas.coords(pipe)
            if (bird_coords[0] < pipe_coords[2] and bird_coords[2] > pipe_coords[0] and
                (bird_coords[1] < pipe_coords[3] or bird_coords[3] > pipe_coords[1])):
                self.game_over = True
                self.canvas.create_text(200, 200, text="Game Over!", font=("Arial", 32), fill="red")

def main():
    root = tk.Tk()
    flappy_bird_game = FlappyBirdGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
