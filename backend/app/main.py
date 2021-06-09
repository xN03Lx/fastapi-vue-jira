from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.mongo import DB
from .tasks import (
    get_and_save_all_projects_from_jira,
    get_and_save_issues_by_project_from_jira,
)
from .querys import query_issues_project_group_by_status


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#TODO: add pydantic


def projects_exists_in_db() -> bool:
    list_collections = DB.list_collection_names()
    if "projects" not in list_collections:
        return False
    return True


@app.get("/api/projects/")
async def get_all_projects():
    if not projects_exists_in_db():
        get_and_save_all_projects_from_jira()
    projects = DB.projects.find({}, {"_id": 0})
    return list(projects)


@app.get("/api/projects/{project_id}/")
async def get_project(project_id: str):
    project = DB.projects.find_one({"id": project_id}, {"_id": 0})
    return dict(project)


@app.get("/api/projects/{project_id}/issues")
async def get_all_issues_by_project(project_id: str):
    cursor = DB.issues.aggregate(
        query_issues_project_group_by_status(project_id)
    )
    result = list(cursor)
    if len(result) == 0:
        get_and_save_issues_by_project_from_jira(project_id)
        result = DB.issues.aggregate(
            query_issues_project_group_by_status(project_id)
        )
    return list(result)


@app.get("/api/issues/")
async def get_all_issues():
    issues = DB.issues.find({}, {"_id": 0})
    return list(issues)


@app.get("/api/issues/{issue_id}")
async def get_issue(issue_id: str):
    issues = DB.issues.find_one({"id": issue_id}, {"_id": 0})
    return dict(issues)
