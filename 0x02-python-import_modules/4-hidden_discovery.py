#!/usr/bin/python3
if __name__ == "__main__":

    import importlib
    module = importlib.import_module("hidden_4")
    names = dir(module)
    names = [name for name in names if not name.startswith("__")]
    names.sort()
    for name in names:
        print(name)
