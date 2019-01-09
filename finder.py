import sublime_plugin
import subprocess
import os


class FinderCommand:
    def get_path(self, path):
        if path:
            return path

        if self.window.active_view():
            file = self.window.active_view().file_name()
            if file:
                return file

        if self.window.folders():
            return self.window.folders()[0]

        pd = self.window.project_data()
        if pd and "folders" in pd and len(pd["folders"]) > 0:
            project_path = pd["folders"][0].get("path")
            if project_path:
                return project_path

        return '.'


class OpenFinderCommand(sublime_plugin.WindowCommand, FinderCommand):
    def run(self, path=""):

        path = self.get_path(path)
        
        # Cross-platform idea from: https://github.com/kallepersson/Sublime-Finder/issues/8
        self.window.run_command("open_dir", {"dir": os.path.dirname(path)})
