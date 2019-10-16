from datetime import datetime
import requests

today = datetime.today()

print(today.year)
print(today.month)

#https://bb.org.bd/pub/monthly/econtrds/aug19/statisticaltable.xlsx


months=['null','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

base_url="https://bb.org.bd/pub/monthly/econtrds/"
year_string=str(today.year)
genarated_url=base_url+months[today.month]+year_string[:2]+'/statisticaltable.xlsx';
print(genarated_url)

print("beginning download")

#url = "https://bb.org.bd/pub/monthly/econtrds/aug19/statisticaltable.xlsx"
response= requests.get(genarated_url)
print(response.status_code)

if response.status_code!=200:
    if today.month!=1:
        genarated_url=base_url+months[today.month-1]+year_string[2:]+'/statisticaltable.xlsx';
        print(genarated_url)
    else:
        prev_year_int=today.year-1
        prev_year=str(prev_year_int)

        genarated_url=base_url+months[12]+prev_year[2:]+'/statisticaltable.xlsx';
        print(genarated_url)
    
    response=requests.get(genarated_url)

    if response.status_code!=200:
        print("downloading failed")
        exit()
    


#the below line saves the binary data, it be returned as well
with open('latest.xlsx','wb') as f:
    f.write(response.content)

print("success")
