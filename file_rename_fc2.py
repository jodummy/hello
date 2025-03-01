import os
import re

# 파일명에서 7자리 숫자 추출 및 변경
def rename_files_in_folder(folder_path):
    # 폴더 내 모든 파일을 가져오기
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    for file_path in files:
        # 파일명만 추출
        file_name = os.path.basename(file_path)
        
        # 7자리 숫자를 찾기 위한 정규식 (숫자만 7자리)
        match = re.search(r'\d{7}', file_name)
        
        if match:
            # 7자리 숫자를 추출
            new_name = match.group(0) + os.path.splitext(file_name)[1]  # 확장자 추가
            new_file_path = os.path.join(folder_path, new_name)
            
            # 파일명 변경
            os.rename(file_path, new_file_path)
            print(f"파일명을 '{file_name}'에서 '{new_name}'로 변경했습니다.")
        else:
            print(f"파일 '{file_name}'에서 7자리 숫자를 찾을 수 없습니다.")

# 폴더 경로를 지정하고 파일명 변경
folder_path = "Z:/etc/새 폴더"  # 폴더 경로를 입력하세요.
rename_files_in_folder(folder_path)
