import json
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
import tempfile


@dag(
    start_date=days_ago(1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "RINTIO", "retries": 3},
    tags=["scraper", "ai_agent"],
)
def sublime_benin_data_collect():
    @task.virtualenv(
        task_id="task_1",
        requirements=["minio==7.2.8", "streamlit==1.37.1", "crewai==0.51.1", "crewai_tools==0.8.3",
                      "langchain_community==0.2.12", "langchain_groq==0.1.9", "langchain==0.2.14"],
        system_site_packages=False
    )
    def task_1():
        from scripts.tache_1 import crew as tache1_crew
        from scripts.minio_utils import PythonMinIOUtils
        result = tache1_crew.kickoff()
        minio_utils = PythonMinIOUtils(
            endpoint="play.min.io",
            access_key="Q3AM3UQ867SPQQA43P2F",
            secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
            secure=True,
            bucket_name="test")

        for elt in result['évènement']:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                print(temp_file.name)
                temp_file.write(bytes(json.dumps(elt), 'utf-8'))
                file_path = temp_file.name

            folder_name = elt["nom"]
            file_name = "tache1.json"

            minio_utils.upload_file(folder_name, file_path, file_name)

    @task.virtualenv(
        task_id="task_2",
        requirements=["minio==7.2.8", "streamlit==1.37.1", "crewai==0.51.1", "crewai_tools==0.8.3",
                      "langchain_community==0.2.12", "langchain_groq==0.1.9", "langchain==0.2.14"],
        system_site_packages=False
    )
    def task_2():
        from scripts.tache_2 import tache2
        from scripts.minio_utils import PythonMinIOUtils
        minio_utils = PythonMinIOUtils(
            endpoint="play.min.io",
            access_key="Q3AM3UQ867SPQQA43P2F",
            secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
            secure=True,
            bucket_name="test")

        file_by_folder = minio_utils.list_files_grouped_by_folder()

        for elt in file_by_folder.keys():
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                download_path = temp_file.name
                minio_utils.download_file(elt + "/tache1.json", download_path)

            result = tache2(download_path)

            with tempfile.NamedTemporaryFile(delete=False) as temp_file1:
                temp_file1.write(json.dumps(result))
                file_path = temp_file1.path

            minio_utils.upload_file(elt, file_path, "tache2.json")

    @task.virtualenv(
        task_id="task_3",
        requirements=["minio==7.2.8", "streamlit==1.37.1", "crewai==0.51.1", "crewai_tools==0.8.3",
                      "langchain_community==0.2.12", "langchain_groq==0.1.9", "langchain==0.2.14"],
        system_site_packages=False
    )
    def task_3():
        from scripts.tache_3 import tache3
        from scripts.minio_utils import PythonMinIOUtils
        minio_utils = PythonMinIOUtils(
            endpoint="play.min.io",
            access_key="Q3AM3UQ867SPQQA43P2F",
            secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
            secure=True,
            bucket_name="test")

        file_by_folder = minio_utils.list_files_grouped_by_folder()

        for elt in file_by_folder.keys():
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                download_path = temp_file.name
                minio_utils.download_file(elt + "/tache1.json", download_path)

            result = tache3(download_path)

            with tempfile.NamedTemporaryFile(delete=False) as temp_file1:
                temp_file1.write(json.dumps(result))
                file_path = temp_file1.path

            minio_utils.upload_file(elt, file_path, "tache3.json")

    @task.virtualenv(
        task_id="task_4",
        requirements=["minio==7.2.8", "streamlit==1.37.1", "crewai==0.51.1", "crewai_tools==0.8.3",
                      "langchain_community==0.2.12", "langchain_groq==0.1.9", "langchain==0.2.14"],
        system_site_packages=False
    )
    def task_4():
        from scripts.tache4 import tache4
        from scripts.minio_utils import PythonMinIOUtils
        minio_utils = PythonMinIOUtils(
            endpoint="play.min.io",
            access_key="Q3AM3UQ867SPQQA43P2F",
            secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
            secure=True,
            bucket_name="test")

        file_by_folder = minio_utils.list_files_grouped_by_folder()

        for elt in file_by_folder.keys():
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                download_path = temp_file.name
                minio_utils.download_file(elt + "/tache1.json", download_path)

            result = tache4(download_path)

            with tempfile.NamedTemporaryFile(delete=False) as temp_file1:
                temp_file1.write(json.dumps(result))
                file_path = temp_file1.path

            minio_utils.upload_file(elt, file_path, "tache4.json")

    @task.virtualenv(
        task_id="task_6",
        requirements=["minio==7.2.8", "streamlit==1.37.1", "crewai==0.51.1", "crewai_tools==0.8.3",
                      "langchain_community==0.2.12", "langchain_groq==0.1.9", "langchain==0.2.14"],
        system_site_packages=False
    )
    def task_6():
        from scripts.tache6 import run as run_tache6
        from scripts.minio_utils import PythonMinIOUtils
        minio_utils = PythonMinIOUtils(
            endpoint="play.min.io",
            access_key="Q3AM3UQ867SPQQA43P2F",
            secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
            secure=True,
            bucket_name="test")

        file_by_folder = minio_utils.list_files_grouped_by_folder()

        for elt in file_by_folder.keys():
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                download_path = temp_file.name
                minio_utils.download_file(elt + "/tache1.json", download_path)

            result = run_tache6(download_path)

            with tempfile.NamedTemporaryFile(delete=False) as temp_file1:
                temp_file1.write(json.dumps(result))
                file_path = temp_file1.path

            minio_utils.upload_file(elt, file_path, "tache6.json")

    @task.virtualenv(
        task_id="task_7",
        requirements=["minio==7.2.8", "streamlit==1.37.1", "crewai==0.51.1", "crewai_tools==0.8.3",
                      "langchain_community==0.2.12", "langchain_groq==0.1.9", "langchain==0.2.14"],
        system_site_packages=False
    )
    def task_7():
        from scripts.tache7 import tache7
        from scripts.minio_utils import PythonMinIOUtils
        minio_utils = PythonMinIOUtils(
            endpoint="play.min.io",
            access_key="Q3AM3UQ867SPQQA43P2F",
            secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
            secure=True,
            bucket_name="test")

        file_by_folder = minio_utils.list_files_grouped_by_folder()

        for elt in file_by_folder.keys():
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                download_path = temp_file.name
                minio_utils.download_file(elt + "/tache1.json", download_path)

            result = tache7(download_path)

            with tempfile.NamedTemporaryFile(delete=False) as temp_file1:
                temp_file1.write(json.dumps(result))
                file_path = temp_file1.path

            minio_utils.upload_file(elt, file_path, "tache7.json")

    # Define task dependencies
    t1 = task_1()
    t2 = task_2()
    t3 = task_3()
    t4 = task_4()
    t6 = task_6()
    t7 = task_7()

    t1 >> [t2, t3, t4, t6, t7]


# Instantiate the DAG
sublime_benin_data_collect()
