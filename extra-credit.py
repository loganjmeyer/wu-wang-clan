#This is a trivia game about Paul Resnick! Make additions, modifications, and deletions as necessary.
#The code is purposefully buggy. Refer to PS6 with the hangman game to fix this one!
#Ideas for changes: what happens when the user enters something other than true or false, more trivia, different wording, tests

print 'This is a trivia game about Paul Resnick! If you get 3 answers wrong, you are a big loser.'
def resgame():
    wrong_answers = 0
    right_answers = 0
    while wrong_answers < 3:
        a = raw_input('Paul Resnick met Obama. True or false?')
        if a.upper() == FALSE:
            wrong_answers += 1
        elif a.upper() == TRUE:
            right_answers += 1
            b = raw_input('Paul Resnick taught at U-M for 8 years. True or false?')
            if b.upper() == TRUE:
                wrong_answers += 1
            elif b.upper() == FALSE:
                right_answers += 1
                c = raw_input('Paul Resnick has a treadmill in his office. True or false?')
                if c.upper == FALSE:
                    wrong_answers += 1
                elif c.upper == TRUE:
                    right_answers += 1
    if wrong_answers >= 3:
        print 'You lose!'
    if wrong_answers < 3:
        print 'Congrats, you win! You guessed correctly ' + right_answers + 'times!'
    return 'You were incorrect ' + wrong_answers + 'times, and correct ' + right_answers + 'times.'
  
