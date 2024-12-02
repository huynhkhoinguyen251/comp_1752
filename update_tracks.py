import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib
import font_manager as fonts
from tkinter import messagebox

def set_text(text_area, content):   
    text_area.delete("1.0", tk.END) 
    text_area.insert(1.0, content)

class UpdateTracks():
    def __init__(self, window):
        window.geometry("600x400")
        window.title("Update Tracks")
    
        self.list_txt = tkst.ScrolledText(window, width=45, height=15, wrap="none")     
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        
        track_number_lbl = tk.Label(window, text="Enter a track number:")
        track_number_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input1_txt = tk.Entry(window, width=5)
        self.input1_txt.grid(row=0, column=2, padx = 10, pady=10)

        new_rating_lbl = tk.Label(window, text="New Rating for this track:")
        new_rating_lbl.grid(row=3, column=1, padx=10, pady=10)

        self.input2_txt = tk.Entry(window, width=5)
        self.input2_txt.grid(row=3, column=2, padx = 10, pady=10)

        set_now_btn = tk.Button(window, text="Set Now",command=self.set_now, width= 10)
        set_now_btn.grid(row=1, column=3, padx=10, pady=10)

    def set_now(self):
        track_number = self.input1_txt.get()
        rating_input = self.input2_txt.get()
        if track_number.isalpha():
            messagebox.showerror("Error", "Track number must be numeric")
            return
        if not track_number or not rating_input:
            messagebox.showerror("Error", "Track number or New rating input cannot be empty")
            return
        new_rating = int(rating_input)
        if new_rating < 1 or new_rating > 5:
            messagebox.showerror("Error", "Rating must be between 1 and 5.")
            return
        if track_number in lib.library:
            track = lib.library[track_number]
            lib.set_rating(track_number, new_rating)
            self.content = f"{track.name} - {track.artist} {track.stars()} - Play count :{track.play_count}"
            set_text(self.list_txt, self.content)
        else:
            set_text(self.list_txt, f"Track {track_number} not found !") 


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateTracks(window)     
    window.mainloop()