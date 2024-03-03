with vendas as (
    select  id_venda
            , id_funcionario
            , id_categoria
            , cast(data_venda as date) as data_venda
            , venda
    from {{ source('raw_data','vendas') }}
)

select * from vendas