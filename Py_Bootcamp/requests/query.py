import requests

# http://www.example.com/?key1=value1&key2=value2

# preferred pythonic method:
# response = requests.get(
# 	"http://www.example.com",
# 	params={
# 		"key1": "value1",
# 		"key2": "value2"
# 	}
# )

url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": "cat", "limit": 1}
)

# print(response.text)
data = response.json()

# print(data["joke"])
# print(f"status: {data['status']}")

print(data["results"])