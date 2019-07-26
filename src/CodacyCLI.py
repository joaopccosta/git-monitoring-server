import subprocess
import sys

from src.Constants import *

class CodacyCLI:
    def fetchCommits(self, url):
        name = str(url).split("/")[1].split(".")[0]
        subprocess.run(GIT_CLONE_COMMMAND+[url])
        output = subprocess.run (GIT_LOG_COMMAND, stdout=subprocess.PIPE, cwd=f"./{name}")
        contents = str(output.stdout.decode(UTF_ENCONDING)).replace("\"", "").split("\n")
        print(f"{contents}")
        subprocess.run(RM_FOLDER_COMMAND+[name])

        return contents

if __name__ == '__main__':
    codacyCLI = CodacyCLI()
    codacyCLI.fetchCommits(sys.argv[1])