from algorhythm2 import notes, chord, scale, utils

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

entered_chords = input('Enter roman numerals for chords: ')
chords = [
    chord.chord(user_chord, SCALE)
    for user_chord in entered_chords.split(' ')
]

print(f'Chords: {chords}')

save_as = input('Save as (exclude .mid): ')

utils.generate_basic_aggregiation(save_as, chords)

print('===[CHORDMAKER]===\n\n\n')