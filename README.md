# Nutri Info API

## A single endpoint that gives you a fair amount of nutritional information.

About the API:
* The endpoint provides you a basic Nutrition Report based on your weight, height and goal with information on you body mass index, water and calorie requirements.

Topics covered:
* Path and Query parameters
* Parameter validation
* Unit testing
* TDD

Stack:
* Python 3.11.2
* FastAPI
* Pytest

How to run locally on Mac:

        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        uvicorn nutri_info_api.main:app --reload

How to locally run on Windows:

        python3 -m venv venv
        source venv\Scripts\activate.bat
        pip install -r requirements.txt
        uvicorn nutri_info_api.main:app --reload

How to run Unit Tests:

        pytest
        
Currently deployed using Render at: https://nutri-info-api.onrender.com/

You can try it out at: [Swagger Documentation Link](https://nutri-info-api.onrender.com/docs)
