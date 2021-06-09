import os
from jira import JIRA
from dotenv import load_dotenv


load_dotenv()


def get_jira_client():
    url = os.getenv("JIRA_HOST")
    username = os.getenv("JIRA_USERNAME")
    api_token = os.getenv("JIRA_API_TOKEN")
    jira_options = {'server': url}
    try:
        return JIRA(jira_options, basic_auth=(username, api_token))
    except Exception as e:
        if e.status_code == 401:
            raise ("JIRA authentication failed.")
        else:
            raise
