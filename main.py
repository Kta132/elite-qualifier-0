import random

# When the user respond, chatbot will randomly choose one of the following as a response.

def speech_response(user_input):
  responses = [
    "That's good.",
    "Oh, what activities did you do?",
    "Great!",
    "Is that so."
  ]
  return random.choice(responses)
#####

#Default state
def init_chat():
  quit_chat = 'Q'

  
  # The chatbot will ask you a question v.

  user_input = input("Hi, how is your day?\n")

#If the input is not equal to quit_chat
  while user_input != quit_chat:
    #Then user_input would input a speech_response in a new line.
    user_input = input(speech_response(user_input) + "\n")
######


#Activity response
def activity_response(user_input):
  responses = [
    "That sounds so nice! Is there anything else that you did?",
    "Wow! I wish I was there.",
    "Did you have fun?"
  ]
  return random.choice(responses)

  #If the response is "Oh, what activities did you do?"
  
  #The user then answered.
  
  #In response, the chatbot will say something.
breakpoint


if __name__ == "__main__":
  init_chat()


