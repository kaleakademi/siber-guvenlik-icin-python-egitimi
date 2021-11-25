# -*- coding: utf-8 -*-
import requests
accessKey="8caddd5ad72d86c509982ca2a3229f426883386b0780c114d275fdd8d5829c97"
secretKey="a53754e51fa487075a67832f885a3953cc3854620da3b8212ab3acfcf50901c5"
xapikeys="accessKey="+accessKey+"; secretKey="+secretKey+";"
header={"X-ApiKeys":xapikeys}
url="https://127.0.0.1:8834/scans"
sonuc= requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()['scans']:
	#print i
	if "Host Discovery" in str(i['name']):
		#print "Host Discovery taraması yapıldı."
		#print "id:",i['id']
		#print "uuid:",i['uuid']
		url="https://127.0.0.1:8834/scans/"+str(i['id'])
		sonuc= requests.get(url=url,headers=header,verify=False)
		for j in sonuc.json()['hosts']:
			#print j
			#print j['hostname']
			dosya_adi=str(i['name'])+"_ipler.txt"
			veri=str(j['hostname'])+"\n"
			dosya=open(dosya_adi,"a")
			dosya.write(veri)
			dosya.close()
			url="https://127.0.0.1:8834/scans/"+str(i['id'])+"/hosts/"+str(j['host_id'])
			IP_sonuc= requests.get(url=url,headers=header,verify=False)
			for k in IP_sonuc.json()['vulnerabilities']:
				plugin_id=k['plugin_id'] 
				url="https://127.0.0.1:8834/plugins/plugin/"+str(plugin_id)
				plugin_sonuc= requests.get(url=url,headers=header,verify=False)
				if str(plugin_sonuc.json()['id']) in "11936":
					for plugin in  plugin_sonuc.json()['attributes']:
						if "os_identification" in plugin['attribute_name']:
							print str(j['hostname']) 
							print IP_sonuc.json()['info']['operating-system']
