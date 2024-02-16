{#
This is a comment. This macro returns the description of the payment type

with

{% macro name_of_the_function(input1, input2,...) -%}
    sql to run
{%- endmacro %}

you define the function or macro
#}

{% macro get_payment_type_description(payment_type) -%}

    case cast( {{ payment_type }} as integer)
        when 1 then 'Credit card'
        when 2 then 'Cash'
        when 3 then 'No charge'
        when 4 then 'Dispute'
        when 5 then 'Unknown'
        when 6 then 'Voided trip'
        else 'EMPTY'
    end

{%- endmacro %}
