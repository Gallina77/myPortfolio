#!/usr/bin/env python3
"""
Type and Let Go Icon Generator - Keyboard Only
Generates keyboard icon with transparent background and light color backdrop.
Theme: Type and let go
"""

from PIL import Image, ImageDraw, ImageFont
import os
import math

# Color palette
COLORS = {
    'primary_dark': '#27445D',
    'primary_medium': '#497D74',
    'primary_light': '#71BBB2',
    'background_light': '#EFE9D5',
    'white': '#ffffff',
    'gray_light': '#f8f9fa',
    'gray_medium': '#6c757d'
}


class IconGenerator:
    def __init__(self, size=512):
        self.size = size
        self.center = size // 2

    def create_base_image(self):
        """Create a transparent base image"""
        return Image.new('RGBA', (self.size, self.size), (0, 0, 0, 0))

    def keyboard_icon(self):
        """Generate a keyboard icon with floating keys - light keyboard base on transparent background"""
        img = self.create_base_image()
        draw = ImageDraw.Draw(img)

        # Main keyboard body - larger size
        kbd_width = self.size * 0.85
        kbd_height = self.size * 0.5
        kbd_x = (self.size - kbd_width) // 2
        kbd_y = self.size * 0.25

        # Keyboard base in light color (the "board" the keyboard sits on)
        draw.rounded_rectangle(
            [kbd_x, kbd_y, kbd_x + kbd_width, kbd_y + kbd_height],
            radius=25, fill=COLORS['background_light'], outline=COLORS['primary_medium'], width=4
        )

        # Individual keys with "letting go" effect - larger keys
        key_size = 32
        key_spacing = 42
        rows = 3
        keys_per_row = [8, 7, 6]

        for row in range(rows):
            y_pos = kbd_y + 25 + row * key_spacing
            row_keys = keys_per_row[row]
            start_x = kbd_x + (kbd_width - (row_keys * key_spacing - 10)) // 2

            for col in range(row_keys):
                x_pos = start_x + col * key_spacing

                # Some keys "float away" with transparency
                alpha = 255 if row < 2 else max(120, 255 - col * 25)
                key_color = COLORS['primary_light'] + f"{alpha:02x}"

                # Slightly offset floating keys with more dramatic effect
                offset_y = 0 if row < 2 else -col * 3

                draw.rounded_rectangle(
                    [x_pos, y_pos + offset_y, x_pos + key_size, y_pos + key_size + offset_y],
                    radius=6, fill=key_color, outline=COLORS['primary_dark'], width=2
                )

        return img


def generate_keyboard_icon(output_dir="icons", size=512):
    """Generate keyboard icon only"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    generator = IconGenerator(size)
    icon = generator.keyboard_icon()

    # Save as PNG
    filename = f"type_and_go_keyboard_{size}px.png"
    icon.save(os.path.join(output_dir, filename), format='PNG', optimize=True)
    print(f"Generated: {filename}")

    print(f"\nKeyboard icon generated in '{output_dir}' directory")
    print("Features: Light background, large keyboard with floating keys effect")


if __name__ == "__main__":
    # Generate only 512px keyboard icon
    print("Generating 512px keyboard icon...")
    generate_keyboard_icon("icons", 512)

    print("\n✨ Keyboard icon generation complete!")
    print("Theme: Type and let go")
    print("Features: Transparent background with light keyboard base and floating key effect")