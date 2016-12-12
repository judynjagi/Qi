import cmd
import sys
import cmd
import warnings

import app


class TestYourKnowledgeApp(cmd.Cmd):

    def do_seperate(self,  *args):
        print "*************************************************************"
        print "------------T E S T Y O U R K N O W L E D G E ---------------"
        print "*************************************************************"

    def do_line(self,  *args):
        print "*************************************************************"

    def do_allquizzes(self, *args):
    	print app.all_quizzes()

    def do_localquizzes(self, *args):
    	print app.local_quizzes()

    def do_importquiz(self, quiz):
    	for item in app.import_quizzes (quiz):
            print item

    def do_takequiz(self, quizie):
    	
    	for item in app.take_quiz(quizie):
    		print item

    def default(self, arg):
        pass

    def do_EOF(self, line):
        return True
  
if __name__ == '__main__':
    TestYourKnowledgeApp().cmdloop()
  
