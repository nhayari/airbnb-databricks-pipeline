# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.70.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


bronze_to_silver = Job.from_dict(
    {
        "name": "bronze_to_silver",
        "tasks": [
            {
                "task_key": "calendar",
                "sql_task": {
                    "file": {
                        "path": "/Workspace/Users/myemail@???.???/airbnb-databricks-pipeline/silver/calendar.sql",
                        "source": "WORKSPACE",
                    },
                    "warehouse_id": "4a91db18b293ba94",
                },
            },
            {
                "task_key": "listings",
                "sql_task": {
                    "file": {
                        "path": "/Workspace/Users/myemail@???.???/airbnb-databricks-pipeline/silver/listings.sql",
                        "source": "WORKSPACE",
                    },
                    "warehouse_id": "4a91db18b293ba94",
                },
            },
            {
                "task_key": "listings_details",
                "sql_task": {
                    "file": {
                        "path": "/Workspace/Users/myemail@???.???/airbnb-databricks-pipeline/silver/listings_details.sql",
                        "source": "WORKSPACE",
                    },
                    "warehouse_id": "4a91db18b293ba94",
                },
            },
            {
                "task_key": "neighberhoods",
                "sql_task": {
                    "file": {
                        "path": "/Workspace/Users/myemail@???.???/airbnb-databricks-pipeline/silver/neighbourhoods_geo.sql",
                        "source": "WORKSPACE",
                    },
                    "warehouse_id": "4a91db18b293ba94",
                },
            },
            {
                "task_key": "reviews_details",
                "sql_task": {
                    "file": {
                        "path": "/Workspace/Users/myemail@???.???/airbnb-databricks-pipeline/silver/reviews_details.sql",
                        "source": "WORKSPACE",
                    },
                    "warehouse_id": "4a91db18b293ba94",
                },
            },
        ],
        "queue": {
            "enabled": True,
        },
    }
)

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.jobs.reset(new_settings=bronze_to_silver, job_id=186406315997448)
# or create a new job using: w.jobs.create(**bronze_to_silver.as_shallow_dict())
