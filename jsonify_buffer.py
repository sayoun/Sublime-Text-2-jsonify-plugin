import sublime, sublime_plugin
import json

class JsonifyBufferCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        sel = view.sel()

        for s in sel:
            buffy = json.loads(view.substr(s))
            view.replace(edit, s, json.dumps(buffy, sort_keys=True, indent=4))
