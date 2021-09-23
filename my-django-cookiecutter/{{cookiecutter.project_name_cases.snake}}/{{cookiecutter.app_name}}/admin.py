from {{cookiecutter.app_name}} import models
from django.contrib import admin

admin.site.site_header = '{{cookiecutter.project_name}}'
# {{cookiecutter.project_name_cases.camel}}

@admin.register(models.{{cookiecutter.first_model}})
class {{cookiecutter.first_model}}Admin(admin.ModelAdmin):
    ...
