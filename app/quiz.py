questions = [
    {
        "Question": "How many Cc's does HD Iron have?:",
        "Options": [1000, 883, 1600],
        "Answer": 883
    },
    {
        "Question": "How many Cc's does HD Dyna have?:",
        "Options": [1000, 883, 1600],
        "Answer": 1600
    },
    {
        "Question": "How many Cc's does HD Breakout have?:",
        "Options": [1000, 883, 1600, 1800],
        "Answer": 1800
    },
]

right_answers = 0

for question in questions:
    print('Question:',question["Question"])
    print()

    options = question['Options']

    for i, option in enumerate(options):
        print(f'[{i}]', option)
    print()

    choice = input('Choose an option: ')

    right = False
    choice_int = None

    qtd_options = len(options)

    if choice.isdigit():
        choice_int = int(choice)

    if choice_int is not None:
        if choice_int >=0 and choice_int < qtd_options:
            if options[choice_int] == question['Answer']:
                right = True
    
    print()
    if right:
        right_answers += 1
        print('You choose the right answer!!')
    else:
        print('Sorry, try again')

    print('Score', right_answers, 'right answers of', len(questions), 'questions.')
    print()