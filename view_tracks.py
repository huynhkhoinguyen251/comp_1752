import tkinter as tk
import tkinter.scrolledtext as tkst


import track_library as lib
import font_manager as fonts


def set_text(text_area, content):   # Inserts content into the text_area 
    text_area.delete("1.0", tk.END) # First the existing content is deleted
    text_area.insert(1.0, content)  # Then the new content is inserted


class TrackViewer():                # Define a certain class to start creating a GUI to view and manage the tracks
    def __init__(self, window):     # Create a function to initialize the window for TrackViewer
        window.geometry("900x400")  # Set the window size to 700x600 pixels
        window.title("View Tracks") # Set the title of the window to "View Tracks"

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked) # Create a button labeled "List All Tracks" and give it a command "list_tracks_clicked" to show the list tracks when users click it
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10) # Then place the button in the grid which called grid layout

        enter_lbl = tk.Label(window, text="Enter Track Number") # Create a label called "Enter Track Number" to prompt users to enter the number of songs they want
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)       # Then place the label in the grid layout

        self.input_txt = tk.Entry(window, width=3)              # Create a input box to enter the track number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # Then place the input field in the grid layout

        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked) # Create a button labeled "View Track" and give it a command "view_tracks_clicked" to show the track that the user entered the number before
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)                                  # Then place the button in the grid layout

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")     # Create a scrollable text area to display the list of tracks for users
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) # Then place that scrolled text in the grid layout

        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")   # Create a text area to display detailed information about a selected track for users
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10) # Then place the text area in the grid layout again

        self.image_label = tk.Label(window) # Create a Label widget to display an image, associated with the window
        self.image_label.grid(row=1, column=3, sticky = "S") # Place the Label widget in the grid layout at row 1, column 3. The sticky="S" option aligns the Label to the bottom (South) of the cell

        search_lbl = tk.Label(window, text="Search for tracks/artists by name") # Create a label prompting the user to search for tracks or artists by name
        search_lbl.grid(row=2, column=0, padx=10, pady=10) # Position the label in row 2, column 0 with padding

        self.search_txt = tk.Entry(window, width=12) # Create an entry widget for user input (search query)
        self.search_txt.grid(row=2, column=1, padx=10, pady=10) # Position the entry field in row 2, column 1 with padding

        search_button_btn = tk.Button(window, text="SEARCH", command=self.search_tracks) # Create a button that triggers the search function when clicked
        search_button_btn.grid(row=2, column= 2, padx=10, pady=10)  # Position the button in row 2, column 2 with padding

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))                 # Create a label to display status messages
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Finally, place them below the text areas



        self.list_tracks_clicked()  # This will automatically list all the tracks once the app starts


    def view_tracks_clicked(self):  # This function will manages the click event for the "View Track" button
        key = self.input_txt.get()  # Retrieves the track number that the user has entered
        name = lib.get_name(key)    # Uses the track number to retrieve the track's name
        if name is not None:        # This means if the track exists
            track = lib.library[key] # 'lib.library' refers to a dictionary object where 'key' is used to retrieve a specific item
            artist = lib.get_artist(key) # Fetches the artist's name
            rating = lib.get_rating(key) # Fetches the rating of the track
            play_count = lib.get_play_count(key) # Retrieves the track's play count
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}" # Creates a formatted string with the track information in it
            set_text(self.track_txt, track_details) # Adds the retrieved data to the track details text field
            # Load an image file associated with the 'track' object's 'picture' attribute
            self.track_img = tk.PhotoImage(file=track.picture) # 'track.picture' contains the file path to the image
            self.image_label.configure(image=self.track_img) # Set the loaded image (self.track_img) as the content of the Label widget (self.image_label)
        else:   # And if the track doesn't exist
            # Clear the image from the Label widget by setting it to an empty string
            self.image_label.configure(image="") # This effectively removes the currently displayed image
            set_text(self.track_txt, f"Track {key} not found") # Shows an error notice in the text field for the track details

        self.status_lbl.configure(text="View Track button was clicked!") # Updates the status label


    def list_tracks_clicked(self): # Manages the "List All Tracks" button click occurrence
        track_list = lib.list_all() # Retrieves a comprehensive list of all tracks from the library
        set_text(self.list_txt, track_list) # Modifies the text area of the list using the acquired track list
        self.status_lbl.configure(text="List Tracks button was clicked!") # This one means updates the status label, too

    def search_tracks(self): 
        query = self.search_txt.get().lower() # Get the user's search query from the input field and convert it to lowercase
        results = [] # Initialize an empty list to store the search results
        for key, track in lib.library.items():   # Iterate through all tracks in the library
            if query in track.name.lower() or query in track.artist.lower(): # Check if the search query matches either the track name or artist name (case-insensitive)
                results.append(f"{key}. {track.name} - {track.artist} - {track.stars()}")  # Add the matching track's details to the results list in a formatted string
            if results:  # If there are results, display them in the list widget
                set_text(self.list_txt, "\n".join(results)) # Display each result on a new line
            else:
                set_text(self.list_txt, f"No results found for '{query}'") # If no results found, display a "no results" message

        self.status_lbl.configure(text="Search button was clicked!")  # Update the status label to indicate that the search button was clicked   

if __name__ == "__main__":  # Only runs when this file is run as a standalone
    window = tk.Tk()        # Create a TK object
    fonts.configure()       # Configure the fonts
    TrackViewer(window)     # Open the TrackViewer GUI
    window.mainloop()       # Run the window main loop, reacting to button presses, etc
