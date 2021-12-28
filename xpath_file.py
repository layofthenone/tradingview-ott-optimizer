login_one = "/html/body/div[2]/div[4]/div/div/p[1]/a"
login_two = "/html/body/div[6]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span"
login_button = "/html/body/div[6]/div/div[2]/div/div/div/div/div/div/form/div[5]/div[2]/button/span[2]"

percent_box_xpath = "/html/body/div[2]/div[6]/div[2]/div[4]/div[3]/div/div/div[1]/div[3]/strong"
values_box_xpath = "/html/body/div[2]/div[6]/div[2]/div[4]/div[3]/div/div/div[1]/div[1]/strong"

ott_period_xpath = "/html/body/div[5]/div/div/div[1]/div/div[3]/div/div[4]/div/span/span[1]/input"
ott_percent_xpath = "/html/body/div[5]/div/div/div[1]/div/div[3]/div/div[6]/div/span/span[1]/input"

percents = [0.1, 0.2]
percentss = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]

ok_button_xpath = "/html/body/div[5]/div/div/div[1]/div/div[4]/div/span/button/span"

setting_button_xpath = "/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]"
setting_button_2_xpath = "/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[2]"


def percents_range(num):
    percent_list = [0.1]
    for i in range(num):
        my_num = 0.1
        my_num = 0.1 + my_num
        percent_list.append(my_num)
        return percent_list

