from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool,FileReadTool 
from langchain_groq import ChatGroq
import os


llm_groq = ChatGroq(temperature=0,groq_api_key="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",model_name="llama3-70b-8192")


tool = SerperDevTool(
            country="bj",  # Code ISO du Bénin
            locale="fr",  # Langue principale utilisée au Bénin
            location="Bénin, Africa",  # Localisation spécifique
            n_results=2,
        )
def tache3(filepath):

    file_read_tool = FileReadTool(file_path=filepath)

    agent= Agent (
        role="Events's informations Search Specialist",
        goal="Collecter les informations pratiques sur la liste d'évènements touristiques du bénin fournie par l'outil en entrée, en faisant des rechercher plus approfondies sur internet",
        backstory="Tu es un expert en recherche d'informations pratiques sur les évènements touristiques du Bénin.Ta tâche est de collecter pour chaque évènement les informations suivantes: date et lieu de la dernière édition - date,lieu, horaire et tarifs de la prochaine édition - lieu et localisation géographique de la prochaine édition - source de chaque information sous forme de lien cliquable",
        verbose=True,
        llm=llm_groq,
        tools=[file_read_tool, tool]
    )


    task= Task(
        description=(
            
            "rechercher et lister les informations pratiques sur les évènements touristiques du Bénin contenus dans la liste fournie par l'outil en faisant des rechercher plus approfondies sur internet"
            "Inclure : date et lieu de la dernière édition - date,lieu, horaire et tarifs de la prochaine édition - lieu et localisation géographique de la prochaine édition - source de chaque information sous forme de lien cliquable "
        ),
        expected_output="un objet json comme réponse avec pour clé le nom de chaque évènement touristique",
        agent=agent
    )

    crew = Crew(
        agents= [agent],
        tasks= [task],
        verbose=True,
    )

    return crew.kickoff()

