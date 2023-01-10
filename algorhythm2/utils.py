import re


def get_closest_element(element, iterable):
    closest = iterable[0]

    for item in iterable[1:]:
        if abs(element - item) < abs(element - closest):
            closest = item
    
    return closest


def get_closest_element_index(element, iterable):
    closest = iterable[0]

    for i in range(len(iterable) - 1):
        item = iterable[i + 1] 
        if abs(element - item) < abs(element - closest):
            closest = i
    
    return closest

def generate_basic_midi(file_name, chords):
    from mido import Message, MidiFile, MidiTrack

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=12, time=0))
    
    for chord in chords:
        notes = chord.get_notes()
        for note in notes:
            track.append(Message('note_on', note=note, velocity=64))
        track.append(Message('note_off', note=notes[0], time=mid.ticks_per_beat))
        for note in notes[1:]:
            track.append(Message('note_off', note=note, velocity=64))
    
    mid.save(f'output/{file_name}.mid')

KEY_SCALE_REGEX = re.compile('(C#|Db|D#|Eb|G#|Ab|A#|Bb|C|D|E|F|G|A|B)(.*)', flags=re.IGNORECASE)

def generate_basic_aggregiation(file_name, chords):
    from mido import Message, MidiFile, MidiTrack

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=12, time=0))
    
    for chord in chords:
        notes = chord.get_notes()

        for note in notes:
            track.append(Message('note_on', note=note, velocity=64))
            track.append(Message('note_off', time=mid.ticks_per_beat))
    
        track.append(Message('note_on', note=notes[-2], velocity=64))
        track.append(Message('note_off', time=mid.ticks_per_beat))

    mid.save(f'output/{file_name}.mid')

def generate_basic_aggregiation2(file_name, chords):
    from mido import Message, MidiFile, MidiTrack

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=12, time=0))

    last_note = None
    current_note = 0
    
    for chord in chords:
        notes = chord.get_notes()
        if last_note == None:
            last_note = notes[-2]
        else:
            current_note = get_closest_element_index(last_note, notes)
        
        for note in range(len(notes)):
            note_value = notes[(note + current_note) % len(notes)]
            track.append(Message('note_on', note=note_value, velocity=64))
            print(mid.ticks_per_beat)
            track.append(Message('note_off', time=int(mid.ticks_per_beat * 0.25)))
            last_note = note_value

    mid.save(f'output/{file_name}.mid')

def get_key_and_scale(name):
    match = KEY_SCALE_REGEX.match(name)
    if match:
        return match.group(1), match.group(2).strip().lower()
    return None, None

