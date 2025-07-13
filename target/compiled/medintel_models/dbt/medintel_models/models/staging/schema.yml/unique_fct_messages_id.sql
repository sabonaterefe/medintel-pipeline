
    
    

select
    id as unique_field,
    count(*) as n_records

from "postgres"."staging"."fct_messages"
where id is not null
group by id
having count(*) > 1


