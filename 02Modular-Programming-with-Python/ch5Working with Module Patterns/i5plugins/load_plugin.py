import importlib
import sys
import os.path

plugin_name = input("Load plugins: ")
if plugin_name != "":
    print("os.path.dirname(__file__)=", os.path.dirname(__file__))
    plugin_dir = os.path.join(os.path.dirname(__file__), "plugins")
    sys.path.append(plugin_dir)
    plugin = importlib.import_module(plugin_name)
    plugin.say_hello()