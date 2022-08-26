from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def url_conn(_url_list):
	options = Options()
	options.add_argument('headless'); # headless는 화면이나 페이지 이동을 표시하지 않고 동작하는 모드

	# webdirver 설정(Chrome, Firefox 등)
	chromedriver_autoinstaller.install()
	#driver = webdriver.Chrome(options=options) # 브라우저 창 안보이기
	driver = webdriver.Chrome() # 브라우저 창 보이기

	# 크롬 브라우저 내부 대기 (암묵적 대기)
	driver.implicitly_wait(5)

	# 브라우저 사이즈
	driver.set_window_size(1920,1280)

	# 페이지 이동(열고 싶은 URL)
	for _url in _url_list:
		#print("conn: " + _url)
		driver.get(_url)

	time.sleep(2)
	# 브라우저 종료
	driver.close()       

def read_url_list(_file_path):
        f = open(_file_path, 'r')
        url_list = list()
        
        lines = f.readlines()
        
        for line in lines:
                line = line.strip()
                if 'http' in line:
                        url_list.append(line)

        f.close()
        return url_list

url_conn(read_url_list("UrlList.txt"))

