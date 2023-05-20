import tkinter as tk
from PIL import ImageTk, Image


# Function to handle algorithm selection
def select_algorithm():
    algorithm = algorithm_list.get(tk.ACTIVE)
    print("Selected Algorithm:", algorithm)


# Function to handle difficulty selection
def select_difficulty():
    difficulty = difficulty_list.get(tk.ACTIVE)
    print("Selected Difficulty:", difficulty)


# Create the main window
window = tk.Tk()

# Load and resize the background image
background_image = Image.open("AGame.png")
background_image = background_image.resize((500, 300))
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas for the background image
canvas = tk.Canvas(window, width=500, height=300)
canvas.pack()
canvas.create_image(0, 0, image=background_photo, anchor=tk.NW)

# Create a frame for the algorithm selection
algorithm_frame = tk.Frame(window)
algorithm_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a button to select the algorithm
select_difficulty_button = tk.Button(algorithm_frame, text="Select Algorithm", command=select_algorithm)
select_difficulty_button.pack()

# Create a listbox for Difficulty selection
algorithm_list = tk.Listbox(algorithm_frame, height=2)
algorithm_list.insert(tk.END, "AlphaBeta")
algorithm_list.insert(tk.END, "minmax")
algorithm_list.pack()

# Create a listbox for Difficulty selection
select_difficulty_button = tk.Button(algorithm_frame, text="Select Difficulty", command=select_difficulty)
select_difficulty_button.pack()

difficulty_list = tk.Listbox(algorithm_frame, height=3)
difficulty_list.insert(tk.END, "Hard")
difficulty_list.insert(tk.END, "Medium")
difficulty_list.insert(tk.END, "Easy")
difficulty_list.pack()

# Run the GUI event loop
window.mainloop()
