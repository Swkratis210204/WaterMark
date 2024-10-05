import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from edit import EditImages


class GUI:
    def __init__(self):
        self.WINDOW_WIDTH = 750
        self.WINDOW_HEIGHT = 600
        self.BG_COLOR = "#87CEEB"  # Light Sky Blue
        self.canvas = None
        self.scrollable_content = None
        self.root = tk.Tk()
        self.setup_window()
        self.create_scrollable_frame()
        self.selection = ''
        self.current_image = None
        self.edit = EditImages()

    def setup_window(self):
        self.root.title("My Tkinter App")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_geometry = f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{(screen_width - self.WINDOW_WIDTH) // 2}" \
                          f"+{(screen_height - self.WINDOW_HEIGHT) // 2}"
        self.root.geometry(window_geometry)  # Centered window
        self.root.configure(bg=self.BG_COLOR)

    def create_scrollable_frame(self):
        # Create a scrollable frame
        scrollable_frame = tk.Frame(self.root)

        # Create a canvas for adding scrolling
        self.canvas = tk.Canvas(scrollable_frame, bg=self.BG_COLOR)
        scrollbar = tk.Scrollbar(scrollable_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_content = tk.Frame(self.canvas, bg=self.BG_COLOR)

        # Configure the canvas to scroll
        self.scrollable_content.bind("<Configure>",
                                     lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_content, anchor="nw")

        # Pack the scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollable_frame.pack(fill="both", expand=True)

        # Bind mouse wheel scrolling
        self.root.bind_all("<MouseWheel>", self.on_mouse_wheel)  # For Windows and Mac

    def on_mouse_wheel(self, event):
        """ Scroll the canvas with mouse wheel """
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def run(self):
        self.root.mainloop()

    def set_selected_option(self, selected_option):
        self.selection = selected_option.get()  # Fetch the selected option

    def set_current_image(self, image):
        self.current_image = image

    from tkinter import simpledialog, messagebox

    def show_popup(self, selection):
        self.set_selected_option(selection)

        if self.selection == "Resize":
            width = simpledialog.askinteger("Input", "Enter width:", parent=self.root, minvalue=1)
            height = simpledialog.askinteger("Input", "Enter height:", parent=self.root, minvalue=1)
            if width is not None and height is not None:
                self.edit.resize_image_final(self.current_image, width, height)
            else:
                messagebox.showinfo("Cancelled", "Resize operation was cancelled.")

        elif self.selection == "Add logo/label":
            logo = filedialog.askopenfilename(title="Select Logo",
                                              filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])

            label_text = simpledialog.askstring("Input", "Enter label text (or leave empty if none):", parent=self.root)
            if logo:
                logo_x = simpledialog.askinteger("Input", "Enter X coordinate for logo position:", parent=self.root,
                                                 minvalue=0)
                logo_y = simpledialog.askinteger("Input", "Enter Y coordinate for logo position:", parent=self.root,
                                                 minvalue=0)
                if logo_x is not None and logo_y is not None:
                    self.edit.add_logo(self.current_image, logo, (logo_x, logo_y))
            if label_text:
                label_x = simpledialog.askinteger("Input", "Enter X coordinate for label position:", parent=self.root,
                                                  minvalue=0)

                label_y = simpledialog.askinteger("Input", "Enter Y coordinate for label position:", parent=self.root,
                                                  minvalue=0)
                if label_x is not None and label_y is not None:
                    self.edit.add_label(self.current_image, label_text, (label_x, label_y))
            if not logo and not label_text:
                messagebox.showinfo("Cancelled", "No logo or label was added.")

        elif self.selection == "Change type":
            type_img = simpledialog.askstring("Input", "Enter type (e.g., JPEG, PNG):", parent=self.root)
            if type_img is not None:
                self.edit.change_type(self.current_image, type_img)
        else:
            messagebox.showinfo("Unknown Option", "Please select a valid option.")
