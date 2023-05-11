import genanki
from random import randint
from id_generator import id_create
from file_reader import txt_to_dict

OOP_aspects = txt_to_dict("subject_file.txt")


model_id,deck_id = id_create()
model = genanki.Model(
    model_id,
    'Python OOP folders',
    fields=[
        {'name': 'Directory'},
        {'name': 'Description'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Directory}}',
            'afmt': '{{Description}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Description}}',
            'afmt': '{{Directory}}',
        },
    ])


deck = genanki.Deck(deck_id, 'Python OOP')

for dir_name, description in OOP_aspects:
    note = genanki.Note(model = model, fields=[dir_name, description])
    deck.add_note(note)

genanki.Package(deck).write_to_file('Python_OOP.apkg')