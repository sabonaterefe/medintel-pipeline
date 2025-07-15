SELECT
  message_id,
  detected_object_class,
  confidence_score
FROM {{ source('medintel', 'image_detections') }}
