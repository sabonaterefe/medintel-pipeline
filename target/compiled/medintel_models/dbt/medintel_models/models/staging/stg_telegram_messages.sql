SELECT
  msg.id,
  msg.channel,
  CAST(msg.date AS TIMESTAMP) AS message_date,
  CHAR_LENGTH(REGEXP_REPLACE(TRIM(msg.text), '\s+', '', 'g')) AS message_length,
  msg.has_image,
  msg.image_path,
  msg.text
FROM "postgres"."raw"."telegram_messages" AS msg
WHERE CHAR_LENGTH(REGEXP_REPLACE(TRIM(msg.text), '\s+', '', 'g')) > 1