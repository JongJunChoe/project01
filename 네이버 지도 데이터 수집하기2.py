# 네이버 지도 데이터 수집하기
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#### 사이트 불러오는 크롤링 ####
url = 'https://www.naver.com/' #원하는 사이트를 입력하시오
# driver.implicitly_wait(3)
driver = webdriver.Chrome('c:\chromedriver.exe')
driver.get(url)

# store = []
name = []
# menu = []
# rating = [] 

for name in range(0,10):
    #### 네이버 맛집 검색 1번째, 한식으로 검색하기 ####
    search_box = driver.find_element_by_css_selector("input#query") # 검색창 마우스 클릭
    search_box.send_keys("남부터미널 한식 맛집") # 원하는 검색어 입력
    driver.find_element_by_xpath('//*[@id="search_btn"]').click() # 검색 버튼 클릭

    ####검색 리스트 중 식당명, 대표메뉴, 별점 ####
    store = driver.find_elements_by_css_selector("div.list_area")
    name = driver.find_element_by_css_selector((".name").text
                                               
#     menu = driver.find_element_by_css_selector("span.category").text
#     rating =driver.find_element_by_css_selector("span.rating".text
# print(name, menu, rating)

####검색 리스트를 다음 페이지로 넘기기 ####
# driver.find_element_by_xpath('//*[@id="place_main_ct"]/div/section[1]/div/div[2]/div[4]/div/a[2]').click()
