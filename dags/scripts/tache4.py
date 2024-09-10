from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool,FileReadTool 
from  langchain_groq import ChatGroq
import os

os.environ["OPENAI_API_KEY"] ="NA"
os.environ["SERPER_API_KEY"] = "eadf5804abf877efa66a320fb74dcfe9ea1306bb"

llm_groq = ChatGroq(temperature=0,groq_api_key="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",model_name="llama-3.1-70b-versatile")


tool = SerperDevTool(
            country="bj",  # Code ISO du Bénin
            locale="fr",  # Langue principale utilisée au Bénin
            location="Bénin, Africa",  # Localisation spécifique
            n_results=200,
        )
def tache4(filepath):

    file_read_tool = FileReadTool(file_path=filepath)

    agent= Agent (
        role="Search organisator's event Specialist",
        goal="Pour chacun des evenements trouve moi les contacts des organisateurs fournie par l'outil en entrée",
        backstory="Tu es un expert en organisations des evenements, recherche moi les differents contacts des organisateurs",
        verbose=True,
        llm=llm_groq,
        tools=[file_read_tool, tool]
    )


    task= Task(
        description=(
                "Lire les données fournie par l'outil en entrée"
                "Trouve moi pour les contacts possibles des organisateurs des evements au Bénin. "
                "Inclure le numero de téléphonne, le mail, le faceboock, l'adresse mail, site web, twitter,son ticktock si possible."
                "Trouver en plus les liens du site des informations recuillis."
            ),
            agent=agent,
            expected_output=(
                "Un objet JSON. "
                "La sortie doit comptenir seulement de json et rien de plus sans ```json ...```. "
                "Dans l'objet JSON produit, il faut retirer la clé 'description'."
            )
    )

    crew = Crew(
        agents= [agent],
        tasks= [task],
        verbose=True,
    )

    return crew.kickoff()

