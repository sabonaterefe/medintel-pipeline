SELECT DISTINCT
  message_date::DATE AS date,
  EXTRACT(DAY FROM message_date) AS day,
  EXTRACT(WEEK FROM message_date) AS week,
  EXTRACT(MONTH FROM message_date) AS month,
  EXTRACT(YEAR FROM message_date) AS year
FROM {{ ref('stg_telegram_messages') }}
WHERE message_date IS NOT NULL
