import subprocess
import sys

RM_FOLDER_COMMAND = ['rm', '-rf']
GIT_CLONE_COMMMAND = ['git', 'clone', '-n']
GIT_LOG_COMMAND = ['git', 'log', '--pretty=format:"%h - %an, %ad : %s"']
UTF_ENCONDING = "utf-8"

class GitCLI:
    def fetchCommits(self, url):
        name = self.getProjectNameFromURL(url)
        subprocess.run(GIT_CLONE_COMMMAND+[url])
        output = subprocess.run (GIT_LOG_COMMAND, stdout=subprocess.PIPE, cwd=f"./{name}")
        gitLogRestuls = str(output.stdout.decode(UTF_ENCONDING)).replace("\"", "").split("\n")
        subprocess.run(RM_FOLDER_COMMAND+[name])

        print(f"{gitLogRestuls}")
        return gitLogRestuls

    def getProjectNameFromURL(self, url):
        name = str(url).split("/")[1].split(".")[0]
        return name


if __name__ == '__main__':
    gitCLI = GitCLI()
    gitCLI.fetchCommits(sys.argv[1])