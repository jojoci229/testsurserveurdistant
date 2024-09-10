import warnings
warnings.filterwarnings("ignore")

from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, FileReadTool
from langchain_groq import ChatGroq
import os


os.environ["GROQ_API_KEY"] = "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"
os.environ["SERPER_API_KEY"] = "36d236523f043f3f653f3544471dc42883a5785e"

serper_tool = SerperDevTool(
    country="bj",
    locale="fr",
    location="Benin, Afrique, Africa",
    n_results=10,
)

llm_groq = ChatGroq(temperature=0, groq_api_key="", model_name="llama-3.1-8b-instant")


def run(filepath):
    file_read_tool = FileReadTool(file_path=filepath)

    agent = Agent(
        role="Event Research Specialist",
        goal="Chercher et Trouver les temoignages, les commentaires, et les liens des sites web sur les evenements du Benin",
        backstory="Tu es un expert en recherche d'informations sur les evenements du Bénin. Ton rôle est d'identifier les temoignages, les commentaires en plus des liens du site web sur les evenements du Bénin.",
        verbose=True,
        llm=llm_groq,
        tools=[file_read_tool, serper_tool],
    )

    task = Task(
        description=(
            "Lire les données en entrée fourni par l'outil. "
            "Recuperer les informations sur l'evenement du Benin. "
            "Trouver et Collecter les temoignages et les commentaires des participants à cet evenement. "
            "Trouver en plus les liens du site web où les temoignages ont été collectés."
        ),
        agent=agent,
        expected_output=(
            "Un objet JSON. "
            "La sortie doit comptenir seulement de json et rien de plus sans ```json ...```. "
            "Dans l'objet JSON produit, il faut retirer la clé 'description'."
        ),
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
    )

    return crew.kickoff()
