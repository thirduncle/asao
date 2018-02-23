import urllib, requests, json, time
from urlparse import urlparse

'''
response1 = requests.post('http://telematics.oasa.gr/api/?act=getBusLocation&p1=1771')
json_response1 = response1.json()
for route in json_response1:
	if json_response1[route]["ROUTE_CODE"] = "1771":
		bus_id = json_response1[route]["VEH_NO"]
		bus_long = json_response1[route]["CS_LNG"]
		print bus_id, bus_long
'''		
# 2085 - route code Stournari - Kifisia
# 1771 - Averof prousis

#sample output
#[{"route_code":"1771","veh_code":"10740","btime2":"6"},
# {"route_code":"2484","veh_code":"10182","btime2":"7"},
# {"route_code":"1974","veh_code":"10162","btime2":"11"},
# {"route_code":"2484","veh_code":"10104","btime2":"15"}]


#ta values epistrefontai etsi:
'''
btime2 4
route_code 1771
veh_code 10749

btime2 5
route_code 2484
veh_code 10104
btime2 15
route_code 2484
veh_code 10168
btime2 20
route_code 1974
veh_code 10203
'''		

monitor = 0

'''
		
def monitor_stop():
	response2 = requests.post('http://telematics.oasa.gr/api/?act=getStopArrivals&p1=60012')
	json_response2 = response2.json()
	global monitor
	monitor = 0
	i = 0
	j = 0	

	for i in json_response2:
		for k,v in sorted(i.items()):
			if v == "2085":
				print i.values()[0]
				monitor = 1
			else:
				continue
'''

		
def monitor_stop_test():
	response2 = requests.post('http://telematics.oasa.gr/api/?act=getStopArrivals&p1=60012')
	json_response2 = response2.json()
	global monitor
	monitor = 0
	i = 0
	j = 0	

	for i in json_response2:
		for k,v in sorted(i.items()):
			print k,v
			#if v == "2085":
			#	print i.values()[0]
			#	monitor = 1
			#else:
			#	continue
	
		

while True:
	if monitor == 0:
		print "Bus nowhere in site!"
	#monitor_stop_test()
	print 20*('*') 
	time.sleep(15)


	
#for d in my_list:
 #   for k, v in d.items(): 
        # do something with the key, value pair
		
	

