import unittest

from src.GitCLI import GitCLI

PROJECT_NAME = "url"
FAKE_PROJECT_URL = "fake/project/%s.git" % PROJECT_NAME

class MyTestCase(unittest.TestCase):
    def test_whenGetProjectNameFromURL_givenAURL_returnsCorrectProjectName(self):
        expectedProjectName = PROJECT_NAME
        gitCLI = GitCLI()
        self.assertEqual(expectedProjectName, gitCLI.getProjectNameFromURL(FAKE_PROJECT_URL))

if __name__ == '__main__':
    unittest.main()
