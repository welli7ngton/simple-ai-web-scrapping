import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.getenv('OPENAI_API_KEY'),
)

site = "https://portal.seuma.fortaleza.ce.gov.br/fortalezaonline/portal/portaltransparencia.jsf"

prompt = f"""
    step 1: Access this url: {site}
    step 2: Click on the button with the an 'a' html element with the word 'Empresa'
    step 3: Put the value '12001568000106' n the field CNPJ
    step 4: Click on the button 'Pesquisar'
    step 5: Wait until the button 'Vizualizar' appears and then click
    step 6: Wait until the processing happens and after processing, you would be able to click in
    some menus containing the files to download, all of them are 'li' HTML elements, click on them and
    download the available files.
    note 1: only click on download, do not try to vizualize any doc with the option 'Abrir'.
"""


async def main():
    agent = Agent(
        task=f"""
            step 1: Access this url: https://www.accordbi.com.br/automacao/
            step 2: Use this credentials: email = wellingtonalmeida@grupoaccord.com.br, passwd = {os.getenv('PASSWD')}
            step 3: Explore the app for 3 minutes, do not exclude or create anything, swap between menus and tabs.
            step 4: Gerenate a review of what can i do with this application.
        """,
        llm=llm,
    )
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
