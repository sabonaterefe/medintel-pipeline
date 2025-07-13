SELECT DISTINCT
  message_date::DATE AS date
FROM {{ ref('stg_telegram_messages') }}
