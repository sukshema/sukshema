import geocoder
import time
import serial
import re
import httplib, urllib
from twilio.rest import Client
from bs4 import BeautifulSoup
          
   #ttyS0   port='  
data = serial.Serial(
                 '/dev/ttyAMA0',
                   baudrate = 9600,
                    parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   bytesize=serial.EIGHTBITS,
 #                   )
                    timeout=1 # must use when using data.readline()
                    )
#data=serial.Serial('/dev/ttyUSB0',9600)
print " "

##########################IOT start####################

sleep = 1
key ='P1BCG39BVNAFFZCY'  # paste the key
def send_IoTDataField1(field1):
    try:
        params = urllib.urlencode({'field1': field1, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")

        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        return

def send_IoTDataField2(field2):
    try:
        params = urllib.urlencode({'field2': field2, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")

        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        return

def send_IoTDataField3(field3):
    try:
        params = urllib.urlencode({'field3': field3, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")

        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        return
#################IOT End here########################
account_sid = "AC5adf35e5e4618d6c162b20e37eae2230"
auth_token = "d96a0c4d45782079ecc424367cdc4ced"
client = Client(account_sid, auth_token)
try:
   print "Waiting for the Vehicle to Pass"
   print "                                "
   while True:
         #x=data.readline()#print the whole data at once
         #x=data.read()#print single data at once
         #data.write('1')
        
         x=data.read(8)#print upto 10 data at once and the 
                        #remaining on the second line
         g = geocoder.ip('me')
         #print(g.latlng)
         #time.sleep(2)
         if x=="22720947":
             print "Vehicle No : ",x
             print "Name :Welcome Sanjana"
             print "Lane Speed : 70 kmh "
             
             #g = geocoder.ip('me')
             
             print(g.latlng)
             time.sleep(2)
             print "       " 
             #vehcile no.
             #owner name
             #ow phone
             #location of vehicle

             #current and lane speed
             
         elif x=="22720964":
             print "Vehicle No : ",x
             print "Name : Welcome sukshema"
             
             print "Lane Speed : 70 kmh "
             print "     "
             print("your location :" + str(g.latlng))
             
             client.api.account.messages.create(
    to="+91-9632571728",
    from_="+1 210-762-4855",
    body="Lane sped : 70km/h  " + str(g.latlng))
             fed=urllib.urlopen("https://api.thingspeak.com/channels/452949/feeds.json?api_key=1RX7XP0B6P7BM2L6&results=2");
             b=repr(fed.read());
             b=b[312:]
             print(b);
             m = re.search('field1":"(.+?)"}', b)
             #print(m)
            # yy=40
            # send_IoTDataField1(yy)
            # speed = 70
            # send_IoTDataField2(speed)
             if m:
               found=m.group(1)
               print found
               y =str(found)
               yy = int(float(found))
              # print(yy)
              # yy=int('80')
              # print(yy)
               send_IoTDataField1(yy)
               speed = 70
               send_IoTDataField2(speed)
               i=0
               data.write('@')
             if yy  > 70:
                #while i < 10:
                   data.write('@')
                   data.write('@')
                   data.write('@')
                   data.write('@')
                   data.write('@')
                   data.write('@')
                   data.write('@')
                   print('exceedes the speed limit')
                   print "                 "
                   print "Waiting for the Vehicle to Pass"
                   print "                    "            
                   continue;
             #data.write('1')
             time.sleep(1)
             data.write(y)
             print "Waiting for the Vehicle to Pass"
             print "                    "  
except KeyboardInterrupt:
       data.close()
