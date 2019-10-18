from datetime import datetime
import requests


def get_latest_xlsx(number_of_months):

    today = datetime.today()

    print(today.year)
    print(today.month)

    #https://bb.org.bd/pub/monthly/econtrds/aug19/statisticaltable.xlsx


    months=['null','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

    base_url="https://bb.org.bd/pub/monthly/econtrds/"

    year=today.year
    year_string=str(today.year)


    month_iterator = today.month

    counter=0




    while(number_of_months!=-1):
        
        if months[month_iterator] == 'null':
            month_iterator=12
            year-=1
            year_string=str(year)
        
        print("beginning download: "+months[month_iterator])

        genarated_url=base_url+months[month_iterator]+year_string[2:]+'/statisticaltable.xlsx';

        #url = "https://bb.org.bd/pub/monthly/econtrds/aug19/statisticaltable.xlsx"
        response= requests.get(genarated_url)
        print('status: ',response.status_code)

        month_iterator-=1
        number_of_months-=1

     
        if response.status_code!=200:
            number_of_months+=1
        
        else:
            #latest month is saved as 1.xlsx, then 2.xlsx, 3.xlsx so on, in a descending order
            counter+=1
            with open(str(counter)+'.xlsx','wb') as f:
                print(str(counter)+'.xlsx', ' downloaded')
                f.write(response.content)
        

        

"""exmple function call for last 13 months"""
get_latest_xlsx(13)


