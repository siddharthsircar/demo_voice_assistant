import operator

import jarvis_voice_assistant as jarvis


def perform_calculations(command):
    jarvis.speak(f'Calculating {command}')
    try:
        jarvis.speak(f'Your result is: {eval_binary_expr(*(command.split()))}')
    except:
        jarvis.speak('I am unable to calculate. I guess I am not smarter than a 12 year old')
        pass

def get_operator(op):
    return {
        '+' : operator.add, #plus
        '-' : operator.sub,  # subtract
        'x' : operator.mul, #multiply
        'divided' : operator.__truediv__, # divided
    }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator(oper)(op1,op2)
