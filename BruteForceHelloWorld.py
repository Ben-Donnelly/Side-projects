from time import sleep
from sys import stdout


def proper(s, cl):
    for i in chars:
        for j in range(14, 500):  # CR, LF e.t.c. cause problems so start from 14
            while cl[0] is not i:
                cl[0] = chr(j)
                if cl[0] == i:
                    s += i
                    stdout.write("\b" * (len(chars) - 2))  # \b for backspace if correct char * (len... stops repetition
                    stdout.write("\b" + s)
                    stdout.flush()  # flush sys
                    # sleep(.01)

                else:
                    stdout.write("\b" + cl[0])  # Otherwise delete char and try again
                    stdout.flush()
                    sleep(.01)

                break

        cl[0] = chr(0)  # Reset char for double letter case


def random_def(s, cl):
    for i in chars:
        for j in range(14, 500):  # Covers most characters
            while cl[0] is not i:
                cl[0] = chr(j)
                if cl[0] == i:
                    s += i
                    stdout.write("\b" * (len(chars) - 2))
                    stdout.write("\b" + s)
                    stdout.flush()
                    sleep(.01)

                else:
                    stdout.write("\b" + cl[0])
                    stdout.flush()
                    sleep(.01)

                break

        cl[0] = chr(0)


if __name__ == '__main__':
    chars = input("Enter word:")
    choice = input("'b' Straight brute force, 'r' for random:")

    char_list = elements = [x[:] for x in [' '] * len(chars)]
    sentence = ''
    if choice == 'b':
        print("Brute forced:\n")
        proper(sentence, char_list)
    else:
        print("Random:\n")
        random_def(sentence, char_list)
