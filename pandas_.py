from pandas import read_csv
from func import get_response
get_response()
df_data = read_csv("product_prices.csv")
discounted_prod = (df_data[df_data.discounted == True])
