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

def extract_text_from_area(screenshot, bbox):
    """
    Extracts text from a specified area of the screenshot.
    Args:
        screenshot (PIL.Image): Screenshot image object
        bbox (tuple): Bounding box coordinates (left, top, right, bottom)
    Returns:
        str: Extracted text from the specified area
    """
    try:
        # Crop the screenshot to the specified area and save it for debugging
        area_image = screenshot.crop(bbox)
        area_image.save('debug_cropped_image.png', 'PNG')
        
        # Extract text from the cropped image
        text = pytesseract.image_to_string(area_image).strip()
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None
