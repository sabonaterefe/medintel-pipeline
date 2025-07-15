from dagster import op
import scripts.enrich_images

@op
def run_yolo_enrichment(transform_result):
    scripts.enrich_images.main()
