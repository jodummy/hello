import os
import re

# 처리할 폴더 경로
folder_path = "Z:/etc/Download"  # 파일이 있는 폴더 경로로 수정하세요.

# 파일명 처리 함수
def rename_file(filename):
    # 코드 번호 추출 (알파벳 + 숫자 조합 찾기)
    match = re.search(r'[A-Z]{2,}-?\d{3}', filename)
    if match:
        return match.group(0) + ".mp4"
    return None

# 폴더 내 파일명 처리
def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        
        # 파일인지 확인 (폴더 무시)
        if os.path.isfile(old_path):
            new_name = rename_file(filename)
            if new_name:
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")
            else:
                print(f"Skipped (no valid code found): {old_path}")

# 스크립트 실행
if __name__ == "__main__":
    process_folder(folder_path)
