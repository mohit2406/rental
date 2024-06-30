import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/Users/user/Downloads/clean_data.csv') 

yearly_avg_price = data.groupby('year')['price'].mean().reset_index()
plt.plot(yearly_avg_price['year'],yearly_avg_price['price'])
plt.title('Year-wise Average Electricity Price')
plt.xlabel('Year')
plt.ylabel('Average Elecetricity Price')
plt.grid(True)
# plt.show() 
plt.savefig("../data/eda_images/yearly_electric_price.png")

plt.figure(figsize=(10,12))
monthly_avg = data.groupby(['year','month'])['price'].mean().reset_index()
for year in monthly_avg['year'].unique():
    data_by_year = monthly_avg[monthly_avg['year'] == year]
    plt.plot(data_by_year['month'], data_by_year['price'], label=year)

plt.title('Monthly Average Electricity Price for Each Year')
plt.xlabel('Month')
plt.ylabel('Average Price')
plt.legend(title='Year')
plt.grid(True)
plt.xticks(range(1, 13))
# plt.show() 
plt.savefig("../data/eda_images/month_average_price.png")


price_increse_in_6_7 = []
for year in data['year'].unique():
    data_year = data[data['year'] == year]
    monthly_avg = data_year.groupby('month')['price'].mean()
    avg_price_6_7 = data_year[data_year['month'].isin([6,7])]['price'].mean()
    avg_price_rest = data_year[~data_year['month'].isin([6,7])]['price'].mean()
    rate_of_increase = ((avg_price_6_7 - avg_price_rest) / avg_price_rest) * 100
    result = {
        'year':year,
        'rate_of_increase':rate_of_increase
    }
    price_increse_in_6_7.append(result)
price_increse_in_6_7_df = pd.DataFrame(price_increse_in_6_7)

plt.plot(price_increse_in_6_7_df['year'],price_increse_in_6_7_df['rate_of_increase'])
plt.title('increase in the average price observed during the 6th and 7th months')
plt.xlabel('Year')
plt.ylabel('rate_of_increase')
plt.grid(True) 
# plt.show() 
plt.savefig("../data/eda_images/increase_in_7_8.png")

data_state = data.groupby('stateDescription')['price'].mean().reset_index()
plt.figure(figsize=(25,6))
# plt.plot(data_state['stateDescription'],data_state['price'])  
plt.savefig("../data/eda_images/stateDescription.png")

data_sector = data.groupby('sectorName')['price'].mean().reset_index()
# plt.plot(data_sector['sectorName'],data_sector['price'])  
plt.savefig("../data/eda_images/sectorName.png")

data_sales = data[['sales','price']]
corr_matrix_sales = data_sales.corr()
sns.heatmap(corr_matrix_sales, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap Sales and Price')
# plt.show()
plt.savefig("../data/eda_images/Correlation.png")

data_revenue = data[['revenue','price']]
corr_matrix_revenue = data_revenue.corr()
sns.heatmap(corr_matrix_revenue, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap Revenue and Price')
# plt.show()
plt.savefig("../data/eda_images/Heatmap.png")