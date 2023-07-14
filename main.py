import requests
import json


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79",
    "user-token": "Hf3uOkLbkBjQkOnu"
}

# 获取热榜 id
x = requests.get("https://api.shudongdehouduan.click//_api/v1/getlist?p=1&order_mode=2&room_id=", 
                 headers=headers)

response = json.loads(x.text)
data = response["data"]

# 爬取热榜第一 
# target_id = 1

for i, item in enumerate(data):
    # if i != target_id: continue

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




