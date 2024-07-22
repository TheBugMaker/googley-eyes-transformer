import numpy as np
import cv2

def alpha_blend(img1, img2, position):
    # Ensure img1 is the background and img2 is the foreground
    y, x = position
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    # Create an overlay with the size of the background image
    overlay = np.zeros((h1, w1, 4), dtype=np.float32)
    overlay[y:y+h2, x:x+w2] = img2

    # Extract the alpha channels
    alpha1 = img1[:, :, 3] / 255.0
    alpha2 = overlay[:, :, 3] / 255.0

    # Create a new image with the same shape as the background image
    blended_image = np.zeros_like(img1, dtype=np.float32)

    for c in range(3):
        blended_image[:, :, c] = (img1[:, :, c] * alpha1 * (1 - alpha2) + overlay[:, :, c] * alpha2)

    # Calculate the new alpha channel
    new_alpha = alpha1 + alpha2 * (1 - alpha1)
    blended_image[:, :, 3] = new_alpha * 255

    # Convert blended image to 8-bit unsigned integer
    blended_image = np.clip(blended_image, 0, 255).astype(np.uint8)

    return blended_image

def add_alpha_channel(img, alpha    = 255):
    b_channel, g_channel, r_channel = cv2.split(img)

    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 #creating a dummy alpha channel image.

    return cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
