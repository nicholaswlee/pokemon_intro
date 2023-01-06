import time, sys
def sprint(string, seconds=0.01):
    '''
    Prints slowly

    Arguments
    ----------
    string - string to print

    seconds - optional, delay between each character

    '''
    for s in string:
        sys.stdout.write(s)
        #print(s, end="")
        sys.stdout.flush()
        time.sleep(seconds)
    print()
def sinput(string, seconds=0.01):
    '''
    Prints slowly and takes input

    Arguments
    ----------
    string - string to print
    
    seconds - optional, delay between each character
    '''
    for s in string:
        sys.stdout.write(s)
        #print(s, end="")
        sys.stdout.flush()
        time.sleep(seconds)
    return input()