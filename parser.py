from extractor import CrawlBrowser
import json
import csv
import pdb

if __name__ == "__main__":
    try:
        print("init")
        driver = CrawlBrowser()
    except:
        print("init error")

    try:
        driver = CrawlBrowser()
        
        driver.login()

        driver.get_list()

        for i in driver.data:
            driver.get_detail(i)

        my_dict = driver.data

        with open('total.csv', 'w', encoding='utf-8') as f:  # Just use 'w' mode in 3.x  # encoding='cp949'
            w = csv.DictWriter(f, my_dict[0].keys())
            w.writeheader()

            for key, value in my_dict.items():
                print(value)              
                w.writerow(value)
            # w.writerows(my_dict.values())  # 이런 식으로 하면 여러 행들의 값들을 엑셀의 여러 행에 걸쳐서 자동으로 입력함.
            
            # print(my_dict.keys())

            # my_dict[0].keys
            
            # for i in my_dict.keys():
            #     # print(i)
            #     i = int(i)
            #     print(my_dict[i])
            #     w.writerow(my_dict[i])

            # for key in my_dict.keys():
            #     print(my_dict[key])
            #     w.writerow(my_dict[key])

            # print(my_dict.items())
            # print(my_dict.values())
            # for my_dic in my_dict:
            #     print(my_dic.value)          
            #     w.writerow(my_dic.value)
                

    except:
        driver.browser.close()
        print("error")
    finally:

        print("end")
