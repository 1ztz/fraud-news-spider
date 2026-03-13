import requests
import json
import os
from datetime import datetime

OUTPUT_FILE = "news_data.json"
SOURCE_URL = "https://oss.gjfzpt.cn/preventfraud-static/h5/list/1-1/1-1-1.json"

def fetch_news():
    try:
        print(f"[{datetime.now()}] 开始抓取...")
        resp = requests.get(SOURCE_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        items = data.get('list', [])[:20]

        news_list = []
        for item in items:
            news_list.append({
                "id": item.get('id', 0),
                "title": item.get('title', ''),
                "summary": item.get('summary', ''),
                "source": "国家反诈中心",
                "publishTime": item.get('releaseTime', ''),
                "detail": item.get('content', '详情请点击链接查看'),
                "category": "权威发布"
            })

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(news_list, f, ensure_ascii=False, indent=2)

        print(f"成功保存 {len(news_list)} 条新闻")
        return True
    except Exception as e:
        print(f"错误: {e}")
        return False

if __name__ == "__main__":
    fetch_news()
