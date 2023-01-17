import requests
import json


headers = {
    "user-agent": "",
    "user-token": ""
}

x = requests.get("https://api.shudongdehouduan.click//_api/v1/getlist?p=1&order_mode=2&room_id=", headers=headers)

response = json.loads(x.text)
data = response["data"]

target_id = 1

for i, item in enumerate(data):
    if i != target_id: continue

    pid = item["pid"]
    head = item["text"]

    y = requests.get(f"https://api.shudongdehouduan.click//_api/v1/getcomment?pid={pid}", headers=headers)
    response = json.loads(y.text)

    comment = response["data"]

    with open(f"record{i}_pid{pid}.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(comment, indent=4, ensure_ascii=False))

    with open(f"record{i}_pid{pid}.txt", "w", encoding="utf-8") as f:
        f.write(head + "\n\n")
        for sentence in comment:
            f.write(sentence["text"] + "\n\n")
    
    break




