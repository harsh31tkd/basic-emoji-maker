import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageDraw
import random


class EmojiMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Emoji Maker")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.face_color = "#ffff00"  # Default Yellow
        self.current_mood = "happy"
        self.draw_emoji()

        # Buttons
        btn_color = tk.Button(root, text="Choose Face Color", command=self.choose_color)
        btn_color.pack(pady=10)

        btn_happy = tk.Button(root, text="Happy Face 😀", command=self.happy_face)
        btn_happy.pack(pady=5)

        btn_sad = tk.Button(root, text="Sad Face 😢", command=self.sad_face)
        btn_sad.pack(pady=5)

        btn_angry = tk.Button(root, text="Angry Face 😠", command=self.angry_face)
        btn_angry.pack(pady=5)

        btn_surprised = tk.Button(root, text="Surprised Face 😮", command=self.surprised_face)
        btn_surprised.pack(pady=5)

        btn_wink = tk.Button(root, text="Wink 😉", command=self.wink_face)
        btn_wink.pack(pady=5)

        btn_random = tk.Button(root, text="Random Face 🎲", command=self.random_face)
        btn_random.pack(pady=5)

        btn_save = tk.Button(root, text="Save Emoji 💾", command=self.save_emoji)
        btn_save.pack(pady=5)

    # --- Face color chooser ---
    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.face_color = color
            self.draw_emoji(self.current_mood)

    # --- Mood Setters ---
    def happy_face(self):
        self.draw_emoji(mood="happy")

    def sad_face(self):
        self.draw_emoji(mood="sad")

    def angry_face(self):
        self.draw_emoji(mood="angry")

    def surprised_face(self):
        self.draw_emoji(mood="surprised")

    def wink_face(self):
        self.draw_emoji(mood="wink")

    def random_face(self):
        mood = random.choice(["happy", "sad", "angry", "surprised", "wink"])
        self.draw_emoji(mood)

    # --- Drawing Function ---
    def draw_emoji(self, mood="happy"):
        self.canvas.delete("all")
        self.current_mood = mood

        # Face
        self.canvas.create_oval(100, 100, 300, 300, fill=self.face_color, outline="black")

        # Eyes
        if mood == "wink":
            self.canvas.create_oval(150, 150, 170, 170, fill="black")
            self.canvas.create_line(230, 160, 250, 160, width=3)  # wink eye
        else:
            self.canvas.create_oval(150, 150, 170, 170, fill="black")
            self.canvas.create_oval(230, 150, 250, 170, fill="black")

        # Mouth
        if mood == "happy":
            self.canvas.create_arc(160, 180, 240, 260, start=0, extent=-180, style=tk.ARC, width=3)
        elif mood == "sad":
            self.canvas.create_arc(160, 220, 240, 260, start=0, extent=180, style=tk.ARC, width=3)
        elif mood == "angry":
            self.canvas.create_arc(160, 220, 240, 260, start=0, extent=180, style=tk.ARC, width=3)
            # Eyebrows
            self.canvas.create_line(145, 145, 170, 140, width=3)
            self.canvas.create_line(230, 140, 255, 145, width=3)
        elif mood == "surprised":
            self.canvas.create_oval(180, 220, 220, 260, outline="black", width=3)  # open mouth
        elif mood == "wink":
            self.canvas.create_arc(160, 200, 240, 260, start=0, extent=-180, style=tk.ARC, width=3)

    # --- Save Emoji as PNG ---
    def save_emoji(self):
        img = Image.new("RGB", (400, 400), "white")
        draw = ImageDraw.Draw(img)

        # Face
        draw.ellipse((100, 100, 300, 300), fill=self.face_color, outline="black")

        # Eyes & Mouth (simplified)
        if self.current_mood == "happy":
            draw.ellipse((150, 150, 170, 170), fill="black")
            draw.ellipse((230, 150, 250, 170), fill="black")
            draw.arc((160, 180, 240, 260), start=0, end=180, fill="black", width=3)
        elif self.current_mood == "sad":
            draw.ellipse((150, 150, 170, 170), fill="black")
            draw.ellipse((230, 150, 250, 170), fill="black")
            draw.arc((160, 220, 240, 260), start=0, end=180, fill="black", width=3)
        elif self.current_mood == "angry":
            draw.ellipse((150, 150, 170, 170), fill="black")
            draw.ellipse((230, 150, 250, 170), fill="black")
            draw.arc((160, 220, 240, 260), start=0, end=180, fill="black", width=3)
            draw.line((145, 145, 170, 140), fill="black", width=3)
            draw.line((230, 140, 255, 145), fill="black", width=3)
        elif self.current_mood == "surprised":
            draw.ellipse((150, 150, 170, 170), fill="black")
            draw.ellipse((230, 150, 250, 170), fill="black")
            draw.ellipse((180, 220, 220, 260), outline="black", width=3)
        elif self.current_mood == "wink":
            draw.ellipse((150, 150, 170, 170), fill="black")
            draw.line((230, 160, 250, 160), fill="black", width=3)
            draw.arc((160, 200, 240, 260), start=0, end=180, fill="black", width=3)

        img.save("emoji.png")
        print("Emoji saved as emoji.png ✅")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmojiMaker(root)
    root.mainloop()
