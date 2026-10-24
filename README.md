# YouTube Sentiment Analyzer — End-to-End MLOps Pipeline

A freeCodeCamp-style end-to-end MLOps project: analyze the sentiment of YouTube comments using a trained ML model, tracked with **MLflow**, versioned with **DVC**, containerized with **Docker**, deployed on **AWS**, served through a **Flask API**, and consumed by a **Chrome extension**.

## Stack

- **ML**: scikit-learn / transformers, pandas, numpy
- **Tracking & versioning**: MLflow (experiments, model registry), DVC (data + model versioning)
- **Serving**: Flask REST API
- **Containerization**: Docker, docker-compose
- **Cloud**: AWS (EC2 / ECS / S3 / ECR)
- **Client**: Chrome extension (Manifest V3)
- **CI/CD**: GitHub Actions

## Project layout

```
youtube-sentiment-analyzer/
├── src/
│   ├── data/          # data ingestion & preprocessing
│   ├── features/      # feature engineering
│   ├── models/        # training, evaluation, prediction
│   ├── api/           # Flask serving app
│   └── utils/         # shared helpers
├── extension/         # Chrome extension (Manifest V3)
├── docker/            # Dockerfile + compose
├── tests/             # unit & integration tests
├── notebooks/         # exploration notebooks
├── scripts/           # one-off scripts (download data, etc.)
├── params.yaml        # DVC params
├── dvc.yaml           # DVC pipeline
├── requirements.txt
└── README.md
```

## Getting started

```bash
# 1. Clone
git clone https://github.com/Elouahabi-Naoufal/youtube-sentiment-analyzer.git
cd youtube-sentiment-analyzer

# 2. Python env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3. DVC
dvc init
dvc pull          # pulls data + model (configure remote first)

# 4. Train
python src/models/train.py

# 5. Track with MLflow
mlflow ui         # http://localhost:5000

# 6. Serve
python src/api/app.py   # http://localhost:8000

# 7. Docker
docker build -t yt-sentiment -f docker/Dockerfile .
docker run -p 8000:8000 yt-sentiment

# 8. Chrome extension
# chrome://extensions → Load unpacked → extension/
```

## Milestones

- [ ] Data collection (YouTube comments via API)
- [ ] Preprocessing & labeling
- [ ] Baseline model + MLflow tracking
- [ ] DVC pipeline (data → features → model)
- [ ] Flask API + Docker image
- [ ] AWS deployment
- [ ] Chrome extension
- [ ] CI/CD + monitoring (drift)

## License

MIT
