import numpy as np
from selenium import webdriver
import time
import xpath_file
from selenium.common.exceptions import NoSuchElementException, WebDriverException

username = "your id"
password = "your password"
chard_id = "your chart id"  # https://tr.tradingview.com/chart/xxxxxxxx/?symbol=BIST%3A"


def login_page(share, id=username, pswd=password):
    global browser
    browser = webdriver.Firefox()
    #freegustrex DiApPRJr
    browser.get("https://tr.tradingview.com/chart/"+ str(chard_id) +"/?symbol=BIST%3A" + share)
    browser.find_element_by_xpath(xpath_file.login_one).click()
    time.sleep(2)

    browser.find_element_by_xpath(xpath_file.login_two).click()
    time.sleep(2)

    browser.find_element_by_name("username").send_keys(id)
    browser.find_element_by_name("password").send_keys(pswd)

    browser.find_element_by_xpath(xpath_file.login_button).click()
    time.sleep(10)


def write_data(share, data, write_type):
    with open(share.upper() + "_data_list.txt", write_type) as text_file:
        text_file.write(data)


def percents():
    percent = browser.find_element_by_xpath(xpath_file.percent_box_xpath).text
    percent = percent[:-2]
    return percent


def values():
    value = browser.find_element_by_xpath(xpath_file.values_box_xpath).text
    value = value[:-3]
    return value


def enter_settings():
    settings_button = browser.find_element_by_xpath(xpath_file.setting_button_2_xpath)
    settings_button.click()
    settings_button.click()


def main(share, period_first, period_last, percent):
    dataList = []
    valueDataList = []
    percentsDataList = []

    login_page(share)
    percent_list = []
    for i in np.arange(0.1, percent, 0.1):
        i = "%.1f" % i
        percent_list.append(float(i))
    percent_list.append(float(percent))

    for i in range(period_first, period_last+1):
        for u in percent_list:
            short_list = []

            try:
                enter_settings()
                time.sleep(1.15)
                browser.find_element_by_xpath(xpath_file.ott_period_xpath).send_keys(str(i))
                browser.find_element_by_xpath(xpath_file.ott_percent_xpath).send_keys(str(u))
                time.sleep(0.60)
                browser.find_element_by_xpath(xpath_file.ok_button_xpath).click()
                time.sleep(3.75)

                short_list.append(i)
                short_list.append(u)
                short_list.append(float(percents()))
                short_list.append(float(values()))
                dataList.append(short_list)

                valueDataList.append(float(values()))
                percentsDataList.append(float(percents()))

            except NoSuchElementException:
                time.sleep(15)
                short_list.append(i)
                short_list.append(u)
                short_list.append("NoSuchElementException ERROR")
                print("NoSuchElementException")
                dataList.append(short_list)

            except WebDriverException:
                time.sleep(15)
                short_list.append(i)
                short_list.append(u)
                short_list.append("WebDriverException ERROR")
                print("WebDriverException")
                dataList.append(short_list)

            except ValueError:
                time.sleep(15)
                short_list.append(i)
                short_list.append(u)
                short_list.append("ValueError ERROR")
                print("ValueError")
                dataList.append(short_list)

    write_data(share, "", "w")

    for data in dataList:
        print(data)
        write_data(share, str(data) + "\n", "a+")

    write_data(share, "\nMax Percent : " +
               str(max(percentsDataList)) +
               "\n" + "Max Gain   : " +
               str(max(valueDataList)), "a+"
               )

    print("\nMax Percent : " + str(max(percentsDataList)))
    print("Max Gain   : " + str(max(valueDataList)))
    browser.close()


if __name__ == '__main__':
    main("XU100", 1, 60, 3.5)
