import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
# import geopandas as gpd
from prettytable import PrettyTable

def get_covid_status():
    url = 'https://www.mohfw.gov.in/'
    # make a GET request to fetch the raw HTML content
    web_content = requests.get(url).content
    # parse the html content
    soup = BeautifulSoup(web_content, "html.parser")
    # remove any newlines and extra spaces from left and right
    extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
    # find all table rows and data cells within
    stats = []
    all_rows = soup.find_all('tr')
    for row in all_rows:
        stat = extract_contents(row.find_all('td'))
    # notice that the data that we require is now a list of length 5
        if len(stat) == 5:
            stats.append(stat)
    #now convert the data into a pandas dataframe for further processing
    new_cols = ["Sr.No", "States/UT","Confirmed","Recovered","Deceased"]
    state_data = pd.DataFrame(data = stats, columns = new_cols)
    state_data.head()

    state_data['Confirmed'] = state_data['Confirmed'].map(int)
    state_data['Recovered'] = state_data['Recovered'].map(int)
    state_data['Deceased'] = state_data['Deceased'].map(int)

    table = PrettyTable()
    table.field_names = (new_cols)
    for i in stats:
        table.add_row(i)
    table.add_row(['','Total',
                   sum(state_data['Confirmed']),
                   sum(state_data['Recovered']),
                   sum(state_data['Deceased'])])
    print(table)


get_covid_status()