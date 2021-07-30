import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from requests.api import get


def data_corona():
    page = requests.get(
        'https://www.worldometers.info/coronavirus/#countries')
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup)
    get_data = soup.find(id='main_table_countries_today')
    # print(week)
    get_table_data = get_data.tbody.find_all("tr")
    # print(get_table_data)
    dic = {}
    for i in range(len(get_table_data)):
        try:
            key = get_table_data[i].find_all("a", href=True)[0].string
        except:
            key = get_table_data[i].find_all("td")[0].string
        values = [j.string for j in get_table_data[i].find_all('td')]
        dic[key] = values
    # print(dic)
    colum_name = ["Datejoined", "User name", "Gabs",
                  "Followers", "Following", "Last 50 post", "Average engagement of the post"]
    df = pd.DataFrame(dic).iloc[1:, :].T.iloc[:, :7]
    df.index_name = "country"
    df.columns = colum_name  # it provide the row and colum
    df.head()
    print(df.head)
    df.to_csv("corona_live_cases.csv")

    print("codeworked")


data_corona()
