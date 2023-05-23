from seleniumwire import webdriver
import time
from seleniumwire.utils import decode
import json
from ast import literal_eval

l = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

driver = webdriver.Firefox()
url = "https://adstransparency.google.com/?region=anywhere"
driver.get(url)
time.sleep(0.5)
search = driver.find_element(
    "css selector", "label.input-container:nth-child(1) > input:nth-child(2)"
)

count = 0
for char in l:
    time.sleep(1)
    search.click()
    time.sleep(0.3)
    search.send_keys(char)
    time.sleep(0.5)
    search.click()
    time.sleep(1.5)
    time.sleep(0.3)
    search.clear()
    count = count + 1
listData = []
for request in driver.requests:
    if (
        request.response
        and request.url
        == "https://adstransparency.google.com/anji/_/rpc/SearchService/SearchSuggestions?authuser="
    ):
        body = decode(
            request.response.body,
            request.response.headers.get("Content-Encoding", "identity"),
        )
        body = literal_eval(body.decode("utf-8"))
        listData.append(body)

with open("data.json", "w") as fout:
    json.dump(listData, fout)
