import logging
from config.mongo import DB
from config.jira import get_jira_client
from .utils import build_data_project, build_data_user, build_data_issue


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


#TODO: use asyncio tasks
def get_and_save_all_projects_from_jira():
    jira_client = get_jira_client()
    projects = jira_client.projects()
    list_projects = []
    for project in projects:
        logging.info("Loading projects...")
        project_data_complete = jira_client.project(project.id)
        project_data = build_data_project(project_data_complete)
        list_projects.append(project_data)
    DB.projects.insert_many(list_projects)


#TODO: use asyncio tasks
def get_and_save_issues_by_project_from_jira(key):
    project = f"project={key}"
    size = 100
    initial = 0
    start = initial * size
    issues = get_jira_client().search_issues(project, start, size)
    #if len(issues) == 0:
    #    break
    initial = 1
    list_issues = []
    for issue in issues:
        logging.info("Loading issue...")
        assignes = []
        status = getattr(issue.fields.status, "name", None)
        if status != None and status not in status:
            status.append(status)
        if issue.fields.assignee != None:
            try:
                for user in issue.fields.assignee:
                    user = build_data_user(issue.fields.assignee)
                    assignes.append(user)
            except:
                user = build_data_user(issue.fields.assignee)
                assignes.append(user)

        list_issues.append(build_data_issue(issue, assignes))
    DB.issues.insert_many(list_issues)
