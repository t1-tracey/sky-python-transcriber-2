# Sky Python Transcriber 2
This produces sheet music in HTML for the musical instruments in Sky. You can use the QWERT ASDFG ZXCVB as the piano. You can see examples at https://t1-tracey.github.io/sky-music-examples

![the road of trials in Sky SVG piano icons](https://raw.githubusercontent.com/t1-tracey/sky-python-transcriber-2/master/images/road-of-trials-sneak-peek.png)

Sky Python Transcriber 2 supports SVG icons for harp. Thanks to madwurmz for SVGs, and thanks to everyone for support <3

Sky: Light Awaits is an upcoming game by thatgamecompany, currently in beta and soft launch. This is a fan project. No affiliation with thatgamecompany.

# Installation

1. Click the green <kbd>Clone or Download</kbd> button in the top right, and then Download ZIP.

2. Save the folder to a location such as your Desktop and rename it. For the next command, I have the file saved on my Desktop and I've renamed the folder to `sky-transcriber`.

3. To run the program, open a Terminal and change directory to where the folder is — here I would type:

```
cd Desktop/sky-transcriber
```

Then type `python3 transcriber.py` on Mac, or `python transcriber.py` on Windows.

![terminal-with-instructions.png](https://github.com/t1-tracey/sky-python-transcriber-2/blob/master/images/terminal-desktop-directory.png)

# Cheatsheet

## Basics
- Use QWERT, ASDFG, ZXCVB as the music keyboard.
- You can use spaces to separate each block of notes.
- Press Enter each time you want to start transcribing a new line.

![Up and Down song example in Terminal with Q W E R T keys](https://github.com/t1-tracey/sky-python-transcriber-2/blob/master/images/up-and-down-song-example.png)

![Up and Down song render](https://github.com/t1-tracey/sky-python-transcriber-2/blob/master/images/up-and-down-song-render.png)

- Press Enter on a blank line to finish the song. There'll be a file named `(your-song-name).html` in the folder on your Desktop, or whatever folder location you've chosen. Double click on it to open.

## Extras

- Use periods to indicate blank block of notes.

![Mary Had A Little Lamb in CLI](https://github.com/t1-tracey/sky-python-transcriber-2/blob/master/images/mary-had-a-little-lamb-cli.png)

![Mary Had A Little Lamb render](https://github.com/t1-tracey/sky-python-transcriber-2/blob/master/images/mary-had-a-little-lamb-render.png)

- Use dashes to separate sets of colours within a block.

![Dashes to separate colours in CLI](https://github.com/t1-tracey/sky-python-transcriber-2/blob/master/images/colours-cli.png)

![Coloured blocks of notes render](https://github.com/t1-tracey/sky-python-transcriber-2/blob/master/images/colours-render.png)

- The author, original transcriber and key are optional. You can press Enter to skip these.  
