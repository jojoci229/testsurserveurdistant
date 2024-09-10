import warnings

warnings.filterwarnings("ignore")
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_groq import ChatGroq
import os


# Initialisation de l'API Key
os.environ["GROQ_API_KEY"] = "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"
os.environ["SERPER_API_KEY"] = "c9a40a7795c62c6b79e9125c75561478bddd121e"

# llm_groq = ChatGroq(temperature=0, groq_api_key='', model_name="llama-3.1-70b-versatile")
llm_groq = ChatGroq(temperature=0, model_name="llama3-70b-8192", max_retries=2)

# Outil de recherche spécifique au Bénin
tool = SerperDevTool(
    country="bj",  # Code ISO du Bénin
    locale="fr",  # Langue principale utilisée au Bénin
    location="Bénin, Africa",  # Localisation spécifique
    n_results=2,
)

# Agent collecteur d'informations
agent_collect = Agent(
    role="Event research specialist",
    goal="Chercher et lister le nom, la description et la source de tous les évènements au Bénin",
    backstory="Tu es expert en recherche d'évènement'",
    verbose=True,
    llm=llm_groq,
    tools=[tool],
)

# Tâche pour rechercher les compagnies aériennes
task = Task(
    description=(
        "Chercher et lister le nom, la description et la source sous forme de lien clickable de tous les évènements au Bénin"
        "Les informations recherchées doivent inclure le nom, la description et la source des évènements."
    ),
    expected_output=("Un objet JSON avec pour clé 'evenement'."),
    agent=agent_collect,
)

# Initialisation du Crew
crew = Crew(
    agents=[agent_collect],
    tasks=[task],
    verbose=True,
)

