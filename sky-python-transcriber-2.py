# Dash separated list of chords
CHORD_DELIMITER = '-'
NOTE_WIDTH = 45

### Instrument classes

class Harp:

    def __init__(self):

        self.column_count = 5
        self.row_count = 3
        self.keyboard_position_map = {'Q': (0, 0), 'W': (0, 1), 'E': (0, 2), 'R': (0, 3), 'T': (0, 4), 'A': (1, 0), 'S': (1, 1), 'D': (1, 2), 'F': (1, 3), 'G': (1, 4), 'Z': (2, 0), 'X': (2, 1), 'C': (2, 2), 'V': (2, 3), 'B': (2, 4)}
        self.chord_image = {}
        self.highlighted_states_image = []
        self.instrument_type = 'harp'

    def map_letter_to_position(self, letter):

        '''
        Returns a tuple containing the row index and the column index of the note's position.
        '''

        keyboard_position_map = self.get_keyboard_position_map()

        letter = letter.upper()
        if letter in keyboard_position_map.keys():
            return keyboard_position_map[letter] # Expecting a tuple
        else:
            #TODO: Implement support for breaks/empty harps
            #Define a custom InvalidLetterException
            raise Exception('Invalid letter')

    def get_row_count(self):
        return self.row_count

    def get_column_count(self):
        return self.column_count

    def get_keyboard_position_map(self):
        return self.keyboard_position_map

    def set_chord_image(self, chord_image):
        '''
        The chord_image is a dictionary. The keys are tuples representing the positions of the buttons. The values are dictionaries, where each key is the frame, and the value is a Boolean indicating whether the button is highlighted in that frame.
        '''
        #TODO: Raise TypeError if chord_image is not a dict
        self.chord_image = chord_image

    # def update_chord_image(self, index, new_state):
    def append_highlighted_state(self, row_index, column_index, new_state):

        '''
        INCOMPLETE IMPLEMENTATION. new_state is expected to be a Boolean
        '''

        chord_image = self.get_chord_image()

        row = chord_image[row_index]
        highlighted_states = row[column_index]
        highlighted_states.append(new_state)

        chord_image[index] = highlighted_states

        self.set_chord_image(chord_image)


    def get_chord_image(self):
        return self.chord_image

    def parse_chords(self, chords):

        keyboard_position_map = self.get_keyboard_position_map()

        chord_image = {}

        for chord_idx, chord in enumerate(chords):

            # Create an image of the harp's chords
            # For each chord, set the highlighted state of each note accordingly (whether True or False)

            for letter in chord:
                #Except InvalidLetterException
                try:
                    highlighted_note_position = self.map_letter_to_position(letter)
                except Exception:
                    pass
                else:
                    chord_image[highlighted_note_position] = {}
                    chord_image[highlighted_note_position][chord_idx] = True

        self.set_chord_image(chord_image)

    def render_from_chord_image(self, chord_image, note_width, instrument_index):

        harp_render = ''
        harp_render += '<table class=\"harp harp-' + str(instrument_index) + '\">'

        for row_index in range(self.get_row_count()):

            harp_render += '<tr>'

            for column_index in range(self.get_column_count()):

                harp_render += '<td>'

                # Calculate the note's overall index in the harp (0 to 14)
                note_index = (row_index * self.get_column_count()) + column_index

                note_position = (row_index, column_index)

                if note_index % 7 == 0:
                    # Note is a root note
                    note = NoteRoot()
                elif (note_index % self.get_column_count() == 0 or note_index % self.get_column_count() == 2) or note_index % self.get_column_count() == 4:
                    # Note is in an odd column, so it is a circle
                    note = NoteCircle()
                else:
                    # Note is in an even column, so it is a diamond
                    note = NoteDiamond()

                note_render = note.render_from_chord_image(note_width, chord_image, note_position, self.get_instrument_type(), note_index)
                harp_render += note_render
                harp_render += '</td>'

            harp_render += '</tr>'


        harp_render += '</table>'
        return harp_render


    def get_instrument_type(self):
        return self.instrument_type

class NoteRoot:

    def __init__(self):
        self.icon = 'note_root'
        self.highlighted_states = []

    def get_highlighted_states(self):
        return self.highlighted_states

    def set_highlighted_states(self, highlighted_states):
        '''
        highlighted_states is a list of True/False depending on whether the note is highlighted in n-th frame, where n is the index of the item in the list
        '''
        #TODO: raise TypeError if type of highlighted_states is not a list
        self.highlighted_states = highlighted_states

    def render_from_highlighted_states(self, width):

        highlighted_states = self.get_highlighted_states()
        highlighted_classes = []

        for is_highlighted_idx, is_highlighted in enumerate(highlighted_states):
            if is_highlighted:
                highlighted_class = 'highlighted-' + str(is_highlighted_idx)
            else:
                highlighted_class = ''
            highlighted_classes.append(highlighted_class)

        note_render = '<svg class=\"note-root  \" xmlns=\"https://www.w3.org/2000/svg\" width=\"' + str(width) + '\" height=\"' + str(width) + '\" viewBox=\"0 0 91 91\">' #TODO: insert instrument type class .e.g harp-key-0, bass
        note_render += '<path class="instrument-button ' + ' '.join(highlighted_classes).rstrip() + '" d="M90.7 76.5c0 7.8-6.3 14.2-14.2 14.2H14.2C6.4 90.7 0 84.4 0 76.5V14.2C0 6.4 6.3 0 14.2 0h62.3c7.8 0 14.2 6.3 14.2 14.2V76.5z"/>'
        note_render += '<circle cx="45.5" cy="45.4" r="26" class="instrument-button-icon"/>'
        note_render += '<rect x="19.5" y="19.3" transform="matrix(-0.7071 0.7071 -0.7071 -0.7071 109.7415 45.2438)" width="52" height="52" class="instrument-button-icon"/>'
        note_render += '</svg>'
        return note_render

    def render_from_chord_image(self, width, chord_image, position, instrument_type, note_index):

        try:
            note_states = chord_image[position]
        except KeyError:
            highlighted_classes = []
        else:
            highlighted_classes = ['highlighted-' + str(frame_index) for frame_index in note_states.keys()]


        note_render = '<svg class=\"note-root ' + instrument_type + '-button-' + str(note_index) + ' \" xmlns=\"https://www.w3.org/2000/svg\" width=\"' + str(width) + '\" height=\"' + str(width) + '\" viewBox=\"0 0 91 91\">\n'
        note_render += '<path class="instrument-button ' + ' '.join(highlighted_classes).rstrip() + '" d="M90.7 76.5c0 7.8-6.3 14.2-14.2 14.2H14.2C6.4 90.7 0 84.4 0 76.5V14.2C0 6.4 6.3 0 14.2 0h62.3c7.8 0 14.2 6.3 14.2 14.2V76.5z"/>\n'
        note_render += '<circle cx="45.5" cy="45.4" r="26" class="instrument-button-icon"/>\n'
        note_render += '<rect x="19.5" y="19.3" transform="matrix(-0.7071 0.7071 -0.7071 -0.7071 109.7415 45.2438)" width="52" height="52" class="instrument-button-icon"/>\n'
        note_render += '</svg>\n'
        return note_render


class NoteCircle:

    def __init__(self):
        self.icon = 'note_circle'
        self.highlighted_states = []

    def get_highlighted_states(self):
        return self.highlighted_states

    def set_highlighted_states(self, highlighted_states):
        '''
        highlighted_states is a list of True/False depending on whether the note is highlighted in n-th frame, where n is the index of the item in the list
        '''
        #TODO: raise TypeError if type of highlighted_states is not a list
        self.highlighted_states = highlighted_states

    def render_from_chord_image(self, width, chord_image, position, instrument_type, note_index):

        try:
            note_states = chord_image[position]
        except KeyError:
            highlighted_classes = []
        else:
            highlighted_classes = ['highlighted-' + str(frame_index) for frame_index in note_states.keys()]

        note_render = '<svg class=\"note-circle ' + instrument_type + '-button-' + str(note_index) + ' \" xmlns=\"https://www.w3.org/2000/svg\" width=\"' + str(width) + '\" height=\"' + str(width) + '\" viewBox=\"0 0 91 91\">\n'
        note_render += '<path class="instrument-button ' + ' '.join(highlighted_classes).rstrip() + '" d="M90.7 76.5c0 7.8-6.3 14.2-14.2 14.2H14.2C6.3 90.7 0 84.4 0 76.5V14.2C0 6.3 6.3 0 14.2 0h62.3c7.8 0 14.2 6.3 14.2 14.2V76.5z"/>\n'
        note_render += '<circle cx="45.4" cy="45.4" r="25.5" class="instrument-button-icon"/>\n'
        note_render += '</svg>\n'
        return note_render

class NoteDiamond:

    def __init__(self):
        self.icon = 'note_diamond'
        self.highlighted_states = []

    def get_highlighted_states(self):
        return self.highlighted_states

    def set_highlighted_states(self, highlighted_states):
        '''
        highlighted_states is a list of True/False depending on whether the note is highlighted in n-th frame, where n is the index of the item in the list
        '''
        #TODO: raise TypeError if type of highlighted_states is not a list
        self.highlighted_states = highlighted_states

    def render_from_chord_image(self, width, chord_image, position, instrument_type, note_index):

        try:
            note_states = chord_image[position]
        except KeyError:
            highlighted_classes = []
        else:
            highlighted_classes = ['highlighted-' + str(frame_index) for frame_index in note_states.keys()]

        note_render = '<svg class=\"note-diamond ' + instrument_type + '-button-' + str(note_index) + ' \" xmlns=\"https://www.w3.org/2000/svg\" width=\"' + str(width) + '\" height=\"' + str(width) + '\" viewBox=\"0 0 91 91\">\n'
        note_render += '<path class="instrument-button ' + ' '.join(highlighted_classes).rstrip() + '" d="M90.7 76.5c0 7.8-6.3 14.2-14.2 14.2H14.2C6.4 90.7 0 84.4 0 76.5V14.2C0 6.4 6.3 0 14.2 0h62.3c7.8 0 14.2 6.3 14.2 14.2V76.5z"/>\n'
        note_render += '<rect x="22.6" y="22.7" transform="matrix(-0.7071 -0.7071 0.7071 -0.7071 45.3002 109.5842)" width="45.4" height="45.4" class="instrument-button-icon"/>\n'
        note_render += '</svg>\n'
        return note_render


#Unit test, remove later
note_root = NoteRoot()
# print(note_root.render_from_chord_image(45, [True, False, False, False]))

### Note collection class

### Parser

def parse_line(line, delimiter):

    tokens = line.split(delimiter)
    return tokens

print('NEW SONG.')
song_title = input('Song title: ')
print('Use QWERT ASDFG ZXCVB keys as the harp keyboard. Separate chords with \"' + CHORD_DELIMITER + '\".')
song_line = input('Type chord(s): ')

instrument_list = []

while song_line:

    chords = parse_line(song_line, CHORD_DELIMITER)
    harp = Harp()
    harp.parse_chords(chords)

    instrument_list.append(harp)
    song_line = input('Type chord(s): ')

# Render the song

with open(song_title + '.html', 'w+') as song_file:
    song_file.write('<!DOCTYPE html>\n')
    song_file.write('<html>\n')
    song_file.write('<head> <title>' + song_title + '</title> <link href="main.css" rel="stylesheet" /> </head>\n')

    song_file.write('<body>\n')
    song_file.write('<h1> ' + song_title + ' </h1>')

    for instrument_index, instrument in enumerate(instrument_list):

        instrument_chord_image = instrument.get_chord_image()
        instrument_render = instrument.render_from_chord_image(instrument_chord_image, NOTE_WIDTH, instrument_index)
        song_file.write(instrument_render + '\n\n')

    song_file.write('</body>\n')

    song_file.write('</html>\n')
