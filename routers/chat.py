import difflib
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from core.rule_loader import get_rules
from utils.dynamic_queries import dynamic_query_result

# Request model (must match frontend JSON)
class Message(BaseModel):
    text: str

chat_router = APIRouter()

@chat_router.post("/chat")
def Chat(input:Message,rules=Depends(get_rules)):
    '''
    Please enter your queries. To stop, type 'bye'.
    '''
    #Converting query to lowercase
    query = input.text.lower()

    # Exit condition
    if query == "bye":
        return {"response": "Thank you for chatting with me. See you next time... Bye!"}

    # Exact match
    if query in rules:
        result = dynamic_query_result(query)#Returns an outcome if the query response is dynamic
        if result:
            return result
        return {"response": rules[query]}

    # Partial match
    sim_query = None #To store the query in the rule base that has the highest match with the input query.
    max_prob=0
    for queries, responses in rules.items():
        similarity = difflib.SequenceMatcher(None, query, queries).ratio() 
        if similarity > 0.85:#If similarity between strings are more than 85%, return the response
            if max_prob<similarity:
                max_prob = similarity
                sim_query = queries
    if sim_query:#There is a partially matching query in the rule base
        result = dynamic_query_result(sim_query)#Returns an outcome if the query response is dynamic
        if result:
            return result
        else:
            return {"response": rules[sim_query]}

    # Failure response
    return {"response": "Sorry! I do not have an answer to this question!"}
