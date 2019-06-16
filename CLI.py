import requests
from urllib.parse import quote


def dialogFlow_request(cmd):
	q= quote(cmd)
	r = requests.get('''https://console.dialogflow.com/api-client/demo/embedded/3080f317-c2bb-4b27-92d0-57f1f67b05f5/demoQuery?q='''+q+'''&sessionId=6c03f00d-e46c-0df0-39b6-998c1ea074ba''')
	print(r.get_json()['result']['fulfillment']['speech'])
	
#while True:
	#cmd = str(input())
	#dialogFlow_request(cmd)
	# return Response(
	# 	r.text,
	# 	status=r.status_code,
	# 	content_type=r.headers['content-type'],
		# )
