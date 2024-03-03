with categorias as (
    select  id as id_categoria
            , nome_categoria
    from {{ source('raw_data','categorias') }}
)

select * from categorias