from algorhythm2 import notes, chord, scale, utils
import random


def _is_similar_chord(chord1, chord2):
    notes1 = set(chord1.get_notes())
    notes2 = set(chord2.get_notes())
    shared_notes = notes1 & notes2
    return bool(shared_notes)

def simgen(scale, chord1, chord2=None):
    total_notes = len(scale._get_notes())
    while True:
        next_note = random.randint(0, total_notes - 1)
        new_chord = chord.chord(next_note, scale)
        if chord1.base_note == new_chord.base_note:
            continue
        if chord2 and not _is_similar_chord(chord2, new_chord):
            continue
        if _is_similar_chord(chord1, new_chord):
            return new_chord

def _score_similarity(chord1, chord2):
    notes1 = chord1.get_notes()
    notes2 = chord2.get_notes()
    
    similarity = 0

    for note1 in notes1:
        similarity += note1 - utils.get_closest_element(note1, notes2)

    return similarity, notes1[0] - notes2[0]

def scoresim(scale, chord1, chord2=None):
    total_notes = len(scale._get_notes())

    while True:
        next_note = random.randint(0, total_notes - 1)
        new_chord = chord.chord(next_note, scale)

        if chord1.base_note == new_chord.base_note:
            continue

        sim_net, sim_root = _score_similarity(chord1, new_chord)

        if sim_root > 3 or sim_net > 6:
            continue

        if chord2 and not _is_similar_chord(chord2, new_chord):
            continue
        
        return new_chord

DEFAULT_MATRIX = (
    (False, True, True, True, True, True, True),
    (True, False, True, True, True, True, False),
    (True, True, False, True, True, True, False),
    (False, True, False, False, True, True, True),
    (True, True, True, True, False, True, True),
    (False, True, True, False, True, False, True),
    (False, False, True, True, True, True, False)
)

class MatrixGeneration:
    def __init__(self, matrix=DEFAULT_MATRIX):
        self._matrix = matrix
    
    def __call__(self, scale, chord1, chord2=None):
        total_notes = len(scale._get_notes())

        while True:
            next_note = random.randint(0, total_notes - 1)
            new_chord = chord.chord(next_note, scale)

            scale.get_scale_number(chord1.base_note)

            mt = self._matrix[scale.get_scale_number(chord1.base_note)]
            if not mt[next_note]:
                continue
            
            return new_chord

ALGORITHMS = {
    'simgen': simgen,
    'scoresim': scoresim,
    'matrix': MatrixGeneration()
}

class ChordGenerator:
    def __init__(self, scale, algorithm):
        self._scale = scale
        if type(algorithm) == str:
            algorithm = ALGORITHMS.get(algorithm, simgen)
        self._algorithm = algorithm

    def generate(self, size):
        root_note = random.randint(0, len(self._scale._get_notes()))
        note = root_note

        generated_chords = [chord.chord(note, self._scale)]

        for _ in range(size - 2):
            new_chord = self._algorithm(self._scale, generated_chords[-1])
            generated_chords.append(new_chord)

        generated_chords.append(self._algorithm(self._scale, generated_chords[-1], generated_chords[0]))
        
        return generated_chords