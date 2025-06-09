# Text-Summarization-Tool
1. Install dependencies:
   pip install -r requirements.txt
2. Run the app:
   streamlit run app.py
3. Build Docker image:
   docker build -t summarizer-app .
4. Run container:
   docker run -p 8501:8501 summarizer-app
5. Access the app in browser:
   http://localhost:8501
