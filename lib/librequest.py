# 
# Copyright (c) 2024 Gabriel Freitas: gabriel.estudy.reis@gmail.com
# Wrapper for unittest: python unit testing framework
#

import requests

def request_get(url, timeout=5):
# {
	try:
		r = requests.get(url, timeout=timeout)
	except requests.Timeout:
		log_info(f"get request to {url} timeout")
		return -1
	except requests.RequestException as e:
		log_info(f"error while trying to fetch {url}: {e}")
		return -2

	return r
# }