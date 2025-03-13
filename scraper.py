from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find_all('table')[0]

world_titles = table.find_all('th')
world_table_titles = [title.text.strip().removesuffix("[note 1]") for title in world_titles][:7]

df = pd.DataFrame(columns=world_table_titles)

column_data = table.find_all('tr')[2:]

rank = 1
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data][:-2]
    individual_row_data.insert(0, rank)
    if individual_row_data[2][1].isdigit():
        individual_row_data.insert(2, iIndustry)
    else:
        iIndustry = individual_row_data[2].strip()
    try:
        iHeadquarters = individual_row_data[6].strip()
    except:
        individual_row_data.append(iHeadquarters.strip())
    rank += 1

    length = len(df)
    df.loc[length] = individual_row_data

df.drop_duplicates(inplace=True)
df.to_csv(r'data.csv', index=False)
