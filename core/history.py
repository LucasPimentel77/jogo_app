import pygame

class History:
    def __init__(self, module, level):
        self.module = module
        self.questions = []
        self.qtd_questions = 0
        self.level = level
        self.hits = None
        self.xp = None

    def add_question(self, question):
        self.questions.append(question)
        self.qtd_questions += 1
        

    