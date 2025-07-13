SELECT DISTINCT
  channel AS channel_name,
  NULL::TEXT AS channel_type -- Optional enrichment
FROM {{ ref('stg_telegram_messages') }}
