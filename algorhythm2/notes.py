NOTE_MAPPING = {
    'C': 0,
    0: 'C',
    'C#': 1,
    1: 'C#',
    'Db': 1,
    2: 'D',
    'D': 2,
    'D#': 3,
    3: 'D#',
    'Eb': 3,
    'E': 4,
    4: 'E',
    'F': 5,
    5: 'F',
    'F#': 6,
    6: 'F#',
    'Gb': 6,
    'G': 7,
    7: 'G',
    'G#': 8,
    8: 'G#',
    'Ab': 8,
    'A': 9,
    9: 'A',
    'A#': 10,
    10: 'A#',
    'Bb': 10,
    'B': 11,
    11: 'B'
}

def format_note(note):
    return f'{NOTE_MAPPING[note % 12]}{note // 12}'

def get_note(key):
    if type(key) == str:
        key = NOTE_MAPPING[key]
    return key

class Note:
    NOTES = {}

    def __new__(cls, note):
        note = get_note(note)
        if note not in cls.NOTES:
            obj = super().__new__(cls)
            cls.NOTES[note] = obj
            return obj
        return cls.NOTES[note]

    def __init__(self, note):
        if type(note) == str:
            note = get_note(note)
        self._note = note
    
    def __str__(self):
        return format_note(self._note)
    
    def __repr__(self):
        return self.__str__()
    
    def __int__(self):
        return self._note
    
    def transpose(self, by):
        return Note(self._note + by)

C = Note('C')
C_SHARP = Note('C#')
D_FLAT = Note('Db')
D = Note('D')
D_SHARP = Note('D#')
E_FLAT = Note('Eb')
E = Note('E')
F = Note('F')
F_SHARP = Note('F#')
G_FLAT = Note('Gb')
G = Note('G')
G_SHARP = Note('G#')
A_FLAT = Note('Ab')
A = Note('A')
A_SHARP = Note('A#')
B_FLAT = Note('Bb')
B = Note('B')