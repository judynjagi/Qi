class Qstructure():
	def __init__(self, questions, ans_options, is_answers):
		self.questions=questions
		self.ans_options=ans_options
		self.is_answers=is_answers

	def __str__(self):
		return str(self.is_answers) 

	def correct_answer(self, users_answer): 
		'''checks if the users answer is correct or not'''
		self.users_answer=users_answer
		users_answer=''
		if len(users_answer)==0:
			return "Your answer is incorrect, try again"  '''if incorrect, it returns a try again message'''
	
		'''if correct, it can take both lower and upper cases '''
		
		return self.is_answer.upper()==users_answer.upper()
		return self.is_answer.lower()==users_answer.lower() 

	def display_questions_and_choices(self):
		''' When a user gives an answer, the output should be in this format'''
		question_answer = self.questions + '\n'
		for index, letter in enumerate(self.options):
			if type[letter]==str:
				question_answer= question_answer + '\n' + letter.strip().upper() 
				'''return the question and letter in capital letters'''
				self.ans_options[letter] 
		return question_answer
		


		

        