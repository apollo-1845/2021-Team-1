import os

from PIL import Image

from image_data import sum_of_pixel_brightnesses

DIR = "resources/images/"


def string_after(str, preceding):
    return_next = False
    for word in str.split(' '):
        if word == preceding:
            return_next = True
        elif return_next:
            return word


def main(mask):
    with open("results.csv", "w+") as results:
        results.write("Filename, Percentage whiteness, Latitude, Longitude\n")
        with open("resources/locations.txt") as locations_file:
            locations = [*map(lambda it: it[:-1], locations_file.readlines())]
            maximum = sum_of_pixel_brightnesses(mask)
            directory = os.fsencode(DIR)
            for file in os.listdir(directory):
                filename = os.fsdecode(file)
                with Image.open(DIR + filename) as im:
                    masked = Image.composite(im, mask, mask)
                    location = locations[int(filename.split('_')[-1][:-4])]
                    results.write(
                        f"{filename}, {sum_of_pixel_brightnesses(masked) / maximum * 100}%, {string_after(location, 'latitude')}, {string_after(location, 'longitude')}\n")


if __name__ == '__main__':
    with Image.open("resources/image_mask.png") as the_mask:
        main(the_mask)
