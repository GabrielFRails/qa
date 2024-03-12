# 
# Copyright (c) Gabriel Freitas: gabriel.estudy.reis@gmail.com
# Wrapper for unittest: python unit testing framework
#

import requests

def request_get(url, timeout=5):
# {
	try:
		r = requests.get(url, timeout=timeout)
	except requests.Timeout:
		print(f"get request to {url} timeout")
		return -1
	except requests.RequestException as e:
		print(f"error while trying to fetch {url}: {e}")
		return -2

	return r
# }