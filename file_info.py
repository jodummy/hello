import os
from datetime import datetime

# 파일 정보 가져오기
def get_file_info(file_path):
    if not os.path.isfile(file_path):  # 파일인지 확인
        return None  # 파일이 아니면 None 반환
    
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    
    try:
        file_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(f"Error getting file modification time for {file_path}: {e}")
        file_date = "Unknown"
    
    return file_name, file_size, file_date

# 폴더 내 모든 비디오 파일을 읽고 정보를 작성 후 로그로 출력
def find_video_files_in_folder(folder_path):
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    for file in files:
        file_info = get_file_info(file)
        if file_info is not None:  # 파일 정보가 있을 경우
            file_name, file_size, file_date = file_info
            
            # file:///로 시작하고 Windows 경로 구분자 사용
            file_uri = f"file:///{file.replace('/', '\\')}"
            
            # 로그 형식에 맞게 출력
            print(f"{file_name}, {file_uri}, {file_size}, {file_date}")

# 폴더 경로를 지정하고 비디오 파일 정보 출력
## folder_path = "Z:/etc/새 폴더"  # 폴더 경로를 입력하세요.
folder_path = "Z:/etc/fc2"  # 폴더 경로를 입력하세요.

find_video_files_in_folder(folder_path)