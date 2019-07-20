import os
import webbrowser
count=0
def check_ping(url):
    global count
    hostname = url
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    count+=1
    print("attempt: ",count)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus


while(check_ping(url)!="Network Active"):
    print("continue")

print("AACCTTIIVVEE")
    
webbrowser.open("https://www.youtube.com/watch?v=BIKarAqOB9I")
