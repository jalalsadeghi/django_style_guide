import os
import shutil


project_name = "{{cookiecutter.project_name}}"
project_slug = "{{cookiecutter.project_slug}}"
lisence = "{{cookiecutter.license}}"
jwt = "{{cookiecutter.use_auth}}"
debug_toolbar = "{{cookiecutter.debug_toolbar}}"
files = "{{cookiecutter.files}}"

def delete_resource(resource):
    if os.path.isfile(resource):
        print(f"removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"removing directory: {resource}")
        shutil.rmtree(resource)


if lisence == "None":
    delete_resource("LICENSE")

if jwt != "jwt":
    delete_resource(f"{project_slug}/authentication/")
    delete_resource(f"{project_slug}/users/")

if files != "y":
    delete_resource(f"{project_slug}/files/")
    delete_resource(f"{project_slug}/integrations/")
    delete_resource(f"config/settings/files_and_storages.py")

if debug_toolbar != "y":
    delete_resource(f"config/settings/debug_toolbar/")


