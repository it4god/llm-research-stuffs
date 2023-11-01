from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import get_data, scrape_linkendin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from dotenv import dotenv_values
config = dotenv_values(".env") 

information = """
Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business magnate and investor. Musk is the founder, chairman, CEO and chief technology officer of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$207 billion as of October 2023, according to the Bloomberg Billionaires Index, and $231 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.[5][6]

Musk was born in Pretoria, South Africa, and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University in Kingston, Ontario. Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics there. He moved to California in 1995 to attend Stanford University. However, Musk dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and with $12 million of the money he made, that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal. 
"""

if __name__ == "__main__":
    api_key = config["OPENAI_API_KEY"]

    linkedin_profile_url = linkedin_lookup_agent(name="Jeffrey Lim", info="MYSABDA")
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name= "gpt-3.5-turbo",openai_api_key=api_key)
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    #profile_url = "https://www.linkedin.com/in/hadipramono/"
    print(linkedin_profile_url)
    linkenin_data = scrape_linkendin_profile(linkedin_profile_url=linkedin_profile_url)
    print(chain.run(information=linkenin_data))