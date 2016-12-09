import cmd
import sys
import cmd
import warnings

import app


class TestYourKnowledgeApp(cmd.Cmd):
    def do_allquizzes(self, *args):
    	print app.all_quizzes()

    def do_localquizzes(self, *args):
    	print app.local_quizzes()

    def do_importquiz(self, quiz):
    	print app.import_quizzes (quiz)

    def do_takequiz(self, quizie):
    	print app.take_quiz(quizie)
  
if __name__ == '__main__':
    TestYourKnowledgeApp().cmdloop()
  
