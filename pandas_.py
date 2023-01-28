from pandas import read_csv
from func import get_response
# replace link in get_response function to get a different result
get_response("https://alta.ge/headphone.html")
df_data = read_csv("product_prices.csv")
discounted_prod = (df_data[df_data.discounted == True])
