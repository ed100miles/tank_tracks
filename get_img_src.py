from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")

PATH = '/Users/Ed/Code/Play/tank_tracks/chromedriver'

driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.implicitly_wait(100)
driver.get("https://t.co/xN99euMy8K")

images = driver.find_elements_by_xpath("//img")

for image in images:
    print(image.get_attribute('src'))

# # download the image
# # urllib.urlretrieve(src, "captcha.png")
driver.close()




# headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36", 
#           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
# page = requests.get('https://t.co/xN99euMy8K', headers=headers).content

# print(page)
# print(page)

# soup = BeautifulSoup(page)
# images = soup.findAll('img')
# for image in images:
#     print(image)

# with open("index.html") as fp:
#     soup = BeautifulSoup(fp)

# soup = BeautifulSoup("<html>data</html>")

# # print(response.split('pbs.twimg.com'))