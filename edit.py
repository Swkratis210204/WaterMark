from PIL import Image, ImageTk, ImageFont, ImageDraw
import os


class EditImages:
    def __init__(self):
        # Load a placeholder image
        placeholder_image_path = "placeholder.jpeg"  # Replace this with your placeholder image path
        self.placeholder_img = Image.open(placeholder_image_path)
        placeholder_img = self.placeholder_img.resize((700, 400), Image.LANCZOS)  # Resize placeholder image if needed
        self.placeholder_img_tk = ImageTk.PhotoImage(placeholder_img)
        self.path = r"C:\Users\swkra\OneDrive\Υπολογιστής\100-Days-Of-Code\Day85-WaterMark"

    def resize_image_final(self, image, width, height):
        if image is None:
            image = self.placeholder_img  # Use the placeholder if no image is provided
        path = os.path.join(self.path, "Resized")
        os.makedirs(path, exist_ok=True)
        resized_image = image.resize((width, height), Image.LANCZOS)
        if resized_image.mode == 'RGBA':
            resized_image = resized_image.convert('RGB')
        original_format = image.format if image.format else 'png'
        output_image_path = os.path.join(path, f"Resized.{original_format.lower()}")
        resized_image.save(output_image_path, format=original_format)
        return resized_image.resize((700, 400), Image.LANCZOS), (width,height)

    def change_type(self, image=None, type_img='JPEG'):
        if image is None:
            image = self.placeholder_img
        if type_img.upper() == 'JPEG' and image.mode == 'RGBA':
            image = image.convert('RGB')  # Convert to RGB as JPEG does not support transparency
        path = os.path.join(self.path, "ChangedType")
        os.makedirs(path, exist_ok=True)
        output_file_path = os.path.join(path, f"Changed.{type_img.lower()}")
        try:
            image.save(output_file_path, format=type_img.upper())
            print(f"Image saved successfully at {output_file_path}")
        except Exception as e:
            print(f"Error saving image: {e}")
        return image.resize((700, 400), Image.LANCZOS), image.size

    def add_logo(self, image, logo_path, coordinates):
        if image is None:
            image = self.placeholder_img
        path = os.path.join(self.path, "LogoText", "Added_Logo")
        os.makedirs(path, exist_ok=True)
        original_format = image.format
        logo = Image.open(logo_path)
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        image.paste(logo, coordinates, logo)  # Use the logo itself as the mask for transparency
        output_file_path = os.path.join(path, f"Text.{original_format.lower()}")
        image.save(output_file_path, format=original_format)
        return image.resize((700, 400), Image.LANCZOS), image.size

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
        draw.text(coordinates, text, fill=font_color, font=font)
        output_file_path = os.path.join(path, f"Added_Logo/Text.{image.format.lower()}")
        image.save(output_file_path)
        return image.resize((700, 400), Image.LANCZOS), image.size

    def get_placeholder_image(self):
        return self.placeholder_img_tk

    def get_placeholder_size(self):
        return self.placeholder_img.size

    def get_placeholder(self):
        return self.placeholder_img
