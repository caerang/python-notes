# directory 다루기

## full path에서 파일 이름과 확장자만 가져오기

`'전체 경로'`에서 파일 이름과 확장자만 반환한다.

Reference: [https://docs.python.org/3/library/os.path.html#os.path.basename](https://docs.python.org/3/library/os.path.html#os.path.basename)

```python
os.path.basename('전체 경로')

>>> import os
>>> os.path.basename('D:\workspace\labelme\setup.py')
'setup.py'
>>>
```

## 확장자와 파일 이름 분리하기

확장자와 파일 이름을 분리할 때 사용한다. 파일 이름에 전체 경로가 포함되어 있으면(예, D:\test\test.txt) 확장자와 나머지 파일 이름(전체 경로 포함)으로 분리한다.

Reference: [https://docs.python.org/3/library/os.path.html#os.path.splitext](https://docs.python.org/3/library/os.path.html#os.path.splitext)

```python
os.path.splitext('파일명')

# 파일 이름만 있는 경우
>>> os.path.splitext('setup.py')
('setup', '.py')

# 파일 이름에 전체 경로가 포함된 경우
>>> os.path.splitext('d:\test\test.txt')
('d:\test\test', '.txt')
>>>
```

## 특정 위치에 파일 목록과 폴더 목록 확인하기

숨겨진 폴더, 파일 목록, 폴더 목록을 리스트 형태로 반환한다. `.` 폴더와 `..` 폴더는 포함하지 않는다.

Reference: [https://docs.python.org/3/library/os.html?highlight=listdir#os.listdir](https://docs.python.org/3/library/os.html?highlight=listdir#os.listdir)

```python
os.listdir('파일 or 폴더 위치')

>>> os.listdir('D:\workspace\labelme')
['.flake8', '.git', '.github', '.gitignore', '.gitmodules', 'docker', 'docs', 'examples', 
'github2pypi', 'labelme', 'labelme.desktop', 'labelme.egg-info', 'labelme.spec', 'LICENSE', 'MANIFEST.in', 'README.md', 'setup.py', 'tests']
>>>
```
