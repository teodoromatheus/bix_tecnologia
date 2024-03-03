with 
    categorias as (
    select * from {{ ref("dim_categorias") }}
    ),
    funcionarios as (
    select * from {{ ref("dim_funcionarios") }}
    ),
    vendas as (
    select * from {{ source("raw_data","vendas") }}
    ),
    fato_vendas as (
        select  vendas.id_venda
                , funcionarios.sk_funcionario as fk_funcionario
                , categorias.sk_categoria as fk_categoria
                , vendas.data_venda
                , vendas.venda
        from vendas
        left join categorias on vendas.id_categoria = categorias.id_categoria
        left join funcionarios on vendas.id_funcionario = funcionarios.id_funcionario
    )

select * from fato_vendas