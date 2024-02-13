import json
from difflib import get_close_matches


#load knowledge to bot 
def load_knowledge_base (file_path: str)  -> dict:
    with  open (file_path, 'r') as file:
        data: dict=json.load(file)
    return data


#save response function
def save_knowldge_base(file_path:str,data:dict):
    with open(file_path,'n' ) as file:
        json.dump (data, file, indent =2)
        
 #find best match to questions       
 
def find_best_match (user_question:str,question:list[str])-> str | None:
    matches:list=get_close_matches(user_question,question,1,0.6 )
    return matches[0] if matches else None 

def get_answer_for_questions (question:str, knowledge_base:dict )-> str | None :
    for q in knowledge_base["questions"]:
        if q ["question"]==question:
            return q ["answer"]
def chat_bot():
    knowledge_base:dict= load_knowledge_base ("knowledge_base.json")
    
    while True:
        user_input:str= input ('You:')
        
        if user_input.lower()=="quit":
            break
        best_match: str|None= find_best_match(user_input, [q['question'] for q in knowledge_base['question']])
         
        if best_match:
            answer: str= get_answer_for_questions    (best_match, knowledge_base)
            print (f'Bot: {answer}')
        else:
            print ('Bot: I dont know the answer, can you teach me?')
            new_answer:str= input ("You:Type the answer or skip to skip")
            
            if new_answer.lower () != "skip":
                knowledge_base["question"].append ({"question": user_input, "answer":new_answer})
                save_knowldge_base('knowledge_base.json', knowledge_base)
                print ('Bot: Thank You For Teaching Me ')
                
if __name__ =="__main__":
    chat_bot()
       