from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Prajwal Kumar!"}

@app.get('/about')
def about():
    return {'message': 'Prajwal Ghotkar is a skilled Data Analyst with a Master’s degree in Data Science and a strong foundation in data visualization, SQL, and Python. He is ISO certified and known for creating impactful dashboards as a Tableau Developer. His recent work includes building a Streamlit-based LLM-powered SQL app that transforms natural language into database queries. With a passion for turning data into actionable insights.'}