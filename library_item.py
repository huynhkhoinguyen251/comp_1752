class LibraryItem:
    def __init__(self, name, artist, picture, rating=0):
        self.name = name
        self.artist = artist
        self.rating = rating
        self.play_count = 0
        self.picture = picture

    def info(self):
        return f"{self.name} - {self.artist} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars

    