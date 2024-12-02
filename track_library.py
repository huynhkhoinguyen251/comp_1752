from library_item import LibraryItem


library = {}
library["01"] = LibraryItem("Another Brick in the Wall", "Pink Floyd","JukeBox/image/another_brick_in_the_wall.png", 4)
library["02"] = LibraryItem("Stayin' Alive", "Bee Gees","JukeBox/image/stayin_alive.png", 5)
library["03"] = LibraryItem("Highway to Hell ", "AC/DC", "JukeBox/image/high_way_to_hell.png", 2)
library["04"] = LibraryItem("Shape of You", "Ed Sheeran", "JukeBox/image/shape_of_you.png", 1)
library["05"] = LibraryItem("Someone Like You", "Adele", "JukeBox/image/some_one_like_you.png", 3)
library["06"] = LibraryItem("Viva La Vida", "Cold Play", "JukeBox/image/vivalavida.png", 4)
library["07"] = LibraryItem("HUMBLE.", "Kendrick Lamar", "JukeBox/image/humble.png", 5)
library["08"] = LibraryItem("Snowman", "Sia", "JukeBox/image/snowman.png", 3)
library["09"] = LibraryItem("Gone", "Convolk", "JukeBox/image/gone.png", 3)

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return
