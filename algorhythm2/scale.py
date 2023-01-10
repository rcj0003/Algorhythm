from algorhythm2 import notes

SCALE_MAJOR = (
    notes.C,
    notes.D,
    notes.E,
    notes.F,
    notes.G,
    notes.A,
    notes.B,
)

SCALE_MINOR = (
   notes.C,
   notes.D,
   notes.E_FLAT,
   notes.F,
   notes.G,
   notes.A_FLAT,
   notes.B, 
)

SCALE_CHROMATIC = (
    notes.C,
    notes.C_SHARP,
    notes.D,
    notes.D_SHARP,
    notes.E,
    notes.F_SHARP,
    notes.G,
    notes.G_SHARP,
    notes.A,
    notes.A_SHARP,
    notes.B
)

SCALES = {
    'major': SCALE_MAJOR,
    'minor': SCALE_MINOR,
    'chromatic': SCALE_CHROMATIC
}

class Scale:
    def __init__(self, key, octave, signature):
        if type(key) == str:
            key = notes.NOTE_MAPPING[key]
        if type(key) == notes.Note:
            key = int(key)
        self._signature = signature
        self._notes = [int(_note) + key + (octave * 12) for _note in signature]
        self._note_count = len(self._notes)
    
    def __getitem__(self, index):
        return self._notes[(index % self._note_count)] + (12 * (index // self._note_count))

    def _get_notes(self):
        return self._notes
    
    def get_scale_number(self, note):
        note %= 12
        for _ in range(len(self._notes)):
            if self[_] % 12 == note:
                return _
        return None
