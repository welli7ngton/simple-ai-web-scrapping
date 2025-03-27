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

urls = ['https://github.com/welli7ngton', 'https://wakatime.com/@welli7ngton']

github_webscrap = f"""
    step 1: for each url in : {urls}
    step 2: Access, explore and pick some usefull habillities and experiences to put in a Software Engineer resume.
    step 3: Explore each page interacting with the sites, looking for experiences, projects, tech and skills,
    scroll the pages and take a good look on the readmes, interact with the github.
    step 4: Organize the data that u got in a json format, do not use special characters.
    step 5: Create a tech resume with the skills that you obtained from the profiles on his github and wakatime.
    note 1: On Github, i want you to tell me about my lasts contributions and pinned repos.
    note 2: On Wakatime, i want you to get me the top five most used languages, top 3 text editors and top 3 Operating Systems.
"""

# profile = 'https://github.com/welli7ngton'
profile = 'https://github.com/LuizGup'


async def main():
    agent = Agent(
        task=f"""
            Access the following GitHub profile: {profile}.

            Read the profile README and extract relevant information related to software engineering.

            Locate and read the README files of the three pinned repositories on the profile homepage (you
            can find them by scrolling down the page).

            Gather additional insights about the person based on the information in the README files.

            Create a summary of technical skills based on the information gathered from the profile and the
            repository READMEs. Format the summary in JSON, including skills such as programming languages,
            frameworks, tools, and any other relevant technical expertise.
        """,
        llm=llm,
    )
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
