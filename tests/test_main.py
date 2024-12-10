import pytest
import os
from PIL import Image
from main import extract_text_from_area

# Get the absolute path to the test_images directory
TEST_IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'test_images')
civilization_box = (5, 780, 90, 794)
population_box = (770, 23, 840, 50)
resources_box = (30, 0, 260, 20)
age_box = (760, 0, 850, 20)
image_path = os.path.join(TEST_IMAGES_DIR, 'town-center-assyrian.png')

def test_extract_civilization_name():
    test_image = Image.open(image_path)
    extracted_text = extract_text_from_area(test_image, civilization_box)
    assert "Assyrian" in extracted_text

def test_extract_population():
    test_image = Image.open(image_path)
    extracted_text = extract_text_from_area(test_image, population_box)
    assert extracted_text == "pop: 3/4"

# def test_extract_resources():
#     test_image = Image.open(image_path)
#     extracted_text = extract_text_from_area(test_image, resources_box)
#     assert extracted_text == "200 200 0 150"

def test_extract_age():
    test_image = Image.open(image_path)
    extracted_text = extract_text_from_area(test_image, age_box)
    assert "Stone" in extracted_text
# def test_extract_text_from_area_invalid_bbox():
#     # Load a test image
#     test_image = Image.open('tests/test_images/sample_text.png')
    
#     # Invalid bounding box (right < left or bottom < top)
#     invalid_bbox = (300, 300, 100, 100)
    
#     # Should return None for invalid bbox
#     result = extract_text_from_area(test_image, invalid_bbox)
#     assert result is None

# def test_extract_text_from_area_empty_region():
#     # Load a test image
#     test_image = Image.open('tests/test_images/sample_text.png')
    
#     # Define a bounding box in an empty area
#     empty_bbox = (0, 0, 50, 50)
    
#     # Extract text from empty area
#     extracted_text = extract_text_from_area(test_image, empty_bbox)
    
#     # Should return empty string or None
#     assert extracted_text == "" or extracted_text is None 