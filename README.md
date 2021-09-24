# Welcome to Gumbys' Django Cookiecutter

In this repository you will find a custom cookiecutter template with an extensive Django setup.\
This includes the following:
- A Django project boilerplate with some commonly used extra, such as debug_toolbar, 
django_extensions and the Django Rest Framework.
- A Docker environment with docker-compose, so that both the project and its database are dockerized.
- WIP: serverless environment for deployment to aws.


## What is cookiecutter?

Cookiecutter is a handy tool that will allow you to quickly setup new projects if you often reuse similar setups.
It allows you - with the help of Jinja - to create templates for your project. 
You can use Jinja in the content of your files, but also in your file and directory names, 
which makes it perfect to create whole projects.

More info on cookiecutter: [PyPi](https://pypi.org/project/cookiecutter/) / 
                           [Documentation]( https://cookiecutter.readthedocs.io) / 
                           [Github](https://github.com/cookiecutter/cookiecutter)

Keep reading to setup your project with this cookiecutter.

## Using this cookiecutter

1. Install cookiecutter by following [this guide](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
2. In your terminal, go to the folder you want to create your new project in.
3. If you have never used this cookiecutter before, run: `cookiecutter gh:DaanVandenreyt/DCG`
   - the 'gh' is a shortcut built into cookiecutter for working with github repo's
4. If it is not the first time, the cookiecutter will be available locally in any location, you just use: `cookiecutter DCG`


