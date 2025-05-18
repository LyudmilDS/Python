import mss
from PIL import Image
import pytesseract
import time

from keyboard_lib import keyboard_lib


def take_screenshot():
    with mss.mss() as scrsht:
        scrsht.shot(output='pokemon_screenshot.png')

def crop_image():
    file = Image.open('pokemon_screenshot.png')
    crop_start_x = 1150
    crop_start_y = 240
    crop_size_x = 400
    crop_size_y = 35
    box = (crop_start_x, crop_start_y, crop_start_x+crop_size_x, crop_start_y+crop_size_y)
    cropped_scrsht = file.crop(box)
    return cropped_scrsht

def convert_image_to_text(image):
    pytesseract.pytesseract.tesseract_cmd = r'E:\Program Files\Tesseract-OCR(image-to-text)\tesseract'
    text = pytesseract.image_to_string(image)
    return text[2:]


#
if __name__ == "__main__":
    time.sleep(2)
    # a log file is created for analysis purpose
    f = open("encounter_log.txt", "w")
    obj = keyboard_lib()
    while True:
        if obj.stop_program():
            break

        take_screenshot()
        cropped_image = crop_image()
        encountered_pokemon = convert_image_to_text(cropped_image)
        cropped_image.save("Cropped_pokemon_name.png")
        print("encountered:"+encountered_pokemon)

        # This is hard-coded to search for encounter, named Slowpoke
        if "[E]" in encountered_pokemon:
            f.write("encountered an Elite. Stopping the program\n")
            break
        elif "Graveler" in encountered_pokemon:
            f.write("Graveler\n")
            obj.fight_Graveler()
        elif "Golbat" in encountered_pokemon:
            f.write("Golbat\n")
            obj.run()
        elif "Slowpoke" in encountered_pokemon:
            f.write("Congratulation! you found Slowpoke. Now take actions!\n")
            break

        obj.walking_in_circle()
