from PIL import Image, ImageDraw, ImageFont
import os

PATH = f"{os.getcwd()}\emote-creation"
font_filename = "LDFComicSans.ttf"
FONT = ImageFont.truetype(f"{PATH}\{font_filename}", 32)

def create_emote(dimensions, bg_colour, fg_colour, letter):
    emote = Image.new("RGB", dimensions, color=bg_colour)

    draw = ImageDraw.Draw(emote)
    draw.text((dimensions[0]/2, dimensions[1]/2), letter, fg_colour, FONT, anchor="mm")
    # print(f"created emote {letter}")
    return emote

def create_all_emotes():
    folders = ["default", "yellow", "green"]
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    bg_colours = [(54, 57, 62), (200, 182, 83), (108, 169, 101)]

    # create the folders
    os.mkdir(f"{PATH}\emotes") # create the emotes folder
    for folder in folders:
        os.mkdir(f"{PATH}\emotes\{folder}")
        print(f"Created folder {folder}")

    # create emotes based off of bg colour and save in folders
    for i in range(len(bg_colours)):
        colour = bg_colours[i]
        folder = folders[i]
        for letter in letters:
            emote = create_emote((32, 32), colour, (255, 255, 255), letter)
            emote.save(f"{PATH}\emotes\{folder}\letter_{letter}_{folder}.png")
            # print(f"saved emote {folder} {letter}")
        print(f"Saved {folder} emotes")

create_all_emotes()    