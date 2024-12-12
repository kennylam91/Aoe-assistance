import pytest
import os
from PIL import Image
from main import extract_text_from_area

# Get the absolute path to the test_images directory
TEST_IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'test_images')
civilization_box = (5, 780, 90, 796)
population_box = (802, 23, 840, 50)
wood_box = (30, 2, 60, 17)
food_box = (97, 2, 130, 17)
gold_box = (163, 2, 200, 17)
stone_box = (232, 2, 270, 17)
age_box = (760, 0, 850, 20)
timeline_box = (2, 26, 55, 40)
assyrian_image = os.path.join(TEST_IMAGES_DIR, 'town-center-assyrian.png')
minoan_image = os.path.join(TEST_IMAGES_DIR, 'minoan.png')

test_Assyrian_image = Image.open(assyrian_image)
test_Minoan_image = Image.open(minoan_image)

def test_extract_civilization_name():
    extracted_text = extract_text_from_area(test_Assyrian_image, civilization_box)
    assert "Assyrian" in extracted_text

    extracted_text = extract_text_from_area(test_Minoan_image, civilization_box)
    assert "Minoan" in extracted_text

def test_extract_population():
    extracted_text = extract_text_from_area(test_Assyrian_image, population_box, True)
    assert extracted_text == "3/4"

    extracted_text = extract_text_from_area(test_Minoan_image, population_box, True)
    assert extracted_text == "5/8"

def test_extract_resources_wood():
    extracted_text = extract_text_from_area(test_Assyrian_image, wood_box, True)
    assert extracted_text == "200"
    extracted_text = extract_text_from_area(test_Minoan_image, wood_box, True)
    assert extracted_text == "170"

def test_extract_resources_food():
    extracted_text = extract_text_from_area(test_Assyrian_image, food_box, True)
    assert extracted_text == "200"
    extracted_text = extract_text_from_area(test_Minoan_image, food_box, True)
    assert extracted_text == "50"

def test_extract_resources_gold():
    extracted_text = extract_text_from_area(test_Assyrian_image, gold_box, True)
    assert int(extracted_text) < 10
    extracted_text = extract_text_from_area(test_Minoan_image, gold_box, True)
    assert int(extracted_text) < 10

def test_extract_resources_stone():
    extracted_text = extract_text_from_area(test_Assyrian_image, stone_box, True)
    assert extracted_text == "150"
    extracted_text = extract_text_from_area(test_Minoan_image, stone_box, True)
    assert extracted_text == "150"

def test_extract_age():
    extracted_text = extract_text_from_area(test_Assyrian_image, age_box)
    assert "Stone" in extracted_text
    extracted_text = extract_text_from_area(test_Minoan_image, age_box)
    assert "Stone" in extracted_text

def test_extract_timeline():
    extracted_text = extract_text_from_area(test_Assyrian_image, timeline_box, True)
    assert extracted_text == "00:00:24"
    extracted_text = extract_text_from_area(test_Minoan_image, timeline_box, True)
    assert extracted_text == "00:03:21"

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