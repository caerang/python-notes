import os

def get_current_path():
    return os.getcwd()

c_path = get_current_path()
print(f'현재 실행중인 모듈의 작업 경로는 {c_path}입니다.')