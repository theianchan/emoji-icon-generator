import argparse
from PIL import Image, ImageDraw, ImageFont

def create_emoji_icon(emoji, output_file, size=(48, 48)):
    # Create a new RGBA image
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Load the emoji font
    font_path = "/System/Library/Fonts/Apple Color Emoji.ttc"
    font_size = min(size) * 2 // 3
    font = ImageFont.truetype(font_path, font_size, layout_engine=ImageFont.Layout.BASIC)
    
    # Calculate the text size
    text_width, text_height = font.getmask(emoji).size

    # Draw the emoji on the image
    draw.text(((size[0] - text_width) / 2, (size[1] - text_height) / 2), emoji, font=font, fill=(0, 0, 0, 255))

    # Save the image to the output file
    img.save(output_file, "PNG")

def main():
    parser = argparse.ArgumentParser(description="Generate an emoji icon")
    parser.add_argument("emoji", type=str, help="Emoji character to use as the icon")
    parser.add_argument("output_file", type=str, help="Output filename for the generated icon")
    args = parser.parse_args()

    create_emoji_icon(args.emoji, args.output_file)
    print(f"Successfully created emoji icon '{args.emoji}' and saved it as '{args.output_file}'.")

if __name__ == "__main__":
    main()
