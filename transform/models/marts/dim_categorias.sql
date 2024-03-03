with selected as (
    select  row_number() over (order by id_categoria) as sk_categoria
            , id_categoria
            , nome_categoria
    from {{ ref("stg_categorias") }}
)

select * from selected