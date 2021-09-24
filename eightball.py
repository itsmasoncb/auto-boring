import random
import time

def getAnswer(answerNumber): # Code being defined but NOT called yet.
    if answerNumber == 1:
        return 'It is absolutely certain.'
    elif answerNumber == 2:
        return 'It is very likely.'
    elif answerNumber == 3:
        return 'Yes.'
    elif answerNumber == 4:
        return 'Quite hazy the future is. Ask differently, you shall.' # Yoda has other things on his mind.
    elif answerNumber == 5:
        return 'I am not so sure that is a good idea.'
    elif answerNumber == 6:
        return 'Quite Doubtful.'
    elif answerNumber == 7:
        return 'Outlook... unfavorable.'
    elif answerNumber == 8:
        return 'No chance.'
    elif answerNumber == 9:
        return 'Absolutely Impossible.'

print() 
print('Ask a question to the magic 8 ball.') # Wait for input, mean to use the question variable later.
question = str(input())
time.sleep(1)

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
print() # Just for easy white space.