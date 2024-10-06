# Flask Feedback Analysis API

This project is a Flask-based API designed to analyze user feedback by determining both the **sentiment** and the **topic** of a given comment. It leverages **Large Language Models (LLMs)** for zero-shot classification of topics and sentiment analysis. The application is containerized using **Docker** for easy deployment.

## Key Features:
- **Sentiment Analysis**: Classifies feedback into sentiments such as *positive*, *negative*, or *neutral* using the [`cardiffnlp/twitter-roberta-base-sentiment-latest`](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) model.
- **Topic Classification**: Identifies key topics from user comments (e.g., *Performance*, *Quality*, *Usability*) using the [`MoritzLaurer/deberta-v3-large-zeroshot-v2.0`](https://huggingface.co/MoritzLaurer/deberta-v3-large-zeroshot-v2.0) model.
- **Dockerized**: The entire application is containerized, making it easy to run and deploy across different environments.

## How It Works:
1. The API accepts **POST** requests with user comments via the `/analyze` endpoint.
2. The comment is processed to extract both the **sentiment** and relevant **topics**.
3. A JSON response is returned with the analysis results.

## Technologies Used:
- **Flask**: A lightweight WSGI web framework for Python.
- **Docker**: Containerization for deployment consistency.
- **Hugging Face Transformers**: Pre-trained language models for natural language processing.

## Getting Started:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-feedback-analysis-api.git

2. Install dependencies: Make sure to install the required Python packages by running:

   ```bash
   pip install -r requirements.txt

3. Build and run the Docker container:
    ```bash
    docker build -t flask-app .
    docker run -p 5000:5000 flask-app

4. Send feedback comments to the /analyze endpoint via POST requests for analysis.
Example Request (via curl):

    ```bash
    curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"comment": "This is a sample comment"}'

5. Configuring Postman for POST Requests:
To send a POST request using Postman, follow these steps:
  - Open Postman and create a new POST request.
  - Set the URL to: http://127.0.0.1:5000/analyze

### Screenshot of the Request in Postman
<img width="1518" alt="image" src="https://github.com/user-attachments/assets/42b5839f-a0d6-494f-971d-62451fa2fde0">

### Screenshot of the Response in Docker
![image](https://github.com/user-attachments/assets/b28af137-2c36-4e8f-af07-c392898c4ed6)


