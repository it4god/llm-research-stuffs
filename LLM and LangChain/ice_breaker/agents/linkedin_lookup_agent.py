from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url

from dotenv import dotenv_values
config = dotenv_values(".env") 
api_key = config["OPENAI_API_KEY"]
def lookup(name:str, info:str) ->str:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", openai_api_key=api_key)
    template = """given the full name {name_of_person} with keyword {info} I want you to get it me a link to their Linkedin profile page.
    Your answer should contain only a URL"""
    
    tools_for_agent = [Tool(name="Crawl Google 4 linkedin profile page", func=get_profile_url, description="")]

    agent = initialize_agent(tools=tools_for_agent, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    prompt_template = PromptTemplate(template=template, input_variables=['name_of_person', 'info'])
    
    linked_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name,info=info))
    print(linked_profile_url)
    return linked_profile_url
