'''
in function skip_tuples with t
    return the slice of t
in function main 
    print the return value of skip_tuples
if __name__ == '__main__':
    call the main function
'''
def skip_tuples(t):
    '''
    It has a tuple as input. 
    It returns a new tuple as output
    such as every second element of the input tuple is skipped, starting with the first one.
    '''
    return t[::2]
def main():
    aTuple = ('I', 'am', 'a', 'test', 'tuple')
    print(skip_tuples(aTuple))
if __name__ == '__main__':
    main()