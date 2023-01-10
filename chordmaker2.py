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

chord_generator = generation.ChordGenerator(SCALE, 'simgen')

while True:
    save_as = input('Save as (exclude .mid): ')

    if save_as:
        break

while True:
    try:
        amount = int(input('How many midi files?'))
        for _ in range(amount):
            chords = chord_generator.generate(8)
            print(f'Chords: {chords}')
            utils.generate_basic_midi(f'{save_as}{_}', chords)
        break
    except:
        pass

print('===[CHORDMAKER]===\n\n\n')