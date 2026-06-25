# 구현 계획

## Phase 1. 골격
- FastAPI 기반 웹 서버 생성
- CSV 업로드 API와 화면 라우팅 뼈대 생성
- 도메인 모델과 서비스 분리
- 테스트 패키지와 CI 설정 추가

## Phase 2. CSV 파서
- 업로드된 CSV를 검증하고 정규화한다.
- BOM, 인코딩, 컬럼 오류를 처리한다.
- 대용량 파일은 스트리밍 방식으로 읽는다.

## Phase 3. 통계
- 일별 통계
- 월별 통계
- 필터 조건별 집계

## Phase 4. 웹 UI
- 업로드 폼
- 일/월 통계 대시보드
- 대용량 업로드 진행 상태 표시

## Phase 5. 품질
- TDD로 테스트 보강
- 브랜치 커버리지 100% 달성
- radon, xenon, ruff/flake8, pytest-cov 적용
- GitHub Actions에서 자동 검사

