import pytest
from track_library import LibraryItem  # Make sure to import the correct path

def test_library_item_initialization():
    item = LibraryItem(name="Song A", artist="Artist 1", picture="image.jpg", rating=3)
    assert item.name == "Song A"
    assert item.artist == "Artist 1"
    assert item.rating == 3
    assert item.play_count == 0  # Default value
    assert item.picture == "image.jpg"

def test_library_item_info():
    item = LibraryItem(name="Song A", artist="Artist 1", picture="image.jpg", rating=3)
    assert item.info() == "Song A - Artist 1 ***"

def test_library_item_stars():
    item = LibraryItem(name="Song A", artist="Artist 1", picture="image.jpg", rating=5)
    assert item.stars() == "*****"
    
    item = LibraryItem(name="Song B", artist="Artist 2", picture="image2.jpg", rating=0)
    assert item.stars() == ""
    
    item = LibraryItem(name="Song C", artist="Artist 3", picture="image3.jpg", rating=1)
    assert item.stars() == "*"

def test_default_rating():
    item = LibraryItem(name="Song A", artist="Artist 1", picture="image.jpg")
    assert item.rating == 0  # Default rating is 0
    assert item.stars() == ""  # No stars for default rating
