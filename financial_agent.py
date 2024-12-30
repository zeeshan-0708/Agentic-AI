from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")


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

multi_ai_agent=Agent(
    team=[web_search_agent,financial_agent],
    instructions=["Always Include Sources","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize Analyst Recommendation and share the latest news for NVDA",stream=True)