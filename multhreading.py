from concurrent.futures import ThreadPoolExecutor
import threading
import time
import datetime
import requests

panIndiaCityArr = ['mumbai','delhi','kolkata','bangalore','chennai','pune','hyderabad']  # Main Array of CIties........

ecsBounceUrl = "http://vinaydesai.mum.jdsoftware.com/csgenio_audit/cron/cron_ECSbounce.php"
# vinaydesai.mum.jdsoftware.com/csgenio_audit/cron/cron_ECSbounce.php?datacity=mumbai

def executeCityBounce(cityname):
    # print('Task Executed'+format(threading.current_thread()))
    try:
        _headers = {'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache"}
        script_response = requests.get(ecsBounceUrl +'?datacity='+str(cityname), headers= _headers)
        if(not script_response):
            print('something went wrong, url is wrong')
        else:
            fileObject = open(str(cityname)+".txt", "w")
            fileObject.write(script_response.text)
            fileObject.close()
            print(script_response.text)
            # print(str(script_response.status_code)+" "+str(script_response.text))
            # print(str(script_response.status_code))
    except Exception as err:
        print('got an err:'+str(err))
        pass




with ThreadPoolExecutor(max_workers = 15) as executor:
    clearance_upload_details = [executor.submit(executeCityBounce, cityName) for cityName in panIndiaCityArr]
print('all cities done..................')
