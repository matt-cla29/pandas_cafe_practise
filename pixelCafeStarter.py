import pandas as pd

df = pd.read_csv('pixel_cafe_sales.csv')
# print(df)

 # print(df.shape) # (number of rows, numbers of columns)
# print(df.columns) # (prints names of the columns)

# print(df[["Product", "Quantity"]]) # prints certain columns

# 3.filter: display food rows
# food = df[df["Category"] == "Food"]
# print(food)

# then display al rows with quantities greater than 30
# busy = df[df["Quantity"] > 30] 
# print(busy)

both = df[(df["Quantity"] > 30) & (df["Category"] == "Food")]
print(both)
