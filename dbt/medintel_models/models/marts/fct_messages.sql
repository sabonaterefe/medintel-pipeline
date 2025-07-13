SELECT
  id,
  channel,
  message_date,
  message_length,
  has_image,
  image_path
FROM {{ ref('stg_telegram_messages') }}
