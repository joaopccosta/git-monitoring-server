import json
import unittest

from mock import Mock

from src.Project import Project

FAKE_PROJECT_NAME = "fakeProject"
FAKE_PROJECT_URL = "fake/project/url.git"
FAKE_COMMIT_DATA = ["c34c2ac - Joao, Sat May 25 11:04:54 2019 +0100 : git ignore added",
                    "db93f9e - Joao, Sat May 25 11:03:35 2019 +0100 : Initial commit. Unit tests."
                    ]
FAKE_PROJECT_JSON = {"name": "fakeProject", "url": "fake/project/url.git", "commits": [
    {"hash": "c34c2ac", "author": "Joao", "date": "Sat May 25 11:04:54 2019", "message": "git ignore added"},
    {"hash": "db93f9e", "author": "Joao", "date": "Sat May 25 11:03:35 2019",
     "message": "Initial commit. Unit tests."}]}


class ProjectTest(unittest.TestCase):

    def test_givenAProject_internalListOfCommitsIsEmpty(self):
        mockCodacyCLI = Mock()
        project = Project(mockCodacyCLI, FAKE_PROJECT_NAME, FAKE_PROJECT_URL)
        self.assertEqual(len(project.commits), 0)

    def test_givenAProject_whenAddingCommit_internalListOfCommitsGrows(self):
        mockCodacyCLI = Mock()
        project = Project(mockCodacyCLI, FAKE_PROJECT_NAME, FAKE_PROJECT_URL)
        project.addCommit("c34c2ac", "Joao", "Sat May 25 11:04:54 2019", "git ignore added")
        self.assertEqual(len(project.commits), 1)

    def test_givenAProject_whenFetchIsInvoked_internalListOfCommitsIsNotEmpty(self):
        mockCodacyCLI = Mock()
        mockCodacyCLI.fetchCommits.return_value = FAKE_COMMIT_DATA
        project = Project(mockCodacyCLI, FAKE_PROJECT_NAME, FAKE_PROJECT_URL)
        project.fetchCommits()
        mockCodacyCLI.fetchCommits.assert_called_once()
        self.assertEqual(len(project.commits), len(FAKE_COMMIT_DATA))

    def test_givenAProject_whenToJsonIsInvoked_internalListOfCommitsIsTransformedToJsonString(self):
        mockCodacyCLI = Mock()
        mockCodacyCLI.fetchCommits.return_value = FAKE_COMMIT_DATA
        project = Project(mockCodacyCLI, FAKE_PROJECT_NAME, FAKE_PROJECT_URL)
        project.fetchCommits()
        expectedJson = json.dumps(FAKE_PROJECT_JSON)
        self.assertEqual(project.toJson(), expectedJson)


if __name__ == "__main__":
    unittest.main()
