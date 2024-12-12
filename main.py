import pyautogui
import pytesseract
from PIL import Image

def take_screenshot(save_path=None):
    """
    Captures a screenshot of the entire screen and optionally saves it to a file.
    Args:
        save_path (str, optional): Path where to save the screenshot. If None, only returns the image.
    Returns:
        PIL.Image: Screenshot image object
    """
    try:
        screenshot = pyautogui.screenshot()
        if save_path:
            screenshot.save(save_path)
        return screenshot
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None

def extract_text_from_area(screenshot, bbox, extract_numbers_only=False):
    """
    Extracts text from a specified area of the screenshot. Optionally, extracts numbers only.
    Args:
        screenshot (PIL.Image): Screenshot image object
        bbox (tuple): Bounding box coordinates (left, top, right, bottom)
        extract_numbers_only (bool, optional): If True, extracts numbers only. Defaults to False.
    Returns:
        str: Extracted text from the specified area
    """
    try:
        # Crop the screenshot to the specified area and save it for debugging
        area_image = screenshot.crop(bbox)
        
        # Pre-process the image to increase the quality for Tesseract
        preprocessed_image = area_image.convert('L')  # Convert to grayscale
        preprocessed_image = preprocessed_image.point(lambda x: 0 if x < 100 else 255, '1')  # Apply threshold
        
        preprocessed_image.save('debug_cropped_image.png', 'PNG')
        # Extract text from the pre-processed image
        if extract_numbers_only:
            text = pytesseract.image_to_string(preprocessed_image,  config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789:/').strip()
        else:
            text = pytesseract.image_to_string(preprocessed_image,  config='--psm 8').strip()
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def convert_to_black_and_white(img, threshold=200):

    # Convert the image to RGB mode if it's not already
    img_rgb = img.convert('RGB')

    # Get the image size
    width, height = img.size
    
    # Loop through each pixel
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel
            r, g, b = img_rgb.getpixel((x, y))
            
            # Check if the pixel is red
            if r > threshold and g < threshold and b < threshold:
                img.putpixel((x, y), (0, 0, 0))
            elif r < threshold and g > threshold and b < threshold:
                img.putpixel((x, y), (0, 0, 0))
            else:
                img.putpixel((x, y), (255, 255, 255))
    
    return img