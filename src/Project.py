import json
import re

from src.Commit import Commit

UTF_ENCONDING = "utf-8"
NAME_TAG = 'name'
URL_TAG = 'url'
COMMITS_TAG = 'commits'
GIT_LOG_REGEX = "([a-z,A-Z,0-9]+)\s-\s([A-zÀ-ú,0-9,\s,\.-]+),\s([a-z,A-Z,0-9,\s,\:]+)\s.*:\s(.*)"

class Project:
    def __init__(self, gitService, name, url):
        self.name = name
        self.url = url
        self.commits = {}
        self.gitService = gitService

    def fetchCommits(self):
        try:
            i = 0
            rawCommits = self.gitService.fetchCommits(self.url)
            if rawCommits:
                for commitInformation in rawCommits:
                    i += 1
                    splitCommitInfo = list(filter(None, re.compile(GIT_LOG_REGEX).split(commitInformation)))
                    hash = splitCommitInfo[0]
                    author = splitCommitInfo[1]
                    date = splitCommitInfo[2]
                    message = splitCommitInfo[3]
                    self.addCommit(hash, author, date, message)

        except Exception as exception:
            raise exception

    def addCommit(self, hash, author, date, message):
        commit = Commit(hash, author, date, message)
        print(f"Adding commit for {self.name} - {hash} - {author} {date} : {message}")
        self.commits[hash] = commit

    def toJson(self):
        data = {}
        data[NAME_TAG] = self.name
        data[URL_TAG] = self.url
        data[COMMITS_TAG] = []

        for commit in self.commits.values():
            data[COMMITS_TAG].append(commit.toJson())

        return json.dumps(data)

    def __str__(self):
        string = self.name
        string += "\n###\n"
        for commit in self.commits.values():
            print(f"Commit {commit}")
            string += commit.__str__()
            string += "\n"
        return string

