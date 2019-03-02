import requests
import re

"""This is class to give me raport about my favouirite website. """

class Raport():

    def __init__(self):
        self.temperature = None
        self.atmospheric_conditions = None
        self.precipitation = None

    def crawl(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77-1 Safari/537.36'}
        response = requests.get(url, headers=headers)
        return(response.content.decode("UTF-8"))

    def weater(self, url):
        html = self.crawl(url)
        """Read temperature from webpage"""
        self.temperature = re.findall('(?:span class="wob_t" id="wob_tm" style="display:inline">)(.*?)</span>', html)[0]
        """Read atmospheric conditions"""
        self.atmospheric_conditions = re.findall('(?:<span class="vk_gy vk_sh" id="wob_dc">)(.*?)</span>', html)[0]
        """Read precipitation"""
        self.precipitation = re.findall('(?:<span id="wob_pp">)(.*?)</span>', html)[0]


    """If you write phrase in google information can be on centre side or in right. This functions takes info from bouth of sides"""

    def info_centre(self, about):
        html = self.crawl("https://www.google.pl/search?ei=HXt6XO7lG8j2qwGp3buICA&q=" + about)
        phrase = re.findall('(?:<span class="ILfuVd">)(.*?)</span>', html)[0]
        lst = re.findall('[^<>/ ]+', phrase)
        num = lst.count('b')
        while num > 0:
            lst.remove('b')
            num -= 1
        return(" ".join(lst))

    def info_right(self, about):
        html = self.crawl("https://www.google.pl/search?ei=HXt6XO7lG8j2qwGp3buICA&q=" + about)
        return(re.findall('(?:<div><h3 class="bNg8Rb">Opis</h3><span>)(.*?)</span>', html)[0])










