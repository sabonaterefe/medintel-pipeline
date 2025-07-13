
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  SELECT *
FROM "postgres"."staging"."fct_messages"
WHERE message_length <= 1
  
  
      
    ) dbt_internal_test