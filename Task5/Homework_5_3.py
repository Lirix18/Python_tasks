tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б',  # '10А', '10Б', '9А'
           ]

Tutor_klass = ((tutor, klasses[idx] if idx < len(klasses) else None) for idx, tutor in enumerate(tutors))
print(type(Tutor_klass))
for i in Tutor_klass:
    print(i)
