def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
        print(symbol * width)


for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        print(sym, w, h)
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] - [%(asctime)s] -  [%(message)s]')

logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s%%)' % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % n)
    return total


print(factorial(5))
logging.debug('End of program')
