import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq

import os
import phi
from phi.playground import  Playground,serve_playground_app

load_dotenv()

phi.api = os.getenv("PHI_API_KEY")


## Websearch Agent
web_search_agent = Agent(
    name='Web Search Agent',
    role='Search the web for information',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always Include Sources"],
    markdown=True,


)

## Financial Agent
financial_agent = Agent(
    name='Financial Agent',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True,company_news=True)],
        instructions=["use tables to display the data"],
        show_tool_calls=True,
        markdown=True,

)


app=Playground(agents=[financial_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)







##Trying Streamlit ui but not success yet
# import openai
# from phi.agent import Agent
# import phi.api
# from phi.model.openai import OpenAIChat
# from phi.tools.yfinance import YFinanceTools
# from phi.tools.duckduckgo import DuckDuckGo
# from dotenv import load_dotenv
# from phi.model.groq import Groq
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# import os
# import phi
# from phi.playground import Playground, serve_playground_app

# load_dotenv()

# phi.api = os.getenv("PHI_API_KEY")

# # Websearch Agent
# web_search_agent = Agent(
#     name='Web Search Agent',
#     role='Search the web for information',
#     model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
#     tools=[DuckDuckGo()],
#     instructions=["Always Include Sources"],
#     markdown=True,
# )

# # Financial Agent
# financial_agent = Agent(
#     name='Financial Agent',
#     model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
#     tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
#     instructions=["use tables to display the data"],
#     show_tool_calls=True,
#     markdown=True,
# )

# # FastAPI app initialization
# app = FastAPI()

# # Add CORS middleware to allow requests from localhost:3000 (front-end app)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Initialize Playground with agents
# playground_app = Playground(agents=[financial_agent, web_search_agent]).get_app()

# # Mount Playground app as a sub-app
# app.mount("/playground", playground_app)

# if __name__ == "__main__":
#     serve_playground_app("playground:app", reload=True)

