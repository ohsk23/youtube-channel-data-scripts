import requests
from config import API_KEY

BASE_URL = "https://www.googleapis.com/youtube/v3"

def get_videos(channel_id, max_results=50, page_token=None):
    url = f"{BASE_URL}/search"
    print(API_KEY)
    params = {
        "key": API_KEY,
        "channelId": channel_id,
        "part": "snippet",
        "order": "date",
        "maxResults": max_results,
    }
    if page_token:
        params["pageToken"] = page_token
    response = requests.get(url, params=params)
    return response.json()

def get_comments(video_id, max_results=100, page_token=None):
    url = f"{BASE_URL}/commentThreads"
    params = {
        "key": API_KEY,
        "videoId": video_id,
        "part": "snippet,replies",
        "maxResults": max_results,
    }
    if page_token:
        params["pageToken"] = page_token
    response = requests.get(url, params=params)
    return response.json()