

import xml.etree.ElementTree as ET  
                                    

def load_questions(filename):
   
    questions = []
    tree = ET.parse(filename)      
    root = tree.getroot()           
    for question in root.findall('question'): 
        question_text = question.find('text').text  
        options = [option.text for option in question.find('options').findall('option')]  
        correct_answer = question.find('correct').text  
        questions.append((question_text, options, correct_answer))  
    return questions 
def run_quiz(questions):

    score = 0  
    for i, (question, options, correct_answer) in enumerate(questions, 1): 
        print(f"\nQuestion {i}: {question}")  
        for j, option in enumerate(options, 1): 
         print(f"{j}. {option}") 
        user_answer = input("Your answer: ").strip().lower()  
        if user_answer == correct_answer.lower():  
            print("Correct!")  
            score += 1  
        else:
            print(f"Wrong! The right enswer is: {correct_answer}") 
    print(f"\nYou got {score} out of {len(questions)} questions correct.")  

if __name__ == "__main__":
    questions = load_questions("quizz.xml")  
    run_quiz(questions)  
