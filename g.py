import re
def insert_spaces(text):
    pattern = r'([a-z])([A-Z])'
    return re.sub(pattern, r'\1 \2', text)


print(insert_spaces('pyThon'))

def task9():
    '''
    Write a Python program to insert spaces between words starting with capital letters.
    '''

    text = input()


    print(re.sub(r'([A-Z])', lambda s: ' '+s.group(1), text).lstrip())

task9()

        