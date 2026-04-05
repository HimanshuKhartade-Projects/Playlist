class Node:
    def __init__(self,song):
        self.song = song
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.play_list = []

    def add_song_at_end(self):
        que = str(input("Do you want to add new songs into the playlist? (y/N): ")).upper()
        count = 0
        if que == "Y":
            count = int(input("How many songs so you want to add? - "))
            for _ in range (count):
                new_song = input("Type the song name you want to add and hit enter: ")
                new_node = Node(new_song)
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                else:
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = new_node
                self.length +=1
                self.play_list.append(new_song)
        else:
            print("Thank you for answering the question\nHave a great day!")
        
    def add_song_at_beginning(self):
        new_song = input("Type the song name you want to add and hit enter: ")
        new_node = Node(new_song)
        temp = self.head
        temp.prev = new_node
        self.head = new_node
        self.head.next = temp
        self.length +=1
        self.play_list.insert(0, new_song)

    def print_songs(self):
        self.play_list = []
        que = str(input("Do you want to see the full list of the songs(Y/N): ")).upper()
        if que == "Y":
            try:
                temp = self.head
                while temp is not None:
                    print(temp.song)
                    self.play_list.append(temp.song)
                    temp = temp.next
            except AttributeError:
                pass
        else:
            print("Thank you")
        print(self.play_list)

    def play_next(self):
        self.temp = self.head
        self.count = 0
        print(f"The current song playing: {self.head.song}")
        for _ in range(len(self.play_list)-1):
            que = str(input("Type 'next' if you want to play next song: ")).upper()
            if que == "NEXT":
                self.temp = self.temp.next
                print(f"The current song playing: {self.temp.song}")
                self.count +=1
            else:
                break
        if self.temp == self.tail:
            print("Playlist is over")
        else:
            print(f"Invalid input\nEnjoy the song {self.temp.song}")

    def remove_song(self):
        re = input("Would you like to remove song from list (y/N): ").upper()
        temp  = self.head
        if re == "Y":
            que = input("Enter the name of the song: ")
            while temp is not None:
                if temp.song == que:
                    if self.head == self.tail:
                        self.head = None
                        self.tail = None
                    elif temp == self.head:
                        self.head = temp.next 
                        self.head.prev = None
                    elif temp == self.tail:
                        self.tail = temp.prev
                        self.tail.next = None
                    else:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev

                temp = temp.next
            print(f"Successfully removed the song: {que}")
            self.length -= 1
            self.print_songs()
    
    def search_for_song(self):
        que = input("Enter the song name that you are looking for in this playlist")
        if que in self.play_list:
            print(f"{que} song exists")
        else:
            print(f"Sorry,{que} song does not exists in the playlist") 
    
    def save_all_songs(self):
        with open("Playlist.txt","w") as f:
            for song in self.play_list:
                f.write(song + "\n")
            print("File is saved")

            

    def main(self):
        print(f"The current playlist is empty")
        que1 = input("Type c if you want to clear the playlist: ")
        if que1 == "c":
            print(f"The current song playing is {self.head}")
            if self.head == None:
                print("Playlist is empty")
        else:
            self.add_song_at_end()
            self.add_song_at_beginning()
            self.print_songs()
            self.play_next()
            self.remove_song()
            self.search_for_song()
            self.save_all_songs()
        

p = Playlist()
p.main()

        
        