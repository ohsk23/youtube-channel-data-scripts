from .youtube_client import get_videos
from .file_in_out import save_data, load_data
from config import CHANNEL_ID

def fetch_all_videos(channel_id, page_token):
    # 기존 데이터 불러오기
    existing_videos = load_data("data/videos/videos.json") or []
    
    # 새로운 데이터 가져오기
    response = get_videos(channel_id, 3, page_token)
    new_videos = response.get("items", [])
    
    # 기존 데이터에 새로운 데이터 추가
    all_videos = existing_videos + new_videos
    
    # 모든 비디오를 합치고 publishedAt 기준으로 정렬
    all_videos = existing_videos + new_videos
    all_videos.sort(key=lambda x: x['snippet']['publishedAt'], reverse=True)  # 최신순 정렬

    # 전체 데이터 저장
    save_data(all_videos, "data/videos/videos.json")
    
    print(f"기존 비디오: {len(existing_videos)}개")
    print(f"새로 추가된 비디오: {len(new_videos)}개")
    print(f"전체 비디오: {len(all_videos)}개")
    print(f"Next Page Token: {response.get('nextPageToken')}")

if __name__ == "__main__":
    fetch_all_videos(CHANNEL_ID, "CAMQAA")