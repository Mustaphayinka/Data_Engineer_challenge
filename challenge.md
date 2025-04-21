# Data_Engineer_challenge
This is a job application test challenge

**World Bank Country Metadata API - Powered by FASTAPI**

This is a simple RESTful API made with FastAPI, meant for fetching socioeconomic data about nations using information from world bank API. This ch,hallenge.md will guide you through the purpose of the project , how to set it up, use it and its documentation interface. 

Project Objective
The primary objective of this API is to enable users to fetch structured metadata for any country that is supported by World Bank. This includes Country Name and ISO codes,
Regional and Income classification, Capital city, Longitude and Latitude, Lending Type and Administrative grouping.

This project shows the strength of Python APIs while making structure of the web page of the fast API while making it easy , clear, and completely interactive.

Features

FastAPI backend
Gets up-to-date info from World Bank API
Gives clean JSON output for any country by name
Has Auto made swagger docs interface
Fully beginner friendly and able to understand


How to Run

1. Clone the repo:
```bash
git clone https://github.com/Mustaphayinka/Data_Engineer_challenge.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the FastAPI application
```bash
fastapi run main.py
```
4. Open file in browser
```
http://0.0.0.0:8000/docs
```

**Example API Usage**

1. Fetch Country Metadata
```GET /meta/NGA```

Response:
```{
"Country": "Nigeria"
"Capital": "Abuja"
"Region": "Sub-Saharan Africa"
"Income level": "Lower middle income"
"Lending Type": "Blend"
}
```

2. Get Country URL from CSV

```
GET /country/Nigeria
```

Response:
```json
"Country": "Nigeria"
"URL": "https://data.worldbank.org//country/nigeria?view=chart"

```




