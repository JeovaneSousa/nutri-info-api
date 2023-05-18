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

How to run on Mac:

        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        uvicorn nutri_info_api.main:app --reload

How to run on Windows:

        python3 -m venv venv
        source venv\Scripts\activate.bat
        pip install -r requirements.txt
        uvicorn nutri_info_api.main:app --reload


You can try it out at: [Swagger Documentation Link](http://127.0.0.1:8000/docs)

(http://127.0.0.1:8000/)