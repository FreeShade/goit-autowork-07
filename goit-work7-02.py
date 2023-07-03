from setuptools import setup


def do_setup(args_dict, requires):
    args_dict["install_requieres"] = requires
    setup(**args_dict)
