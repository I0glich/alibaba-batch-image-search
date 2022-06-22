import requests
from bs4 import BeautifulSoup
import random
import urllib.request
import os
import time
from csv import reader
parent_dir = "materials/"
with open('list2.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        # print(row[0])
        text=row[0]
        text = text.replace(" ", "-")
        # os.path.join(parent_dir, directory)
        path = "materials/new/" + text
        if not os.listdir(path):
        # while not os.path.exists(path):
            # os.mkdir(path)
            url="https://www.alibaba.com/showroom/" + text + ".html"
            A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
                   )
            rstatus = 0
            status = True
            while status:

                if (rstatus != 200):
                    # Agent = A[random.randrange(len(A))]
                    Agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                    headers = {'user-agent': Agent}
                    r = requests.get(url, headers=headers)

                    # print ("Agent: " , Agent , "| Status: " , str(r.status_code))


                    print(text, " Status code is not 200, entering sleep for 5 seconds")
                    time.sleep(5)
                    rstatus = r.status_code
                else:
                    print(text, " status code is 200, hence exiting")
                    status = False
                # with open('page.html', 'w', encoding='utf-8') as f:
                #     f.write(r.text)
                #     f.close()
    #comment
            soup = BeautifulSoup(r.text, 'html.parser')
            links = soup.find_all('div',{"id":"root"})

            for info in links:
                print(text, ": ", len(links))
                i = 1
                img = info.find_all("div", {"class":"image-switcher-content"})

                for thing in img:


                    src = thing["data-image"]

                    # print(src)

                    if src and i < 5:
                        print(text , i, " ", src)
                        urllib.request.urlretrieve(src, path + "/" + text + str(i) +".jpg")
                        i = i + 1
