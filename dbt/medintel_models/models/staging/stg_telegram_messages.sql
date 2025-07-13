SELECT
  id,
  channel,
  CAST(date AS TIMESTAMP) AS message_date,
  LENGTH(text) AS message_length,
  has_image,
  image_path,
  text
FROM raw.telegram_messages
