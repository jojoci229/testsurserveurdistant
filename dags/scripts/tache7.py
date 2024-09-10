
import warnings
warnings.filterwarnings("ignore")
import json
from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool, SerperDevTool
from langchain_groq import ChatGroq
import os

# Initialisation de l'API Key
os.environ["GROQ_API_KEY"] = "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"
os.environ["SERPER_API_KEY"] = "859477bb91d2ad0b4dd8774ba46d6f2e226d15a7"


# llm_groq = ChatGroq(temperature=0, groq_api_key='', model_name="llama-3.1-70b-versatile")
llm_groq = ChatGroq(temperature=0, groq_api_key='', model_name="llama-3.1-8b-instant")

# Outil de recherche spécifique au Bénin
tool = SerperDevTool(
    country="bj",                 # Code ISO du Bénin
    locale="fr",                  # Langue principale utilisée au Bénin
    location="Bénin, Africa",             # Localisation spécifique 
    n_results=100
)

def tache7(filepath):
    file_read_tool =  FileReadTool(file_path=filepath)
    # Agent pour enrichir les événements
    agent = Agent(
        role="Event Enricher",
        goal="Enrichir les données des événements touristiques avec des descriptions détaillées et des sources fournie par l'outil en entrée",
        backstory="Tu es un expert en enrichissement des informations sur les événements touristiques. Ta tâche est de fournir des descriptions détaillées enrichies et des sources pour chaque événement.",
        verbose=True,
        llm=llm_groq,
        tools=[file_read_tool, tool]
    )
        
    # Agent collecteur d'informations
    agent_collect = Agent(
    role="Event media research specialist",
        goal="Chercher les URL des images et vidéos relatives à l'événement spécifié en entrée",
        backstory="Tu es expert en recherche d'images et de vidéos pour divers événements",
        verbose=True,
        llm=llm_groq,
        tools=[tool]
    )


    # Tâche pour rechercher les compagnies aériennes
    task = Task(
        description=(
                    "Lire les données en fournie en entrée sur l'événement. "
                    "Chercher les URL des images et vidéos disponibles relatives à l'événement spécifié en entrée. "
                ),
                expected_output=(
                    "Un objet JSON. "
                    "La sortie doit compter uniquement du JSON sans texte supplémentaire. "
                    "Dans l'objet JSON produit, inclure une liste des URL d'images sous la clé 'image_urls' "
                    "et une liste des URL de vidéos sous la clé 'video_urls'."
                ),
        agent=agent_collect
    )


    # Initialisation du Crew
    crew = Crew(
        agents=[agent_collect],
        tasks=[task],
        verbose=True,
    )


    return  crew.kickoff()