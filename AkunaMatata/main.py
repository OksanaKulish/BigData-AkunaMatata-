import pandas as pd
import numpy as np
import time

# 1 && 2 metrics
def metrics_calculate(data):
    return data.groupby(by="origin_country", sort=True).agg({"price": np.mean}).assign(
            five_percentage=data["rating_five_count"].sum()
            / data["rating_count"].sum()
            * 100
    )

# time taken to read data
s_time = time.time()
col_list = ["price", "origin_country", "rating_count", "rating_five_count"]
data = pd.read_csv("summer_products.csv", usecols=col_list)
e_time = time.time()
print("Read without chunks: ", (e_time - s_time), "seconds")

metrics_calculate(data)
# 2
# sql = """
#     SELECT avg(price), SUM(rating_five_count)/SUM(rating_count)*100 AS five_percentage, 
#           origin_country
#     FROM `summer_products`
#     GROUP BY origin_country
#     ORDER BY origin_country
# """
# # Run a Standard SQL query using the environment's default project
# df = pd.read_gbq(sql, dialect='standard')
# print(df)
