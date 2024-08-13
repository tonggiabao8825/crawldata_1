import numpy as np 
import pandas as pd 
import requests

import requests
from bs4 import BeautifulSoup
import pandas as pd 
import csv
dict_data = {
    "SBD": [],
    "Toán":[],
    "Văn":[],
    "Ngoại ngữ":[],
    "Sinh":[],
    "Lí":[],
    "Hóa":[],
    "Sử":[],
    "Địa":[],
    "GDCD":[]
}

def process_url(sbd):
    # local variable
    url = f"https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2024/{sbd}.html"
    respond = requests.get(url)
    
    if respond.status_code == 200:
        soup = BeautifulSoup(respond.content, "html.parser")
        table_content = soup.find_all("table")
        data = []
        data_csv = []
        for table in table_content:
            rows = table.find_all("tr")
            if len(rows) >= 7:
                a = rows[1].text.strip().split("\n")
                b = rows[2].text.strip().split("\n")
                c = rows[3].text.strip().split("\n")
                d = rows[4].text.strip().split("\n")
                e = rows[5].text.strip().split("\n")
                f = rows[6].text.strip().split("\n")
                # data.append([sbd, a, b, c, d, e, f])
                record_scores = [["SBD", sbd], a, b, c, d, e, f]
                
                for score in record_scores:
                    key = score[0]
                    value = score[1]
                    dict_data[key].append(value)
                    num_records = len(dict_data[key])
                
                for subject in dict_data:
                    if len(dict_data[subject]) < num_records:
                        dict_data[subject].append(None)
                        
                # print(f"SBD :{sbd} {a[0]}:{a[1]} {b[0]}:{b[1]} {c[0]}:{c[1]} {d[0]}:{d[1]} {e[0]}:{e[1]} {f[0]}:{f[1]}\n")
                # sv_w = [f"{sbd}",f'{a[0]}:{a[1]}',f"{b[0]}:{b[1]}",f'{c[0]}:{c[1]}',f'{d[0]}:{d[1]}',f'{e[0]}:{e[1]}',f'{f[0]}:{f[1]}']
                # data_csv.append(csv_w)

                
        # print(dict_data)
        return dict_data
    else:
        # print(f"No data: {sbd}")
        return dict_data

def main():
    for sbd in range(46000000, 46009900):



        
        data = process_url(sbd)   
        if sbd%100 ==0:
            print(sbd)
        
        

        
if __name__ == "__main__":
    main()
    fthanhhoa = pd.DataFrame(dict_data)
    fthanhhoa.to_csv("thanhhoa.csv")





