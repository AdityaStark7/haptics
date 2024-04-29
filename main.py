import tkinter as tk
from PIL import Image, ImageTk
import pygame

class HapticTextureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("HapticTexture Moderator")
        self.master.geometry("600x400")

        # Initialize pygame
        pygame.mixer.init()

        self.current_texture = tk.StringVar()
        self.current_texture.set("")

        # Load background image
        self.bg_image = Image.open("haptics.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Load texture images
        self.water_image = Image.open("water_img.jpg")
        self.concrete_image = Image.open("concrete_image.jpg")
        self.water_photo = ImageTk.PhotoImage(self.water_image.resize((150, 150)))
        self.concrete_photo = ImageTk.PhotoImage(self.concrete_image.resize((150, 150)))

        # Load sound effects
        self.water_sound = pygame.mixer.Sound("glass-filled-with-water-201638.mp3")
        self.concrete_sound = pygame.mixer.Sound("brick-falling-100572.mp3")

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Create a Canvas widget to draw background image and text overlays
        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.pack()

        # Draw background image with "Get Started" button
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)
        self.start_button = tk.Button(self.master, text="Get Started", command=self.show_texture_selection, font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", relief=tk.FLAT)
        self.canvas.create_window(300, 300, window=self.start_button)

        # Haptics screen buttons
        self.haptics_button = tk.Button(self.master, text="Feel Texture", command=self.use_haptics, font=("Arial", 14, "bold"), bg="#FF5733", fg="white", relief=tk.FLAT)
        self.back_button = tk.Button(self.master, text="Back to Texture Selection", command=self.show_texture_selection, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", relief=tk.FLAT)

    def show_texture_selection(self):
        # Clear canvas
        self.canvas.delete("all")

        # Draw texture selection screen with images and buttons
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)

        # Water texture
        self.water_button = tk.Button(self.master, image=self.water_photo, command=lambda: self.select_texture("Water"), relief=tk.FLAT)
        self.canvas.create_window(200, 250, window=self.water_button)

        # Concrete texture
        self.concrete_button = tk.Button(self.master, image=self.concrete_photo, command=lambda: self.select_texture("Concrete"), relief=tk.FLAT)
        self.canvas.create_window(400, 250, window=self.concrete_button)

    def select_texture(self, texture):
        self.current_texture.set("Current Texture: " + texture)
        if texture == "Water":
            self.water_sound.play()
        elif texture == "Concrete":
            self.concrete_sound.play()
        self.show_haptics_screen()

    def show_haptics_screen(self):
        # Clear canvas
        self.canvas.delete("all")

        # Display current texture and haptics buttons
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)
        self.canvas.create_text(300, 150, text=self.current_texture.get(), font=("Arial", 20), fill="white")
        self.canvas.create_window(300, 300, window=self.haptics_button)
        self.canvas.create_window(300, 350, window=self.back_button)

    def use_haptics(self):
        # Placeholder function for haptics feedback
        pass

def main():
    root = tk.Tk()
    app = HapticTextureApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

