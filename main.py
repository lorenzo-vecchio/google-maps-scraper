from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


# Creating a webdriver instance
driver = webdriver.Chrome("C:/Users/your-path/chromedriver.exe")
# Opening the url we have just defined in our browser
driver.get("https://www.google.it/maps/search/ristoranti+isola+milano/")
# Accepts google terms and conditions
driver.find_element_by_xpath('/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/form[2]/div/div/button/span').click()
# Waiting for the page to load
time.sleep(5)
# Finding the part of the website that contains the results
scrollable_list = driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
i = 0
while i == 0:
    time.sleep(4)
    #scrolls down
    scrollable_list.send_keys(Keys.END)
    # If it finds the element that appears when we finished results returns true if it doesn't returns false
    if (driver.find_elements_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[243]/div')):
        i = 1
scrollable_list.send_keys(Keys.HOME)
# Gets all of the results
elements = driver.find_elements_by_css_selector('#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div')
# Getting the number of results
print("Found: ", len(elements), " elements")
# Inizialazing an array for every data we want to scrape
restaurant_name = []
stars = []
reviews = []
restaurant_type = []
address = []
website = []
phone_number = []
price = []
# Looping through the results
for item in range(len(elements)):
    # clicking result to get more detailed informations ________________________________
    try:
        element_path = f'#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div:nth-child({item+1}) > div > a'
        driver.find_element_by_css_selector(element_path).click()
    except:
        pass
    # Waiting for element to load
    time.sleep(2)
    # __________________________________________________________________________________
    restaurant_name_path = '#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.TIHn2 > div.tAiQdd > div.lMbq3e > div:nth-child(1) > h1 > span:nth-child(2)'
    try:
        r_n = driver.find_element_by_css_selector(restaurant_name_path).text
        restaurant_name.append(r_n)
    except:
        restaurant_name.append(' ')
    # __________________________________________________________________________________
    stars_path = '#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.TIHn2 > div.tAiQdd > div.lMbq3e > div.LBgpqf > div > div.fontBodyMedium.dmRWX > div.F7nice.mmu3tf > span:nth-child(1) > span > span:nth-child(1)'
    try:
        s = driver.find_element_by_css_selector(stars_path).text
        stars.append(s)
    except:
        stars.append(' ')
    # __________________________________________________________________________________
    reviews_path = '#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.TIHn2 > div.tAiQdd > div.lMbq3e > div.LBgpqf > div > div.fontBodyMedium.dmRWX > div.F7nice.mmu3tf > span:nth-child(2) > span:nth-child(1) > span'
    try:
        r = driver.find_element_by_css_selector(reviews_path).text
        reviews.append(r)
    except:
        reviews.append(' ')
    # __________________________________________________________________________________
    restaurant_type_path = '#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.TIHn2 > div.tAiQdd > div.lMbq3e > div.LBgpqf > div > div:nth-child(2) > span:nth-child(1) > span:nth-child(1) > button'
    try:
        r_t = driver.find_element_by_css_selector(restaurant_type_path).text
        restaurant_type.append(r_t)
    except:
        restaurant_type.append(' ')
    # __________________________________________________________________________________
    address_path = '#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div:nth-child(11) > div:nth-child(3) > button > div.AeaXub > div.rogA2c > div.Io6YTe.fontBodyMedium'
    try:
        addr = driver.find_element_by_css_selector(address_path).text
        address.append(addr)
    except:
        address.append(' ')
    # __________________________________________________________________________________
    website_path = '#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div:nth-child(11) > div:nth-child(7) > a > div.AeaXub > div.rogA2c.ITvuef > div.Io6YTe.fontBodyMedium'
    try:
        web = driver.find_element_by_css_selector(website_path).text
        website.append(web)
    except:
        website.append(' ')
    # __________________________________________________________________________________
    phone_number_path = '#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div:nth-child(11) > div:nth-child(6) > button > div.AeaXub > div.rogA2c > div.Io6YTe.fontBodyMedium'
    try:
        p_n = driver.find_element_by_css_selector(phone_number_path).text
        phone_number.append(p_n)
    except:
        phone_number.append(' ')
    # __________________________________________________________________________________
    price_path = '#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.TIHn2 > div.tAiQdd > div.lMbq3e > div.LBgpqf > div > div.fontBodyMedium.dmRWX > span:nth-child(4) > span > span > span:nth-child(2) > span:nth-child(1) > span'
    try:
        pri = driver.find_element_by_css_selector(price_path).text
        price.append(pri)
    except:
        price.append(' ')

    print("Current at: ", item, "Percentage at: ", (item + 1) / len(elements) * 100, "%")

driver.quit()
# Transforms the data in a pandas dataframe
restaurant_data = pd.DataFrame({
    'Nome': restaurant_name,
    'Stars': stars,
    'Number of reviews': reviews,
    'Type of restaurant': restaurant_type,
    'Address': address,
    'Website': website,
    'Phone Number': phone_number,
    'Price': price
})
# Eliminates the duplicates
final_data = restaurant_data.drop_duplicates()
# Exports to csv format
final_data.to_csv('C:/Users/you/Desktop/prova.csv')
