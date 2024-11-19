import os
from textwrap import dedent
from crewai import Agent
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from langchain.llms import Ollama

class MarketingAnalysisAgents:
    def __init__(self):
        self.llm = Ollama(model=os.environ['MODEL'])

    def product_competitor_agent(self):
        return Agent(
            role="Market Research Specialist",
            goal=dedent("""\
                Perform thorough analysis of products and competitors,
                delivering valuable insights for marketing strategies."""),
            backstory=dedent("""\
                As a Market Research Specialist at a top digital marketing firm,
                you excel in analyzing online business environments."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet
            ],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

    def strategy_planner_agent(self):
        return Agent(
            role="Marketing Strategy Expert",
            goal=dedent("""\
                Extract insights from product analysis to craft effective
                marketing strategies."""),
            backstory=dedent("""\
                You are a Marketing Strategy Expert at a renowned agency,
                known for creating tailored strategies that achieve results."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True
        )

    def creative_content_creator_agent(self):
        return Agent(
            role="Social Media Content Innovator",
            goal=dedent("""\
                Create engaging and original content for social media campaigns,
                focusing on impactful Instagram ad copies."""),
            backstory=dedent("""\
                As a Social Media Content Innovator at a leading agency,
                you specialize in crafting stories that connect with audiences.
                Your strength is transforming strategies into captivating content."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True
        )

    def senior_photographer_agent(self):
        return Agent(
            role="Lead Photographer",
            goal=dedent("""\
                Capture stunning photographs for Instagram ads that evoke emotions
                and convey powerful messages."""),
            backstory=dedent("""\
                As a Lead Photographer at a premier marketing agency,
                you are skilled in taking photos that inspire and engage.
                You're tasked with creating exceptional images for a key client."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

    def chief_creative_director_agent(self):
        return Agent(
            role="Creative Director",
            goal=dedent("""\
                Ensure team output is top-notch and aligns with product goals,
                providing feedback or delegating tasks as needed."""),
            backstory=dedent("""\
                As the Creative Director at a leading branding agency,
                you oversee content creation to ensure it meets client expectations."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True
        )
