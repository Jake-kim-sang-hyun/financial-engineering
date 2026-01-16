<!-- @format -->

# Financial Engineering

파이썬 금융데이터 분석 프로젝트

## 환경 구축

### 1. 저장소 클론

```bash
git clone https://github.com/your-username/financial-engineering.git
cd financial-engineering
```

### 2. 가상환경 생성

```bash
python -m venv venv
```

### 3. 가상환경 활성화

**Windows (PowerShell)**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD)**
```cmd
.\venv\Scripts\activate.bat
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 4. 패키지 설치

```bash
pip install -r requirements.txt
```

### 5. Jupyter 실행

```bash
jupyter notebook
# 또는
jupyter lab
```

## 프로젝트 구조

```
financial-engineering/
├── data/
│   ├── raw/                       # 원본 데이터
│   └── processed/                 # 처리된 데이터
├── notebooks/                     # Jupyter 노트북
├── src/
│   ├── data/                      # 데이터 수집 모듈
│   ├── analysis/                  # 분석 모듈
│   ├── visualization/             # 시각화 모듈
│   └── utils/                     # 유틸리티
├── tests/                         # 테스트
└── requirements.txt               # 의존성 목록
```

## 주요 라이브러리

| 라이브러리 | 용도 |
|-----------|------|
| pandas, numpy | 데이터 처리 |
| yfinance | 금융 데이터 수집 |
| matplotlib, seaborn, plotly | 시각화 |
| ta, pandas-ta | 기술적 분석 |
| scipy, statsmodels | 통계 분석 |
| quantstats | 포트폴리오 분석 |
| scikit-learn | 머신러닝 |
