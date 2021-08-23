from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string
'''
    If you have a problem with geckodriver 
    1.Install geckodriver from this link https://github.com/mozilla/geckodriver/releases
    2.
    For Windows:
    https://stackoverflow.com/questions/42524114/how-to-install-geckodriver-on-a-windows-system
    For Linux:
    https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu
    For MacOS:
    https://www.kenst.com/2016/12/installing-marionette-firefoxdriver-on-mac-osx/
'''


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='C:/geckodriver.exe')
        self.navigate()

    def take_skreenshot(self):
        self.driver.save_screenshot('avito.png')

    def take_recon(self):
        image = Image.open('tel.gif')
        print(image_to_string(image))

    def crop(self, location, size):
        image = Image.open('avito.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']

        image.crop((x, y, x+width, y+height)).save('tel.gif')
        self.take_recon()

    def navigate(self):
        self.driver.get('https://www.avito.ru/moskva/kvartiry/2-k._kvartira_396_m_1116_et._1746055343')

        blocks = self.driver.find_element_by_xpath('//a[@class="button item-phone-button js-item-phone-button button-origin contactBar_greenColor button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card contactBar_height"]')
        blocks.click()
        sleep(3)
        self.take_skreenshot()
        img = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
        location = img.location         # dict {'x': 131, 'y': 521}
        size = img.size                 # dict {'width': 14412, 'height': 1421}

        self.crop(location, size)
def main():
    class_bot = Bot()


if __name__ == '__main__':
    main()