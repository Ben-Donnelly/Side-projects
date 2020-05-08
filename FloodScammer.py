from requests import post
from random import choice, randint, choices, sample, randrange
from string import digits, ascii_letters
from json import loads
from time import sleep


class Choices:
    emails = ["@gmail.com", "@yahoo.com", "@outlook.com", "@icloud.com", "@hotmail.com", "live.com"]

    nameSeparators = [".", "_", "-", ""]  # Common separators

    def name_sep(self):
        return choice(self.nameSeparators)

    def email_choice(self):
        return choice(self.emails)

    @staticmethod
    def name_cases(s):
        # As weights needed, choises returns a single element list
        return choice((s[0].lower(), s[0].title()))

    @staticmethod
    def name_extra():
        birthYears = str(randint(1985, 2010))  # Full year e.g 1997

        choice1 = ''.join(choice(digits) for _ in range(randint(0, 4)))  # Between 0 and 4 random digits

        choice2 = birthYears[2:]  # Shortened year e.g 97

        return choice([birthYears, choice1, choice2, ""])  # One of above choices or a blank

    @staticmethod
    def password_choices(name_u):
        chars = ascii_letters + digits + '!@~#$&%()'

        rand2Char = ''.join(choice(chars) for _ in range(randint(0, 2)))  # Random chars up to 2

        randDict = choice(dictionary)  # Random dict word

        rand4Char = ''.join(choice(chars) for _ in range(randint(1, 4)))  # Random chars up to 4

        rName = ''.join(choices(names))  # Random Name

        Uname = ''.join(name_u)  # Users Name

        RandDigits = ''.join(choice(digits) for _ in range(randint(1, 4)))  # Random digits up to 4

        metaChoices = [rand2Char, randDict, rand4Char, rName, Uname, RandDigits]

        return ''.join(sample(metaChoices, k=randrange(3, 5)))  # Random 3 - 5 of the parameters


myChoice = Choices()


url = ''

names = loads(open('C:\\xampp\\htdocs\\names.json').read())
lastNames = loads(open('C:\\xampp\\htdocs\\lastName.json').read())
dictionary = loads(open('C:\\xampp\\htdocs\\dictForPasswords.json').read())

for i in range(10000):
    sleep(randint(0, 10))  # Sleep to avoid rate limiting, potential DOS, general suspicion etc.

    fn = choice(names)  # First name
    full_name = f"{fn} {choice(lastNames)}"
    random_word_email = ' '.join(sample(dictionary, 2))

    x = myChoice.name_cases(choices([full_name, random_word_email], [0.7, 0.3], k=1))
    # Weighted 70-30 in favour of a name email over a random word one

    def_name = myChoice.name_sep().join(x.split(" "))  # Separator to replace blank

    uname = def_name + myChoice.name_extra() + myChoice.email_choice()

    password = myChoice.password_choices(fn)

    # For website, could just print out as below

    # post(url, allow_redirects=False, data={
    #     'Email': username,
    #     'Password': password,
    #     'submit': True  # This is only needed if there is a submit button on form
    #                     # i.e if something extra shows up in the google 'preserve log'
    # })

    print(f"{i} username: {uname}  password: {password}")
