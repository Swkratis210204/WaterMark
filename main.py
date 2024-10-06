import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from Gui import GUI
from edit import EditImages

# Create the main window
gui = GUI()
edit = EditImages()


def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )  # Filter for image files
    if file_path:
        img = Image.open(file_path)  # Open the image
        img_width, img_height = img.size  # Store the original dimensions
        gui.set_current_image(img)
        img = img.resize((700, 400), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)  # Convert the image to PhotoImage for display in Tkinter
        image_label.config(image=img_tk)
        image_label.image = img_tk  # Keep a reference to avoid garbage collection
        image_label.pack(pady=10, padx=10, anchor='center')  # Center the image label

        # Display the dimensions in a label
        size_label.config(text=f"Image Dimensions: {img_width} x {img_height}")


def update_display_image(image,size):
    img_tk = ImageTk.PhotoImage(image)
    image_label.config(image=img_tk)
    image_label.image = img_tk  # Keep a reference to avoid garbage collection
    image_label.pack(pady=10, padx=10, anchor='center')
    size_label.config(text=f"Current Dimensions: {size[0]} x {size[1]}")


# Create the welcome label
welcome_label = tk.Label(
    gui.scrollable_content,
    text="Welcome to WaterSwk",
    font=("Helvetica", 14),
    bg="#87CEEB"  # Match the background color
)
welcome_label.pack(pady=10, padx=10)  # Add padding for better spacing

# Create a label for the app description sentence with wraplength
description_label = tk.Label(
    gui.scrollable_content,
    text="This is a simple and free Watermark app to add logos and texts to photos.",
    font=("Helvetica", 10),
    wraplength=350,  # Set wraplength to prevent text overflow
    bg="#87CEEB"  # Match the background color
)
description_label.pack(pady=5, padx=10)  # Add padding for better spacing

# Create an "Upload Image" button
upload_button = tk.Button(gui.scrollable_content, text="Upload Image", command=upload_image)
upload_button.pack(pady=10, padx=10)

# Create an empty label to display the uploaded image
image_label = tk.Label(gui.scrollable_content, image=edit.get_placeholder_image(), borderwidth=0, highlightthickness=0)
image_label.pack(pady=10, padx=10, anchor='center')

# Create a label to display the image dimensions
size_label = tk.Label(
    gui.scrollable_content,
    text="Image Dimensions: ",
    font=("Helvetica", 10),
    wraplength=350,  # Set wraplength to prevent text overflow
    bg="#87CEEB"  # Match the background color
)
size_label.pack(pady=5, padx=10)  # Add padding for better spacing
size_label.config(text=f"Image Dimensions: {edit.get_placeholder_size()[0]} x {edit.get_placeholder_size()[1]}")

# Create the dropdown menu below the image
selected_option = tk.StringVar(gui.root)
selected_option.set("Select an option")  # Set a default option
options = ["Resize", "Add logo/label", "Change type"]

# Create the dropdown menu
dropdown = tk.OptionMenu(gui.scrollable_content, selected_option, *options)
dropdown.config(borderwidth=0, highlightthickness=0)  # Remove border and highlight
dropdown.pack(pady=20, padx=10)

# Add a button to trigger the function
button = tk.Button(gui.scrollable_content, text="Get Selected Option",
                   command=lambda: gui.show_popup(selected_option,update_display_image))
button.pack(pady=10)

gui.run()
