class Playlist:
    def __init__(self, title):
        self.title = title
        self.playlist = []
    def load_songs(self, filename):
        lines = []
        with open(filename, "r") as f:
            lines = f.readlines()
        for line in lines:
            list = line.split(",")
            self.playlist.append(Song(list[0], list[1], list[2]))
    def add_song(self, music):
        self.playlist.append(music)
    def print_playlist(self):
        for i in range(len(self.playlist)):
            print(self.playlist[i])
    def get_total_duration(self):
        x = 0
        for i in range(len(self.playlist)):
            x += int(self.playlist[i].duration)
        return x
    def find_by_artist(self, name):
        for i in range(len(self.playlist)):
            if self.playlist[i].artist == name:
                print("Found! Song(s) by desired artist is/are: ", self.playlist[i])
                continue
            else:
                continue

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    def __str__(self):
        return self.title + " " + self.artist + " " + str(self.duration)


def main():
    playlist = Playlist("My Playlist")
    playlist.load_songs("songs.csv")
    playlist.add_song(Song("My Fav Song", "Megabytes", 250))
    playlist.print_playlist()
    playlist.get_total_duration()
    playlist.find_by_artist("Null Pointer")

main()