from utils import get_comments
from utils import load_data, save_data
def get_video_comments(video_id):
    print('video_id: ', video_id)
    # 기존 데이터 불러오기
    existing_comments = load_data(f"data/comments/{video_id}.json") or []
    # 새로운 데이터 가져오기
    all_new_comments = []
    next_page_token = None
    
    while True:  # while True로 변경
        try:    
            response = get_comments(video_id, 100, next_page_token)
            new_comments = response.get("items", [])
            all_new_comments.extend(new_comments)
        except Exception as e:
            print(f"Error: {e}")
            break
            
        next_page_token = response.get('nextPageToken')
        print(f"댓글 {len(new_comments)}개 수집 완료, 다음 토큰: {next_page_token}")
        if not next_page_token:  # 다음 페이지가 없으면 종료
            break
    
    # 기존 데이터에 새로운 데이터 추가
    all_comments = existing_comments + all_new_comments
    
    # 모든 댓글을 합치고 publishedAt 기준으로 정렬
    # all_comments.sort(key=lambda x: x['snippet']['topLevelComment']['snippet']['publishedAt'], reverse=True)

    # 전체 데이터 저장
    save_data(all_comments, f"data/comments/{video_id}.json")
    
    print(f"\n=== 최종 결과 ===")
    print(f"기존 댓글: {len(existing_comments)}개")
    print(f"새로 추가된 댓글: {len(all_new_comments)}개")
    print(f"전체 댓글: {len(all_comments)}개")

if __name__ == "__main__":
    get_video_comments("neHd1yuxdro")