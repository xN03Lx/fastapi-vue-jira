def build_data_user(data):
    return {
        "accountId": getattr(data, "accountId", ""),
        "avatarUrls": getattr(data.avatarUrls, "16x16", ""),
        "displayName": data.displayName,
        "emailAddress": getattr(data, "emailAddress", ""),
        "accountType": getattr(data, "accountType", ""),
    }


def build_data_project(project, statuses=None):
    data = {
        "projectTypeKey": project.projectTypeKey,
        "key": project.key,
        "name": project.name,
        "isPrivate": getattr(project, "isPrivate", ""),
        "id": project.id,
        "entityId": getattr(project, "entityId", ""),
        "uuid": getattr(project, "uuid", ""),
    }
    if getattr(project, "lead", None):
        data["lead"] = build_data_user(project.lead)
    if statuses:
        data["statuses"] = statuses

    return data


def build_data_issue(issue, assignes):
    return {
        "id": issue.id,
        "issueKey": issue.key,
        "summary": issue.fields.summary,
        "description": issue.fields.description,
        "issueType": issue.fields.issuetype.name,
        "status": issue.fields.status.name,
        "assignes": assignes,
        "labels": issue.fields.labels,
        "created": issue.fields.created,
        "update": issue.fields.updated,
        "reporter": build_data_user(issue.fields.reporter),
        "project": build_data_project(issue.fields.project),
    }
