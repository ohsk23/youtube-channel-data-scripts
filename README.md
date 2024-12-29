YouTube 데이터 분석을 위해 사용하는 스크립트

# 관련 라이브러리 설치

$ pip install -r requirements.txt

# 영상 목록 수집

$ python video_list.py

# 댓글 수집

$ python daily_comments.py

# 댓글 데이터를 CSV로 변환

$ python json_to_csv_comments.py

# 댓글 데이터 분석

$ python analyze_comments.py
