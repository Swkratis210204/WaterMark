from PIL import Image, ImageTk,ImageFont,ImageDraw
import os


class EditImages:
    def __init__(self):
        # Load a placeholder image
        placeholder_image_path = "placeholder.jpeg"  # Replace this with your placeholder image path
        self.placeholder_img = Image.open(placeholder_image_path)
        placeholder_img = self.placeholder_img.resize((700, 400), Image.LANCZOS)  # Resize placeholder image if needed
        self.placeholder_img_tk = ImageTk.PhotoImage(placeholder_img)
        self.path = r"C:\Users\swkra\OneDrive\Υπολογιστής\100-Days-Of-Code\Day85-WaterMark"

    def resize_image(self, image, target_width, target_height):
        # Get the original dimensions
        original_width, original_height = image.size

        # Calculate the aspect ratio
        aspect_ratio = original_width / original_height

        # Determine new width and height to fit within target width and height
        if original_width / original_height > target_width / target_height:
            # Image is wider than the target aspect ratio
            new_width = target_width
            new_height = int(new_width / aspect_ratio)
        else:
            # Image is taller than the target aspect ratio
            new_height = target_height
            new_width = int(new_height * aspect_ratio)

        return image.resize((new_width, new_height), Image.LANCZOS)

    def resize_image_final(self, image, width, height):
        if image is None:
            image = self.placeholder_img
        path = f"{self.path}\Resized"
        os.makedirs(path, exist_ok=True)
        resized_image = image.resize((width, height), Image.LANCZOS)
        original_format = image.format
        # Convert to RGB if the image is in RGBA mode
        if resized_image.mode == 'RGBA':
            resized_image = resized_image.convert('RGB')
        output_image_path = os.path.join(path,
                                         f'Resized.{original_format.lower()}')  # Save with original format

        # Save the resized image in its original format
        resized_image.save(output_image_path, original_format)
        return self.resize_image(resized_image, 700, 700)

    def change_type(self, image=None, type_img='JPEG'):
        if image is None:
            image = self.placeholder_img
        path=f"{self.path}\LogoText"
        os.makedirs(path, exist_ok=True)
        output_file_path = os.path.join(path, f"Changed.{type_img.lower()}")
        image.save(output_file_path, format=type_img)
        return self.resize_image(image,700,700)

    def add_logo(self, image, logo_path, coordinates):
        if image is None:
            image = self.placeholder_img

        # Define the path for saving the image
        path = os.path.join(self.path, "LogoText", "Added_Logo")

        # Create the directories if they don't exist (including nested directories)
        os.makedirs(path, exist_ok=True)

        # Get the original format of the image
        original_format = image.format
        logo = Image.open(logo_path)
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        image.paste(logo, coordinates, logo)  # Use the logo itself as the mask for transparency
        output_file_path = os.path.join(path, f"Text.{original_format.lower()}")
        image.save(output_file_path, format=original_format)
        return self.resize_image(image, 700, 700)

    def add_label(self, image, text, coordinates, font_size=200, font_color='red'):
        if image is None:
            image = self.placeholder_img

        # Create directory for saving images if it doesn't exist
        path = os.path.join(self.path, "LogoText")
        os.makedirs(path, exist_ok=True)

        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)  # Specify your font file if needed
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font if arial.ttf is not found

        # Draw the text on the image
        draw.text(coordinates, text, fill=font_color, font=font)

        # Save the modified image
        output_file_path = os.path.join(path, f"Added_Logo/Text.{image.format.lower()}")
        image.save(output_file_path)
        return self.resize_image(image, 700, 700)

    def get_placeholder_image(self):
        return self.placeholder_img_tk

    def get_placeholder_size(self):
        return self.placeholder_img.size

    def get_placeholder(self):
        return self.placeholder_img
