# Dictionary에 키가 있는지 확인하기

```python
# 문법
key not in dictionary
```

**Example**

- annotations dictionary에 img_id key가 없으면 새로운 img_id를 키로 생성하고 빈 리스트로 초기화한다.

```python
annotations = {}
for annotation in data['annotations']:
    img_id = annotation['img_id']
    if img_id not in annotations:
        annotations[img_id] = []
    
    annotations[img_id].append(annotation)
```