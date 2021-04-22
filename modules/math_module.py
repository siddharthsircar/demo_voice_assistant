import operator

import voice_assistant as assistant


def perform_calculations(command):
    assistant.speak(f'Calculating {command}')
    try:
        assistant.speak(f'Your result is: {eval_binary_expr(*(command.split()))}')
    except:
        assistant.speak('I am unable to calculate. I guess I am not smarter than a 12 year old')
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
