from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

@app.get('/info{name}')
async def get_nutritional_report(name: 
                                Annotated[str | None, 
                                Path(description='The name of the person that will be presented in the report',
                                min_length=3,
                                max_length=20)]):
    return {'Test': 'Sucess'}