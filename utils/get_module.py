import pkgutil
import inspect


def get_module(path):
    r_list = list()
    for loader, name, is_pkg in pkgutil.walk_packages(path):
        module = loader.find_module(name).load_module(name)

        for name, value in inspect.getmembers(module):
            if name.startswith('__'):
                continue

            globals()[name] = value
            r_list.append(name)

    return r_list
