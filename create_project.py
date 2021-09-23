from cookiecutter.main import cookiecutter
import inflection
import json
import os


def get_project_dir():
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    use_default = input(f"The default directory for your project is '{project_dir}'.\n"
                        f"Do you want to use this one? [y/n]")

    while use_default not in ['y', 'n']:
        use_default = input("Invalid response, please reply with 'y' or 'n': ")

    if use_default == 'y':
        return project_dir

    new_dir = input(
        'Please give your desired directory as an absolute path or one relative to the current directory:\n')
    while True:
        if not os.path.isabs(new_dir):
            new_dir = os.path.abspath(os.path.join(project_dir, new_dir))
        if os.path.isdir(new_dir):
            return new_dir
        new_dir = input('The given path does not exist, try again:\n')


# with open('./my-django-cookiecutter/cookiecutter.json') as cookies_file:
#     data = json.load(cookies_file)
#
#     print('==== Script inputs ====')
#
#     for key, value in data.items():
#         if key == 'project_name_cases':
#             continue
#
#         user_input = input(f'{key}[{value}]:')
#         if user_input:
#             data[key] = user_input
#
#     print('==== Cookiecutter inputs ====')
#
#     # Set different casing options for the project name, starting with snake_case gives the best results with inflection
#     project_name_snake = inflection.parameterize(data['project_name']).replace('-', '_')
#     cases = {
#         'camel': inflection.camelize(project_name_snake, False),
#         'pascal': inflection.camelize(project_name_snake),
#         'snake': project_name_snake,
#         'hyphens': inflection.dasherize(project_name_snake)
#     }
#     data['project_name_cases'] = cases
#
#     cookiecutter('my-django-cookiecutter', no_input=True, extra_context=data)

if __name__ == '__main__':
    print(os.path.join(os.path.dirname(__file__)))
    project_dir = get_project_dir()
    print(project_dir)
