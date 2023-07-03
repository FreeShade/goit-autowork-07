from setuptools import setup


def do_setup(args_dict, requires, entry_points):
    args_dict["install_requires"] = requires
    args_dict["entry_points"] = entry_points
    setup(**args_dict)
