import tkinter as tk
import tkinter.scrolledtext as tkst

from tkinter import messagebox
import track_library as lib
import font_manager as fonts




def set_text(text_area, content):   
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song, track_number):
        song.track_number = track_number
        self.songs.append(song)

album1 = Playlist("Album1")

class CreateTrackList():
    def __init__(self, window):
        window.geometry("750x500")
        window.title("Create Track List")

        self.input_txt = tk.Entry(window, width=5)
        self.input_txt.grid(row=0, column= 2, padx = 10, pady=10)

        track_number_lbl = tk.Label(window, text="Enter a track number:")
        track_number_lbl.grid(row=0, column=1, padx=10, pady=10)

        add_btn = tk.Button(window, text="Add to playlist", command=self.add_to_playlist, width= 20)
        add_btn.grid(row=0, column=3, padx=40, pady=40)

        reset_btn = tk.Button(window, text="Reset", command=self.reset, width=8)
        reset_btn.grid(row=3, column=2, padx=30, pady=30)

        play_btn = tk.Button(window, text="Play Now",command=self.play)
        play_btn.grid(row=3, column=1, padx=0, pady=0)

        self.list_txt = tkst.ScrolledText(window, width=45, height=15, wrap="none")     
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    
        self.content=""
    def add_to_playlist(self):
        track_number = self.input_txt.get()
        if not track_number:
            messagebox.showerror("Error", "Track number cannot be empty")
            return
        if track_number.isalpha():
            messagebox.showerror("Error", "Track number must be numeric")
            return
        if track_number in lib.library:
            track = lib.library[track_number]   
            album1.add_song(track, track_number)
            self.display()
        else:
            set_text(self.list_txt, f"Track {track_number} not found !")
     
    def reset(self):
        album1.songs = []
        self.display()
        set_text(self.list_txt, f"Playlist has been reset completely !")

    def play(self):
        for song in album1.songs:
            key = song.track_number
            lib.increment_play_count(key)            
        self.display()
    
    def display(self):
        content = "Current Playlist:\n"
        for track in album1.songs:
            content += f"{track.name} - {track.artist} {track.stars()} - Play count :{track.play_count}\n"
            set_text(self.list_txt, content)
    


if __name__ == "__main__":
    window = tk.Tk()        
    fonts.configure()       
    CreateTrackList(window)     
    window.mainloop()       
            