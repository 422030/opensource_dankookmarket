# opensource_dankookmarket

# 단근마켓 사용자 가이드
**소개**  
: 단근마켓은 단국대학교 학생들을 위한 중고 교재 거래 및 공동구매 플랫폼입니다. 누구나 쉽게 교재를 등록하고, 검색하고, 구매할 수 있습니다.  
학생 간 직접적인 거래를 돕고, 학기마다 반복되는 교재 비용 부담을 줄이기 위해 개발되었습니다.  

**주요 기능**  
①     로그인/회원가입  
      : 간단한 이름과 비밀번호만으로 빠른 가입 및 로그인
      
②     교재 등록  
      : 내가 갖고 있는 중고 교재를 직접 등록 가능
      
③     교재 검색  
      : 원하는 책을 제목 및 전공/교양 카테고리로 쉽게 검색
      
④     공동구매 요청  
      : 여러 학생이 함께 구입하고 싶은 품목을 등록하여 모집 가능

⑤     채팅함  
      : 다른 사용자와 실시간으로 교재 거래 및 공동구매 관련 대화를 나눌 수 있는 채팅 기능 제공  
      
**사용 방법**  
①     로그인 / 회원가입  
      처음 사용자라면 회원가입 버튼을 통해 이름과 비밀번호 입력 후 가입하세요.  
      로그인 후에만 교재 등록, 검색, 공동구매 등의 기능을 사용할 수 있습니다

②     교재 등록  
      I.      상단 메뉴 또는 메인 화면의 교재 등록 버튼 클릭  
      II.     교재 제목, 가격, 카테고리(전공/교양), 코멘트 입력 후 등록 버튼 클릭  
      III.    등록된 교재는 메인 화면에서 확인할 수 있습니다.
      
③     교재 검색  
      I.      상단 메뉴에서 교재 검색 페이지로 이동  
      II.     원하는 제목 또는 키워드 입력 + 카테고리 선택 후 검색 버튼 클릭  
      III.    검색 결과에서 원하는 교재를 클릭해 자세한 정보를 확인할 수 있습니다.
      
④     공동구매 요청  
      I.      상단 메뉴에서 공동구매 페이지로 이동  
      II.     구매하고 싶은 품목명과 예상 가격 입력 후 등록  
      III.    등록된 목록은 같은 페이지 하단에 자동으로 보여집니다.


⑤     채팅함 사용  
      I.      상단 메뉴에서 ‘채팅창’ 버튼 클릭  
      II.     내가 등록한 교재와 채팅한 사용자 목록을 확인  
      III.    사용자를 클릭하여 채팅방으로 이동해 실시간 대화 가능

# 단근마켓 개발자 가이드
1. 프로젝트 구조 
 
opensource_dankookmarket/
├── backend/                # Django 백엔드
│   ├── apps/               # 사용자 정의 앱들 (books, users 등)
│   ├── market_project/     # 프로젝트 설정
│   ├── db.sqlite3          # SQLite 데이터베이스
│   └── manage.py
├── frontend/
│   ├── public/             # HTML, CSS, JS 파일들
│   └── src/                # 정적 파일들


 
2. 개발 환경 설정 

① 가상환경 만들기 및 실행 
 
루트 디렉토리에서
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # macOS/Linux
 
② 패키지 설치
pip install -r requirements.txt


3. 서버실행

백엔드 (Django)

cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


> 기본 주소: [http://127.0.0.1:8000](http://127.0.0.1:8000)

프론트엔드
cd frontend/public
python -m http.server 8001

> 프론트 주소: [http://127.0.0.1:8001](http://127.0.0.1:8001)

4. API 정보
① 로그인 
 - URL: /users/login_api/
 - Method: POST
 - 요청 데이터: { "username": "이름", "password": "비밀번호" }
 설명: 사용자 로그인 처리, 성공 시 is_admin 정보 포함 응답

② 등록된 책 조회
 - URL: /api/books/
 - Method: GET
 설명: 등록된 모든 교재 목록 반환

③ 책 등록
  - URL: /api/books/
  - Method: POST
  ex) 요청 데이터

    {
      "title": "오픈소스",
      "author": "송인식",
      "price": 12000,
      "condition": "good",
      "description": "사용감 있음",
      "category": "전공"
    }
    
  설명: 로그인된 사용자만 등록 가능. seller는 자동으로 서버에서 설정됨.

 ④ 책 검색
  - URL: /api/books/?search=자료
  - Method: GET
  설명: 교재 제목, 카테고리, 설명(comment)에서 키워드 포함 항목 검색

 ⑤ 찜 확인
   - URL: /api/interests/check/?book_id=1
   - Method: GET
  설명: 해당 책(book\_id)을 내가 찜했는지 확인 (로그인 필요)

5. 개발 시 체크리스트
① 책 등록/검색 API는 인증 토큰 없이도 접근 가능 (IsAuthenticatedOrReadOnly)
② 책 등록 시 seller는 서버에서 자동 등록됨
③ 프론트에서 교재 등록 시 로컬스토리지 아닌 서버 DB로 연동되도록 수정 필요
④ image 필드 등 일부 항목은 현재 사용 안 함 (필요 시 multer/s3 등 연결 고려)

6. 로컬 테스트 팁
- API 호출 테스트: Postman 또는 fetch()로 직접 확인
- Django Admin: /admin/ (superuser 만들어서 테스트 가능)

  python manage.py createsuperuser
  
7. 협업 & 유지보수

* PR 시 변경사항은 명확히 작성
* 파일 위치 통일 (e.g., js는 frontend/src/js/)
* 커밋 메시지 스타일:
'''
  feat: 교재 검색 API 연결
  fix: 로그인 오류 해결
  docs: 사용자 가이드 작성
'''


 
**프로젝트 참여자**  
: 강유진, 권도윤, 신정민, 한은초


