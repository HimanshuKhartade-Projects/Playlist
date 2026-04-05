Problem Statements — Build in this order
1. Create the Node
Design a Node that can hold a song name and knows how to point to the next song in the playlist. It should start with no connection to anything.
2. Create the Playlist skeleton
Design a Playlist that has a starting point (head) and knows which song is currently playing. Initially both should be empty.
3. Add a song to the end
When a user adds a song, it should always go to the end of the playlist. Handle the case where the playlist is completely empty.
4. Display the playlist
Print all songs in order from first to last. If the playlist is empty, tell the user. Show which song is currently playing with a marker like ▶.
5. Play next song
Move to the next song in the playlist. Handle the case where you're already at the last song and there's nothing next.
6. Remove a song by name
Find a song by name and remove it cleanly without breaking the chain. Think carefully about three situations — what if it's the first song, the last song, or somewhere in the middle?
7. Add a song at the beginning
Instead of always adding to the end, let the user add a song that plays first.
8. Search for a song
Tell the user whether a song exists in the playlist and what position it's at (1st, 2nd, etc.)

Stretch Problems
9. Shuffle the playlist
Randomize the order of all songs in the playlist.
10. Save and load
Save the current playlist to a text file and reload it when the program starts again.
11. Build the CLI menu
Wrap everything in a loop where the user can pick options from a menu until they choose to quit.