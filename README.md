# YAPP 프로젝트 연습용 레포입니다.

## 시작하기
```
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

## 파일구조(변경여지 있음)
* User - User, Feed, QuestList
* Quest - Quest
* Planet - Planet
* Etc - Trashcan, Token

## URL
**들어갔더니 404뜬다고 당황하지마십쇼..**
기본구조 - 로컬호스트주소/앱명/모델명

* User - http://127.0.0.1:8000/User/mgmtuser
* Feed - http://127.0.0.1:8000/User/feed
* QuestList - http://127.0.0.1:8000/User/questlist
* Quest - http://127.0.0.1:8000/Quest/quest
* Planet - http://127.0.0.1:8000/Planet/planet
* Trashcan - http://127.0.0.1:8000/Ect/trashcan
* Token - http://127.0.0.1:8000/Ect/token