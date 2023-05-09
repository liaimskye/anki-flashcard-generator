import genanki
from random import randint

subject_aspects = [
    ('Syntax', 'Python has a simple and easy-to-learn syntax, which makes it ideal for beginners.'),
    ('Data types', 'Python supports various data types such as integers, floats, strings, lists, tuples, and dictionaries.'),
    ('Control structures', 'Python has control structures such as if-else statements, loops, and functions, which are used to control the flow of a program.'),
    ('Libraries', 'Python has a vast collection of libraries that make programming easier and faster.'),
    ('Object-oriented programming', 'Python supports object-oriented programming, which is a programming paradigm that focuses on creating objects that have properties and methods.'),
    ('Interpreted language', 'Python is an interpreted language, which means that the code is executed line by line rather than compiled before execution.'),
    ('Community', 'Python has a large and supportive community of developers who contribute to the language, create libraries and tools, and provide help and support to beginners.')
]

model_id = randint(1000000,9999999)
model = genanki.Model(
    model_id,
    'Python intermediate folders',
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

deck_id =2059400110
deck = genanki.Deck(deck_id, 'Python intermediate')

for dir_name, description in subject_aspects:
    note = genanki.Note(model = model, fields=[dir_name, description])
    deck.add_note(note)

genanki.Package(deck).write_to_file('Python_intermediate.apkg')