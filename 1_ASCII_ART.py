import PIL.Image

# ASCII Charater List [Descending Order]
ASCII_CHARS = ["#", "@", "$", "&", "%", "B", "8", "W", "M", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "Z", "0", "O", "Q", "L", "C", "J", "U", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t", "/", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", "^", "'", ".", " "]

# Resize the image according to new width while maintaining aspect ratio
def resize_image(image, new_width=650, new_height=125):
    width, height = image.size
    aspect_ratio = height / width
    # new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert Each Pixel To GrayScale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert pixels to ASCII Strings
def pixels_to_ASCII(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def main(new_width=650, new_height=250):
    # Attempt to open object from user input
    path = input("Enter a Valid Path: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not valid")
        return

    # Convert to ASCII
    new_image_data = pixels_to_ASCII(grayify(resize_image(image, new_width)))

    # Format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i : (i + new_width)] for i in range(0, pixel_count, new_width))

    # Print Image
    print(ascii_image)

    # Save image as txt
    with open("5_ascii_image_art.txt", "w") as f:
        f.write(ascii_image)

if __name__ == "__main__":
    main()



main()