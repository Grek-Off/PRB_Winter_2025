import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import matplotlib.pyplot as plt

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

books_data = []

for page in range(1, 20):
    url = BASE_URL.format(page)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Ошибка загрузки страницы {page}")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a.attrs['title']
        price = float(book.find('p', class_='price_color').text[2:])
        rating = book.p.attrs['class'][1]
        availability = 'In stock' in book.find('p', class_='instock availability').text.strip()

        books_data.append([title, price, rating, availability])

    # time.sleep(1)

df = pd.DataFrame(books_data, columns=['Title', 'Price', 'Rating', 'Availability'])

df.to_csv('competitor_price.csv', index=False)
print('Данные успешно сохранены в competitor_prices.csv')

median_price = df['Price'].median()
mean_price = df['Price'].mean()
min_price = df['Price'].min()
max_price = df['Price'].max()

print("\nАнализ цен:")
print(f"Минимальная цена: £{min_price:.2f}")
print(f"Максимальная цена: £{max_price:.2f}")
print(f"Медианная цена: £{median_price:.2f}")
print(f"Средняя цена: £{mean_price:.2f}")

df['Price Difference'] = df['Price'] - median_price
print("\nКниги с ценой ниже медианной:")
print(df[df['Price Difference'] < 0][['Title', 'Price']])

plt.figure(figsize=(10,5))
plt.hist(df['Price'], bins=15, color='skyblue', edgecolor='black')
plt.axvline(median_price, color='red', linestyle='dashed', linewidth=2, label=f"Median: £{median_price:.2f}")
plt.axvline(median_price, color='green', linestyle='dashed', linewidth=2, label=f"Average: £{mean_price:.2f}")
plt.xlabel('Price (£)')
plt.ylabel('Count')
plt.title('Distribution of Prices')
plt.legend()
plt.show()

rating_map = {'One': 1, 'Two': 2, "Three": 3, "Four": 4, "Five": 5}
df['Numeric_Rating'] = df['Rating'].map(rating_map)
rating_price_avg = df.groupby('Numeric_Rating')['Price'].mean()

plt.figure(figsize=(8,5))
plt.bar(rating_price_avg.index, rating_price_avg.values, color='orange')
plt.xlabel('Rating')
plt.ylabel('Average Price (£)')
plt.title('Average Price per Rating')
plt.xticks(ticks=[1,2,3,4,5], labels=['1★', '2★', '3★', '4★', '5★'])
plt.show()