import warnings
import json
from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool, SerperDevTool
from langchain_groq import ChatGroq
import os

# Configuration de l'environnement et des modèles

llm_groq = ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama3-70b-8192",
)

serper_tool = SerperDevTool(
    country="bj",
    locale="fr",
    location="Benin, Afrique, Africa",
    n_results=2,
)


def tache2(filepath):

    file_read_tool = FileReadTool(file_path=filepath)
    # Agent pour enrichir les événements
    agent = Agent(
        role="Event Enricher",
        goal="Enrichir les données des événements touristiques avec des descriptions détaillées et des sources fournie par l'outil en entrée",
        backstory="Tu es un expert en enrichissement des informations sur les événements touristiques. Ta tâche est de fournir des descriptions détaillées enrichies et des sources pour chaque événement.",
        verbose=True,
        llm=llm_groq,
        tools=[file_read_tool, serper_tool],
    )

    # Tâche pour enrichir un événement
    task = Task(
        description=(
            "Enrichir les données des événements touristiques avec des descriptions détaillées et des sources fournie par l'outil en entrée"
        ),
        expected_output="Un dictionnaire contenant le nom de l'événement, et une présentation de l'événement enrichie et la source avec un lien si disponible.",
        agent=agent,
    )

    # Crew pour exécuter la tâche
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
    )

    return crew.kickoff()
