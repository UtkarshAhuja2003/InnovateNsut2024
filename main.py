
from fastapi import FastAPI
import os
from pydantic import BaseModel
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

app = FastAPI()

API_KEY= "AIzaSyA6fYVkYWamANNjKIMwrdEJ9w0fqsmGU98"
os.environ['GOOGLE_API_KEY'] = API_KEY

llm = GooglePalm(temperature = 0.3)


class InputData(BaseModel):
    question: str

@app.post("/legalaid")
async def assistive_legalaid(data: InputData):

    title_template = PromptTemplate(
        input_variables = ['question'],
        template = "Act as an assistive legal advisor about Indian law . Here is the Question : {question} "
    )

    title_chain = LLMChain(llm = llm, prompt = title_template, verbose = True, output_key = 'output')

    response = title_chain({'question' : data.question})

    return response["output"]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
