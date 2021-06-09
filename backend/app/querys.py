def query_issues_project_group_by_status(project_id, issues=True):
    query = [
        {"$match": {"project.id": project_id}},
        {
            "$group": {
                "_id": "$status",
                "count": {"$sum": 1},
                "key": {"$first":"$id"},

            }
        },
    ]

    if issues:
        query[1]["$group"]["issues"] = {
            "$push": {
                "id": "$id",
                "issueKey": "$issueKey",
                "summary": "$summary",
                "description": "$description",
                "issueType": "$issueType",
                "status": "$status",
                "assignes": "$assignes",
                "labels": "$label",
                "created": "$created",
                "update": "$updated",
                "reporter": "$reporter",
                "project": "$project",
            }
        }
    return query

