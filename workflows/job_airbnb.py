# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.70.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


airbnb_pipeline = Job.from_dict(
    {
        "name": "airbnb_pipeline",
        "email_notifications": {
            "on_success": [
                "myemail@???.com",
            ],
            "on_failure": [
                "myemail@???.com",
            ],
        },
        "schedule": {
            "quartz_cron_expression": "42 30 2 * * ?",
            "timezone_id": "Europe/Paris",
            "pause_status": "PAUSED",
        },
        "tasks": [
            {
                "task_key": "download",
                "run_job_task": {
                    "job_id": 142753620867121,
                },
            },
            {
                "task_key": "Bronze",
                "depends_on": [
                    {
                        "task_key": "download",
                    },
                ],
                "run_job_task": {
                    "job_id": 481158249657270,
                },
            },
            {
                "task_key": "Silver",
                "depends_on": [
                    {
                        "task_key": "Bronze",
                    },
                ],
                "run_job_task": {
                    "job_id": 186406315997448,
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
w.jobs.reset(new_settings=airbnb_pipeline, job_id=997336968762480)
# or create a new job using: w.jobs.create(**airbnb_pipeline.as_shallow_dict())
