import json
import os.path
import struct
import sys

import selenium.webdriver.support.expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def download(movie_name, movie_year):
    try:
        options = webdriver.ChromeOptions()
        options.binary_location = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        chrome_driver_binary = "C:\\chromedriver.exe"
        prefs = {'download.default_directory': 'D:\\Downloads', 'download.prompt_for_download': False}
        options.add_experimental_option('prefs', prefs)
        browser = webdriver.Chrome(chrome_driver_binary, options=options)
        browser.implicitly_wait(10)
        movie_name = str(movie_name).lower().replace(' ', '-')
        movie_year = str(movie_year)

        url = "https://www.yts.mx/movies/{0}-{1}".format(movie_name, movie_year)
        browser.get(url)

        wait = WebDriverWait(browser, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="movie-poster"]/a')))
        downloadButton = browser.find_element_by_class_name('torrent-modal-download')

        downloadButton.click()

        try:
            magnet = browser.find_element_by_xpath('//a[contains(@title, "1080p Magnet")]')
            magnet.click()
        except:
            magnet = browser.find_element_by_xpath('//a[contains(@title, "720p Magnet")]')
            magnet.click()

        browser.refresh()

        startTorrent = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/button[1]')
        startTorrent.click()

        while browser.find_elements_by_class_name('torrentStat')[0].text != 'Seeding':
            continue

        download_list = len(browser.find_elements_by_xpath('//*[@id="root"]/div/div[3]/div/table/tbody/*'))
        for i in range(0, download_list):
            saveToDownloads = browser.find_element_by_xpath(
                '//*[@id="root"]/div/div[3]/div/table/tbody/tr[{0}]/td[3]/a'.format(i + 1))
            saveToDownloads.click()

            fileName = saveToDownloads.get_attribute('download')
            downloadPath = 'D:\\Downloads\\{}'.format(fileName)

            while not os.path.exists(downloadPath):
                continue

        return "success"
    except:
        return "failure"
    finally:
        browser.quit()


def send_message(encoded_message):
    sys.stdout.buffer.write(encoded_message['length'])
    sys.stdout.buffer.write(encoded_message['content'])
    sys.stdout.buffer.flush()


def get_message():
    raw_length = sys.stdin.buffer.read(4)

    if not raw_length:
        sys.exit(0)
    message_length = struct.unpack('=I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode("utf-8")
    return json.loads(message)


def encode_message(message_content):
    encoded_content = json.dumps(message_content).encode("utf-8")
    encoded_length = struct.pack('=I', len(encoded_content))
    return {'length': encoded_length, 'content': struct.pack(str(len(encoded_content)) + "s", encoded_content)}


def delimit(message):
    msg = message.split('*', 1)
    return msg[0], msg[1]


def Main():
    message = str(get_message())
    movie_name, movie_year = delimit(message)
    status = download(movie_name, movie_year)
    send_message(encode_message(status))


if __name__ == '__main__':
    Main()
