import urllib.request as request
import json

src="http://125.227.65.79:8080/EIP/service/ITRI/AIR012Service.php"
with request.urlopen(src) as response:
    # data = json.load(response)
    # data = response.read().decode("utf-8")
    print(data)

# src="https://data.taipei/opendata/datalist/apiAccess?scope=datasetMetadataSearch"
# with request.urlopen(src) as response:
#     data2 = json.load(response)
#     clist = data2["result"]["results"]
# with open("data.txt","w",encoding="utf-8") as file:
#     for description in clist:
#         file.write(description["description"]+"\n")





