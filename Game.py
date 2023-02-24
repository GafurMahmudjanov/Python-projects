from random import randint
print('Welcome to guess-number game, developed by M.Gafur.')


answer = randint(1,10)

def gessgame():

   while True:

    try:
        num = int(input('\nTry to guess a number between 1 - 10:  '))
        if 0 < num < 11:
            if num == answer:
                print('You are a genius')
                exit_out = input('If you want to finish say \'bye\' if not say \'hey\':  ')
                if exit_out == 'bye' or 'BYE' or 'Bye':
                    break
                elif exit_out == 'hey' or 'HEY' or 'Hey':
                    continue
                else:
                    print('Say it correctly) ')
                    continue

            else:
                print('Try again апчалбек')
                continue
        else:
            input('I said between 1 - 10 ')
            continue
    except ValueError:
        print('Hey апчалбек, i said a number!')
        continue