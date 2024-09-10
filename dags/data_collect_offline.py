import json
import os
from scripts.tache_2 import tache2
from scripts.tache_1 import crew as tache1_crew
from scripts.tache_3 import tache3
from scripts.tache6 import run as run_tache6
from scripts.minio_utils import PythonMinIOUtils
import tempfile


os.environ["GROQ_API_KEY"] = "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"
os.environ["SERPER_API_KEY"] = "c9a40a7795c62c6b79e9125c75561478bddd121e"

"""
def task_1():
    result = tache1_crew.kickoff()
    
    minio_utils = PythonMinIOUtils(
        endpoint="play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        secure=True,
        bucket_name="test",
    )
    print("---------------------------------")
    print(type(result))
    print(json.loads(dict(result)['raw']))
    data = json.loads(dict(result)['raw'])
    
    for elt in data['evenement']:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            print(temp_file.name)
            temp_file.write(json.dumps(elt).encode('utf-8'))
            file_path = temp_file.name

        folder_name = elt["nom"]
        file_name = "tache1.json"

        minio_utils.upload_file(folder_name, file_path, file_name)


def task_2():
    minio_utils = PythonMinIOUtils(
        endpoint="play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        secure=True,
        bucket_name="test",
    )

    file_by_folder = minio_utils.list_files_grouped_by_folder()

    for elt in file_by_folder.keys():

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            download_path = temp_file.name
            minio_utils.download_file(elt+"/tache1.json", download_path)

        result = tache2(download_path)

        with tempfile.NamedTemporaryFile(delete=False) as temp_file1:
            data = json.loads(dict(result)['raw'])
            temp_file1.write(bytes(json.dumps(data), "utf-8"))
            file_path = temp_file1.name

        minio_utils.upload_file(elt, file_path, "tache2.json")

def task_3():
    minio_utils = PythonMinIOUtils(
        endpoint="play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        secure=True,
        bucket_name="test",
    )

    file_by_folder = minio_utils.list_files_grouped_by_folder()

    for elt in file_by_folder.keys():

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            download_path = temp_file.name
            minio_utils.download_file(elt+"/tache1.json", download_path)

        result = tache3(download_path)

        with tempfile.NamedTemporaryFile(delete=False) as temp_file1:
            data = json.loads(dict(result)['raw'])
            temp_file1.write(bytes(json.dumps(data), "utf-8"))
            file_path = temp_file1.name

        minio_utils.upload_file(elt, file_path, "tache3.json")

"""
def task_4():
    minio_utils = PythonMinIOUtils(
        endpoint="play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        secure=True,
        bucket_name="test",
    )

    file_by_folder = minio_utils.list_files_grouped_by_folder()

    for elt in file_by_folder.keys():

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            download_path = temp_file.name
            minio_utils.download_file(elt+"/tache1.json", download_path)

        result = tache2(download_path)

        with tempfile.NamedTemporaryFile(delete=False) as temp_file1:
            data = json.loads(dict(result)['raw'])
            temp_file1.write(bytes(json.dumps(data), "utf-8"))
            file_path = temp_file1.name

        minio_utils.upload_file(elt, file_path, "tache4.json")

"""

def task_6():
    minio_utils = PythonMinIOUtils(
        endpoint="play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        secure=True,
        bucket_name="test",
    )

    file_by_folder = minio_utils.list_files_grouped_by_folder()

    for elt in file_by_folder.keys():

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            download_path = temp_file.path
            minio_utils.download_file(elt, "tache1.json", download_path)

        result = run_tache6(download_path)

        with tempfile.NamedTemporaryFile(delete=False) as temp_file1:
            temp_file1.write(json.dumps(result))
            file_path = temp_file1.path

        minio_utils.upload_file(elt, file_path, "tache6.json")


def task_7():
    minio_utils = PythonMinIOUtils(
        endpoint="play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        secure=True,
        bucket_name="test",
    )

    file_by_folder = minio_utils.list_files_grouped_by_folder()

    for elt in file_by_folder.keys():

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            download_path = temp_file.path
            minio_utils.download_file(elt, "tache1.json", download_path)

        result = tache3(download_path)

        with tempfile.NamedTemporaryFile(delete=False) as temp_file1:
            temp_file1.write(json.dumps(result))
            file_path = temp_file1.path

        minio_utils.upload_file(elt, file_path, "tache7.json")

"""

# task_1()
# task_2()
# task_3()
task_4()
# task_6()
# task_7()
