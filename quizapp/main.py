#!/usr/bin/env python
"""
Usage:
    main.py allquizzes <allquizzes>
    main.py localquizzes <localquizzes>
    main.py importquiz <importquiz>
    main.py takequiz <takequiz>
    main.py (-i | --interactive)
    main.py (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit


def docopt_cmd(func):
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to QuizzApp'
    prompt = '(quiz)> '
    file = None

 
    @docopt_cmd
    def do_allquizzes(self, *args):
        """Usage: allquizzes <allquizzes>"""
        print app.all_quizzes()

    @docopt_cmd
    
    def do_localquizzes(self, *args):

        print app.local_quizzes()

    @docopt_cmd
    
    def do_importquiz(self, quiz):
        print app.import_quizzes (quiz)

    @docopt_cmd
    
    def do_takequiz(self, quiz):
        print app.take_quiz(quiz)



    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
