
  create view "postgres"."staging"."dim_channels__dbt_tmp"
    
    
  as (
    SELECT DISTINCT
  channel AS channel_name,
  NULL::TEXT AS channel_type -- Optional enrichment
FROM "postgres"."staging"."stg_telegram_messages"
  );