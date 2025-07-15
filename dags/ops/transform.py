from dagster import op
import subprocess

@op
def run_dbt_transformations(load_result):
    # Your transform logic
    subprocess.run(["dbt", "run"], check=True)
    subprocess.run(["dbt", "test"], check=True)
    return "transformed"
