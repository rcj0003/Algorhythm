from algorhythm2 import notes, chord, scale, utils
from algorhythm2.chord import generation

key, signature = None, None

print('\n\n\n===[CHORDMAKER]===')

while True:
    try:
        key, signature = utils.get_key_and_scale(input('Enter key signature (ex: C Major): '))
        break
    except:
        pass

print(f'Signature: {key} {signature}')

SCALE = scale.Scale(
    key=notes.Note(key),
    octave=3,
    signature=scale.SCALES[signature]
)

chord_generator = generation.ChordGenerator(SCALE, 'matrix')
chords = chord_generator.generate(16)

print(f'Chords: {chords}')

save_as = input('Save as (exclude .mid): ')

utils.generate_basic_aggregiation2(save_as, chords)

print('===[CHORDMAKER]===\n\n\n')