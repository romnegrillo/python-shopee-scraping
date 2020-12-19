#!/usr/bin/python3
import bs4
import re
import generate_report
import datetime

def read_webpage_contents(file_path):
    with open(file_path, "r") as f:
        contents = f.read()
        return contents

def get_dict_items(file_path, account_name):
    
    page_contents = read_webpage_contents(file_path)

    item_dict = {}

    bs_item_info = bs4.BeautifulSoup(page_contents, "html.parser")

    # This method is not ordered.
    # item_name_tag = {"class": "order-content__item__detail-content"}
    # item_price_tag = {"class": "purchase-card-buttons__total-price"}

    # item_name_list = [i.getText() for i in bs.find_all(attrs = item_name_tag)]
    # item_price_list = [i.getText() for i in bs.find_all(attrs = item_price_tag)]

    # for item_num, (item_name, item_price) in enumerate(zip(item_name_list, item_price_list)):
    #     print("{:<3} {:<175} {:<20}".format(item_num, item_name, item_price))


    item_info_tag = {"class": "purchase-list-page__checkout-card-wrapper"}
    item_info_list = bs_item_info.find_all(attrs = item_info_tag)

    for item_num, item_info in enumerate(item_info_list,1):
        # Each item_info is a html_element blocks about the item purchased
        # like name and its price. We extract it again so it is ordered.
        # The first methos above is not ordered.
        
        #print(item_info)
        #print()

        item_name_regex_pattern = r'<div class="order-content__item__name">(.+?)<\/div>?'
        item_name = re.findall(item_name_regex_pattern, item_info.decode())

        item_price_regex_pattern = r'<span class="purchase-card-buttons__total-price">(.+?)<\/span>?'
        item_price = re.findall(item_price_regex_pattern, item_info.decode())

        #print(item_name[0], item_price[0].replace("₱","").replace(",",""))
        
        item_dict[item_num] = {"name": item_name[0], "price": item_price[0].replace("₱","").replace(",","")}

    # for item in item_dict:
    #     print(item_dict[item])

    return item_dict

if __name__ == "__main__":

    # Sample test only.

    sample_username = "romnegrillo"
    file_title = "Summary of your Shopee Orders"
    date_generated = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    file_name = "shopee-summary-" + date_generated.replace(" ", "-").replace("/","-").replace(":","-").replace(",","-") + ".pdf"
    
    item_info = get_dict_items("webpage_contents.html", sample_username)
    total_money_spent = sum([float(val["price"]) for key, val in item_info.items()])

    file_description = "Account of: {}\nGenerated on: {}\n Total Money Spent on Shopee: {:,.2f}".format(sample_username, date_generated, total_money_spent)
   
    generate_report.generate_report_from_dict(file_name, file_title, file_description, item_info)