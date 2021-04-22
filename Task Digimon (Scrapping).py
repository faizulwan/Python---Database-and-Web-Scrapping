from bs4 import BeautifulSoup
import requests

### Connecting to Digimon Web
url = "http://digidb.io/digimon-list/"
web = requests.get(url)
out = BeautifulSoup(web.content, "html.parser")

# print (out)



### Collecting Digimon Name
digimon_name = []
for i in out.find_all('a'):
    digimon_name.append(i.text)
# print (digimon_name)

first = digimon_name.index("Kuramon")
# print (first)
last = digimon_name.index("Gallantmon NX")
# print (last)

digimon = digimon_name[first:last+1]
# print (digimon)                         #Digimon Name



### Collecting Digimon ID
digimon_id = []
for i in range (len(digimon)):
    digimon_id.append(i+1)

# print (digimon_id)                      #Digimon ID



### Collecting Digimon Image
digimon_image = []
for i in out.find_all("img"):
    digimon_image.append(i["src"])

# print (digimon_image)                 #Digimon image link






#Collecting Digimon Data
data_1 = []
for i in out.find_all('tbody'):
    for j in i.find_all('tr'):
        for k in j.find_all('td'):
            for l in k.find_all('center'):
                data_1.append(l.text)

data_2 = []
for i in range(len(digimon)):
    j = i*11
    k = j+10
    slices = data_1[j:k]
    data_2.append(slices)

# print (data_2)                      #Digimon Data



# Creating Digimon Data Set
Digimon_Data = []

for i in range(len(digimon)):
    store = f"({digimon_id[i]}, '{digimon_image[i]}', '{data_2[i][0]}', '{data_2[i][1]}', '{data_2[i][2]}', '{data_2[i][3]}', {data_2[i][4]}, {data_2[i][5]}, {data_2[i][6]}, {data_2[i][7]}, {data_2[i][8]}, {data_2[i][9]})"
    Digimon_Data.append(store)

print (Digimon_Data)


