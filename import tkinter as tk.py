import tkinter as tk

class HapticTextureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("HapticTexture Moderator")

        self.current_texture = tk.StringVar()
        self.current_texture.set("")

        self.create_widgets()

    def create_widgets(self):
        # Screen 1: Start
        self.start_label = tk.Label(self.master, text="Welcome to HapticTexture Moderator!")
        self.start_label.pack()

        self.start_button = tk.Button(self.master, text="Get Started", command=self.show_texture_selection)
        self.start_button.pack()

        # Screen 2: Choose Texture
        self.texture_label = tk.Label(self.master, text="Select the texture you want to experience:")
        self.water_button = tk.Button(self.master, text="Water", command=lambda: self.select_texture("Water"))
        self.concrete_button = tk.Button(self.master, text="Concrete", command=lambda: self.select_texture("Concrete"))
        
        # Screen 3: Use Haptics
        self.texture_display = tk.Label(self.master, textvariable=self.current_texture)
        self.haptics_button = tk.Button(self.master, text="Feel Texture", command=self.use_haptics)
        self.back_button = tk.Button(self.master, text="Back to Texture Selection", command=self.show_texture_selection)

    def show_texture_selection(self):
        # Clear previous screen
        self.clear_screen()

        # Display screen 2 widgets
        self.texture_label.pack()
        self.water_button.pack()
        self.concrete_button.pack()

    def select_texture(self, texture):
        self.current_texture.set("Current Texture: " + texture)
        self.show_haptics_screen()

    def show_haptics_screen(self):
        # Clear previous screen
        self.clear_screen()

        # Display screen 3 widgets
        self.texture_display.pack()
        self.haptics_button.pack()
        self.back_button.pack()

    def use_haptics(self):
        # Simulate haptic feedback
        print("Simulating haptic feedback for", self.current_texture.get())

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()

def main():
    root = tk.Tk()
    app = HapticTextureApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
