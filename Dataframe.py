import pandas as pd
# 1.Series controller
# data = pd.Series([20, 10, 15])
# data=data*2
# print(data)
# print("Max",data.max())
# print("Median",data.median())
# print("Mean",data.mean())
# data=data==20
# print(data)
# 2.DataFrame controller
data = pd.DataFrame({
    "name":["amy", "john", "bob"],
    "salary":[3000, 5000, 6000]
})
print(data)
