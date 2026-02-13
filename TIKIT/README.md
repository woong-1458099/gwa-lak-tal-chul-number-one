## TIKIT (E103) - 스마트 명함 교환 및 출입 권한 플랫폼
TIKIT은 디지털 명함 교환을 중심으로, 명함 최신화 동기화, AI 검색, NFC 출입 권한까지 확장한 풀스택 프로젝트입니다.
핵심 컨셉은 유저당 여러 개의 명함 = 여러 개의 페르소나입니다. 사용자는 상황에 맞는 명함을 골라 교환하고, 교환된 명함은 상대의 명함첩에서도 자동 최신화됩니다.

핵심 가치


명함 교환 후 최신화 동기화: 내 명함 정보가 바뀌면 교환된 상대의 명함첩에도 최신 정보가 반영됩니다.

1:N 명함 교환: 강의/행사/소개 자리에서 다수에게 한 번에 명함을 공유할 수 있습니다.

NFC 출입 권한(MVP): 사용자가 소유한 NFC 기기에 출입 권한을 부여하고, 임시 출입증으로 손쉽게 출입할 수 있습니다.

보안 강화: 허가되지 않은 기기 태깅 시 권한 박탈 + 보안팀 알림이 즉시 발생합니다.

교환 위치 기반 검색: 명함 교환 위치를 저장하고, AI 검색으로 쉽게 찾을 수 있습니다.

OCR 도입: 종이 명함을 촬영하면 자동 인식/분류됩니다.

AI 검색: 명함 정보 + 교환 상황(장소/메모/태그/날씨)을 함께 검색할 수 있습니다.



저장소 구조


tikit-frontend/: 모바일 앱 (React Native + Expo)

tikit-backend/: Spring Boot API 서버

tikit-search_AI/: OCR + 의미 검색 FastAPI 서비스

nginx/: Nginx 설정

jenkins-docker/: Jenkins CI/CD 컨테이너 구성

docker-compose.yml: 운영 스택 (블루/그린)

docker-compose.dev.yml: 개발 스택

deploy.sh, deploy-prod.sh: 배포 스크립트



아키텍처 요약

모바일 앱은 NFC/QR로 명함을 교환하고, OCR로 명함 정보를 디지털화합니다.
백엔드는 인증/명함/교환/출입 검증을 담당하고, Redis, S3, AI 서비스와 연동됩니다.
AI 서비스는 Clova OCR + PyTorch 분류로 텍스트를 정제하고, OpenAI 임베딩 + Redis Vector Search로 검색을 제공합니다.
인프라는 Docker Compose, Nginx 리버스 프록시, Jenkins CI/CD, 백엔드 블루/그린 배포로 구성됩니다.



주요 기능


명함 교환

NFC/QR 교환
1:1, 1:N 교환 지원
명함 최신화 동기화



위치/검색

교환 위치 저장
교환 히스토리 기반 검색
AI 기반 자연어 검색



OCR & AI

종이 명함 OCR 인식
AI 분류 + 벡터 검색



출입 권한 (MVP)

NFC 기기 등록 및 권한 부여
임시 출입증 발급
허가되지 않은 태깅 시 보안 경보





기술 스택


Frontend: React Native, Expo, TypeScript

Backend: Spring Boot 3.5, Java 21, JPA, Redis, OAuth2/JWT, WebSocket, AWS S3, Firebase Admin

AI Service: FastAPI, OpenAI 임베딩, Clova OCR, PyTorch, Redis Stack

Infra: Docker Compose, Nginx, Jenkins

Data: MySQL 8.0, Redis Stack



로컬 개발

1) 개발 스택 실행

# repo root에서 실행

docker compose -p dev -f docker-compose.dev.yml up -d --build


개발 서비스/포트 (docker-compose.dev.yml 기준):

MySQL: 127.0.0.1:3307

Redis: 127.0.0.1:6379

RedisInsight: 127.0.0.1:8001

AI 서비스: 8002 (컨테이너 8000 매핑)
Backend Blue: 127.0.0.1:8081

Backend Green: 127.0.0.1:8082

Nginx Dev: 8000, 8443



2) 프론트엔드 (Expo)

cd tikit-frontend
npm install
npm run start


에뮬레이터 포트 포워딩 예시:

adb reverse tcp:8081 tcp:8081
adb reverse tcp:8082 tcp:8082



3) 백엔드 단독 실행

cd tikit-backend
./gradlew bootRun



4) AI 서비스 단독 실행

cd tikit-search_AI
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000




환경 설정
루트에 .env 파일 생성 (docker-compose에서 참조):

DB_NAME=...
DB_ROOT_PASSWORD=...
DB_USERNAME=...
DB_PASSWORD=...

AWS_ACCESS_KEY=...
AWS_SECRET_KEY=...
S3_BUCKET_NAME=...
CDN_URL=...

OPENAI_API_KEY=...
CLOVA_OCR_URL=...
CLOVA_OCR_KEY=...

JWT_SECRET=...




AI 서비스 엔드포인트


POST /v1/cards/index: 명함 인덱싱 (Redis 벡터 저장)

POST /v1/cards/search: 하이브리드 검색

POST /v1/ocr/analyze: OCR + 필드 분류



백엔드 참고
백엔드는 기기 프로비저닝, NFC 패스 검증, 명함 교환, 알림 전송 등의 도메인 모듈로 구성됩니다. 자세한 구조는 tikit-backend/src 참고.


문서


tikit-frontend/README.md: 프론트 구조/개발 가이드

Porting_Manual.md: 배포/이관 가이드 (문자 깨질 경우 인코딩 확인 필요)

emulatorTest.md: 에뮬레이터 관련 참고

