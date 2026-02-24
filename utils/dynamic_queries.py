from datetime import date
from datetime import datetime
#This function finds response to dynamic queries
def dynamic_query_result(query):
    if query == "what day is today?":
        today = date.today()
        day_name = today.strftime("%A")
        return {"response": f"Today is {day_name}"}

    if query == "what is today's date?":
        today = date.today()
        return {"response": f"Today's date is {today}"}

    if query == "what time is it now?":
        formatted_now = datetime.now().strftime("%H:%M:%S")
        return {"response": f"Now the time is {formatted_now}"}
    
    return None
