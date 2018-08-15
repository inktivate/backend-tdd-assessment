import unittest
import echo
import subprocess


class TestEcho(unittest.TestCase):

    def setUp(self):
        """Let us create one parser to rule them all"""
        self.parser = echo.create_parser()

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect its output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper1(self):
        """ Running the program with the -u flag
        should return text in uppercase """

        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = 'HELLO'

        self.assertEquals(stdout.strip('\n'), expected)

    def test_upper2(self):
        """ Running the program with the --upper flag
        should return text in uppercase """

        process = subprocess.Popen(
            ["python", "./echo.py", "--upper", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = 'HELLO'

        self.assertEquals(stdout.strip('\n'), expected)

    def test_lower1(self):
        """ Running the program with the -l flag
        should return text in lowercase """

        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "Hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = 'hello'

        self.assertEquals(stdout.strip('\n'), expected)

    def test_lower2(self):
        """ Running the program with the --lower flag
        should return text in lowercase """

        process = subprocess.Popen(
            ["python", "./echo.py", "--lower", "Hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = 'hello'

        self.assertEquals(stdout.strip('\n'), expected)

    def test_title1(self):
        """ Running the program with the -t flag
        should return text in titlecase """

        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = 'Hello'

        self.assertEquals(stdout.strip('\n'), expected)

    def test_title2(self):
        """ Running the program with the --title flag
        should return text in titlecase """

        process = subprocess.Popen(
            ["python", "./echo.py", "--title", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = 'Hello'

        self.assertEquals(stdout.strip('\n'), expected)

    def test_order1(self):
        """ Running the program with multiple flags
        should return text transformed in the order listed
        in USAGE """

        process = subprocess.Popen(
            ['python', './echo.py', '-tul', 'hello!'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = 'Hello!'

        self.assertEquals(stdout.strip('\n'), expected)

    def test_order2(self):
        """ Running the program with multiple flags
        should return text transformed in the order listed
        in USAGE """

        process = subprocess.Popen(
            ['python', './echo.py', '-ul', 'hello!'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = 'hello!'

        self.assertEquals(stdout.strip('\n'), expected)

    def test_no_flags(self):
        """ Running the program with no flags
        returns the text unscathed """

        process = subprocess.Popen(
            ['python', './echo.py', 'obama llama'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        expected = 'obama llama'

        self.assertEquals(stdout.strip('\n'), expected)


if __name__ == '__main__':
    unittest.main()
