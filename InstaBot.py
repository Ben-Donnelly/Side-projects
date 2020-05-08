from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, ui


class GetDifference:
    def __init__(self, username, pw):

        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

        # Username variable for use in methods
        self.username = username

        # Login page
        self.driver.get("https://www.instagram.com/accounts/login/")
        # Login
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))).send_keys(self.username)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))).send_keys(pw)

        self.driver.find_element_by_tag_name('form').submit()

        # Deals with pop-up
        ui.WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

    def get_unfollowers(self):
        # Your home page
        which = input("Enter username of person to check\nNote page must be public or else followed by user\nHit enter to use your own:")

        self.driver.get(f'https://www.instagram.com/{self.username}/' if which == "" else f'https://www.instagram.com/{which}/')
        print("Getting data, this may take a while depending on numbers...")

        ui.WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/following')]"))).click()
        following = self.get_names()

        ui.WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/followers')]"))).click()
        followers = self.get_names()

        not_following_back = [user for user in following if user not in followers]
        # unpack and print
        print(*not_following_back, sep="\n")

    def get_names(self):

        last, current = 0, 1

        # Dialog is dynamic, need to figure out when we are at bottom/Scroll limit
        while last != current:
            last = current

            # Sleep is needed, otherwise scrolling happens too fast and last == current
            # 0.75 delay is minimum I have found to return faithful results
            sleep(.75)

            # Scroll and return depth of scroll
            current = self.driver.execute_script('''
                             var forScroll = document.querySelector('div[role="dialog"] .isgrP');
                             forScroll.scrollTop = forScroll.scrollHeight
                             return forScroll.scrollHeight
                         ''')
        # for anchor tags in that scroll (gets names)
        links = self.driver.find_elements_by_tag_name('a')
        names = [name.text for name in links]

        # Some ''s are returned, remove these
        names[:] = [v for v in names if v != '']

        # close button
        self.driver.find_element_by_css_selector(".wpO6b ").click()
        return names


uName = input("Username: ")
pWord = input("Password: ")

my_bot = GetDifference(uName, pWord)
my_bot.get_unfollowers()
