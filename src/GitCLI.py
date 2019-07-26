import subprocess
import sys

import Constants


class CodacyCLI:
    def fetchCommits(self, url):
        name = self.getProjectNameFromURL(url)
        subprocess.run(Constants.GIT_CLONE_COMMMAND+[url])
        output = subprocess.run (Constants.GIT_LOG_COMMAND, stdout=subprocess.PIPE, cwd=f"./{name}")
        gitLogRestuls = str(output.stdout.decode(Constants.UTF_ENCONDING)).replace("\"", "").split("\n")
        subprocess.run(Constants.RM_FOLDER_COMMAND+[name])

        print(f"{gitLogRestuls}")
        return gitLogRestuls

    def getProjectNameFromURL(self, url):
        name = str(url).split("/")[1].split(".")[0]
        return name


if __name__ == '__main__':
    codacyCLI = CodacyCLI()
    codacyCLI.fetchCommits(sys.argv[1])