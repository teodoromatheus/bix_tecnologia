with selected as (
    select  row_number() over (order by id_funcionario) as sk_funcionario
            , id_funcionario
            , nome_funcionario
    from {{ ref("stg_funcionarios") }}
)

select * from selected