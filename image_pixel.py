import cv2
import numpy as np
import matplotlib.pyplot as plt


def read_image(file_path):
    # Read the image in grayscale mode
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    return image


def add_value_to_pixels(image, value):
    # Add a predefined value to each pixel
    added_image = image.astype(np.int16) + value  # Using int16 to avoid overflow

    # Clip the values to be between 0 and 255 for display
    clipped_image = np.clip(added_image, 0, 255).astype(np.uint8)

    return added_image, clipped_image


def subtract_uniform_noise(image, min_noise, max_noise):
    # Generate a single random noise value for all pixels
    noise = np.random.randint(min_noise, max_noise + 1)

    # Subtract the uniform noise value from the image
    subtracted_image = image - noise

    # Clip the values to be between 0 and 255 for display
    clipped_image = np.clip(subtracted_image, 0, 255).astype(np.uint8)

    return subtracted_image, clipped_image, noise


def display_image(image, title):
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.title(title)
    plt.axis('off')
    plt.show()


def save_image(image, file_name):
    cv2.imwrite(file_name, image)


def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                key, value = line.split('=')
                config[key.strip()] = int(value.strip())
    return config


# Main function to execute the process
def main(image_path, config_path):
    # Read configuration values from file
    config = read_config(config_path)

    # Extract values from the config dictionary
    add_value = config['add_value']
    min_noise = config['min_noise']
    max_noise = config['max_noise']

    # Step 1: Read the image
    original_image = read_image(image_path)
    display_image(original_image, 'Original Image')
    save_image(original_image, 'original_image.png')

    # Step 2: Add predefined value to each pixel
    added_image, added_clipped_image = add_value_to_pixels(original_image, add_value)
    display_image(added_clipped_image, 'Image After Adding Value')
    save_image(added_clipped_image, 'image_after_adding_value.png')

    # Step 3: Subtract uniform noise
    subtracted_image, subtracted_clipped_image, noise = subtract_uniform_noise(added_image, min_noise, max_noise)

    # Display the final image with noise subtraction info
    display_image(subtracted_clipped_image, f'Image After Subtracting Uniform Noise\nNoise Subtracted: {noise}')
    save_image(subtracted_clipped_image, 'image_after_subtracting_noise.png')


# Example usage
image_path = 'img.png'  # Indicate that the image file is in the same folder as the script
config_path = 'config.txt'  # The path to the configuration file

main(image_path, config_path)
#Test
