
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select id
from "postgres"."staging"."stg_telegram_messages"
where id is null



  
  
      
    ) dbt_internal_test