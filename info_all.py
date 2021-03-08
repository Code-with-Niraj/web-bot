from selenium import webdriver

path = '/home/niraj/Downloads/chromedriver/chromedriver'
driver = webdriver.Chrome(path)

driver.get('https://www.nepalyp.com/')

category = driver.find_element_by_xpath('//*[@id="index_heading"]/div[2]/div/a[1]')
category.click()



links_of_all_companies = []
condition = True
while condition:
    each_restaurant = driver.find_elements_by_class_name('details')
    for links in each_restaurant:
        rest1 = links.find_elements_by_tag_name('a')[-1]
        links_of_all_companies.append(rest1.get_property('href'))
    try:
        driver.find_elements_by_class_name('pages_arrow')[-1].click()
    except:
        condition=False
print('Total Companies', len(links_of_all_companies))

company_name = driver.find_elements_by_xpath('/html/body/main/section/h1').text
company_address = driver.find_elements_by_xpath('//*[@id="left"]/div[2]/div/div[5]/div[2]')
company_phone = driver.find_elements_by_xpath('//*[@id="left"]/div[2]/div/div[6]/div[1]')
company_mobile = driver.find_elements_by_xpath('//*[@id="left"]/div[2]/div/div[7]/div[2]')

dict_name = {'name of company':company_name,
             'company address': company_address,
             'company_phone': company_phone,
             'company_mobile': company_mobile
            }
print(dict_name)