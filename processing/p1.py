from firebase import firebase
import requests
import json
import time

firebase=firebase.FirebaseApplication('https://processing1-33307.firebaseio.com/')
while(True):
	time.sleep(5)

	
	result=firebase.put('user1','reading','111' )
	print(result)
	r=requests.get('http://10.0.0.1:8000/iotdevices/')
	data=r.json()
	sumx=0
	for i in range(len(data)):
		sumx=sumx+float(data[i]['value'])
	print(sumx/len(data))
	
	result=firebase.put('user1','reading',sumx )
	print(result)