## Overview
This project creates SimChat, a simple rule based chatbot.
## Tech Stack
Frontend: HTML,CSS,JavaScript<br>
Backend: Python, FastAPI<br>
Rule base: JSON file - where each key -> query and each value -> corresponding response
## Algorithm
1. User asks a query to the chatbot
2. If the input query exactly matches a query present in the rule base, the corresponding response is send.
3. If there is a 85% partially matching query in the rule base, the corresponding response is send
4. If no matching queries are present, the response "Sorry! I do not have an answer to this question!" is send
5. If "bye" is typed, the response "Thank you for chatting with me. See you next time... Bye!" is displayed and the HTML page is refreshed after 2 seconds
## Result
To run the code, start the uvicorn server and double click index.html file
<img width="1920" height="903" alt="Screenshot" src="https://github.com/user-attachments/assets/e2d677df-1351-4f31-80b6-e56612385ec7" />



