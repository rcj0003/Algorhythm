from algorhythm2 import notes

class ChordType:
    MAJOR = 'Major', 'maj', {0, 4, 7}
    MINOR = 'Minor', 'min', {0, 3, 7}
    AUGMENTED = 'Augmented', 'aug', {0, 4, 8}
    DIMINISHED = 'Diminished', '*', {0, 3, 6}

    TYPES = (
        MAJOR,
        MINOR,
        AUGMENTED,
        DIMINISHED
    )

    @classmethod
    def determine_type(cls, chord):
        chord_notes = {
            chord_note - chord.base_note
            for chord_note in chord.get_notes()
        }

        for chord_type in cls.TYPES:
            if chord_notes == chord_type[2]:
                return chord_type
        
        return None

class Chord:
    def __init__(self, notes):
        self.base_note = notes[0]
        self._notes = notes
        self._type = ChordType.determine_type(self)
    
    def __str__(self):
        return f'{notes.format_note(self.base_note)} {self._type[1]}'
    
    def __repr__(self):
        return self.__str__()

    def get_notes(self):
        return self._notes
    
    def transpose(self, by):
        return self.__new__([
            note + by
            for note in self._notes
        ])

def basic3(base_note, scale):
    if type(base_note) == notes.Note:
        base_note = int(base_note)
    return Chord(notes=[
        scale[base_note],
        scale[base_note + 2],
        scale[base_note + 4]
    ])

CHORD_NUMERALS = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii']

def chord(numeral, scale):
    if type(numeral) == int:
        return basic3(numeral, scale)
    numeral = numeral.lower()
    for i in range(len(CHORD_NUMERALS)):
        if numeral == CHORD_NUMERALS[i]:
            return basic3(i, scale)
    return None