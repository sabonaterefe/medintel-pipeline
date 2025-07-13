
  create view "postgres"."staging"."fct_messages__dbt_tmp"
    
    
  as (
    SELECT
  stg.id,
  stg.channel,
  stg.message_date,
  CHAR_LENGTH(REGEXP_REPLACE(TRIM(stg.text), '\s+', '', 'g')) AS message_length,
  stg.has_image,
  stg.image_path,
  stg.text
FROM "postgres"."staging"."stg_telegram_messages" AS stg
WHERE CHAR_LENGTH(REGEXP_REPLACE(TRIM(stg.text), '\s+', '', 'g')) > 1
  );