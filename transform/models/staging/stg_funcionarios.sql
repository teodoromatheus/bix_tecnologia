with funcionarios as (
    select  id_funcionario
            , nome_funcionario
    from {{ source('raw_data','funcionarios') }}
)

select * from funcionarios