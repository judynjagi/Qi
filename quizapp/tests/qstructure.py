class Qstructure():
	def __init__(self, question, ans_options, answer):
		self.question =question
		self.ans_options=ans_options
		self.answer=answer

	def __repr__(self): 
		
		return "A: {}".format(self.answer)


	def correct_answer(self, users_answer): 
		'''checks if the users answer is correct or not'''
		self.users_answer=users_answer
		users_answer = ['a', 'b', 'c', 'd']
		if self.users_answer.lower() not in users_answer:
		
			return "Your answer is incorrect, try again"  '''if incorrect, it returns a try again message'''
	
		'''if correct, it returns upper cases '''
	
		return self.answer.upper()==self.users_answer.upper()
		

	def display_questions_and_choices(self):
		''' When a user gives an answer, the output should be in this format'''
		question_answer = self.question + '\n'
		for index, letter in enumerate(self.ans_options):
			question_answer += letter.strip().upper() + ').' + ' ' + self.ans_options[letter] + '\n'
		return question_answer

		 



		

        
