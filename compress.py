from PIL import Image

def compress_image(input_file, output_file, quality=50):
    image = Image.open(input_file)
    image.save(output_file, optimize=True, quality=quality)
    print("Image compressed successfully")

if __name__ == "__main__":
    compress_image("sample.jpg", "compressed.jpg", 40)
