"""

{% macro lower_first(text) %}
    {{ text[0]|upper}}{{text[1:] }}
{% endmacro %}

{% macro snake_case(text) %}
    {{ text|lower|replace(' ', '_') }}
{% endmacro %}

{% macro pascal_case(text) %}
    {{ text|replace(' ', '') }}
{% endmacro %}

{% macro camel_case(text) %}
    {{ lower_first(pascal_case(text)) }}
{% endmacro %}

{% macro flat_case(text) %}
    {{ text|lower|replace(' ', '') }}
{% endmacro %}

{% macro slugify(text) %}
    {{ text|lower|replace(' ', '-') }}
{% endmacro %}

{{ cookiecutter.update({"project_slug": "{{ slugify(cookiecutter.project_name) }}"}) }}
{{ cookiecutter.update({"project_snake": "{{ snake_case(cookiecutter.project_name) }}"}) }}
{{ cookiecutter.update({"project_flat": "{{ flat_case(cookiecutter.project_name) }}"}) }}
{{ cookiecutter.update({"project_camel": "{{ camel_case(cookiecutter.project_name) }}"}) }}

"""