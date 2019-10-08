import json
import re
import sys
from src.Commit import Commit

UTF_ENCONDING = "utf-8"
NAME_TAG = 'name'
URL_TAG = 'url'
COMMITS_TAG = 'commits'
GIT_LOG_REGEX = "(.+)\s-\s(.+),\s(.+)\s.*:\s(.+)"

class Project:
    def __init__(self, gitService, name, url):
        self.name = name
        self.url = url
        self.commits = {}
        self.gitService = gitService

    def fetchCommits(self):
        try:
            commitNumber = 0
            rawCommits = self.gitService.fetchCommits(self.url)
            if rawCommits:
                for commitInformation in rawCommits:
                    commitNumber += 1
                    splitCommitInfo = list(filter(None, re.compile(GIT_LOG_REGEX).split(commitInformation)))
                    commitHash = splitCommitInfo[0]
                    author = splitCommitInfo[1]
                    date = splitCommitInfo[2]
                    message = splitCommitInfo[3]
                    self.addCommit(commitHash, author, date, message)
        except IndexError as indexOutOfRangeException:
            sys.stderr.write(f"REGEX PROBLEM FOR {splitCommitInfo} in index {commitNumber}")
            raise indexOutOfRangeException
        except Exception as exception:
            raise exception

    def addCommit(self, commitHash, author, date, message):
        commit = Commit(commitHash, author, date, message)
        print(f"Adding commit for {self.name} - {commitHash} - {author} {date} : {message}")
        self.commits[commitHash] = commit

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

