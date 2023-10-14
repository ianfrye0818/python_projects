#Import OpenAI Library
import openai
import apikey

#Set OpenAi API Key
openai.api_key = apikey.API_KEY


#Function for making API call
def chatWithGPT(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}])

    return response.choices[0].message.content.strip()

#Execute this file as the main python file
if __name__ == "__main__":
    while True:
        #Continue the conversation as long as they user does not input one of the words below:
        userInput = input("You: ")
        if userInput.lower() in ["quit", "exit", "bye"]:
            break
        
        #Call chat function with the user's input
        response = chatWithGPT(userInput)

        #Print the Chatbot's response to console
        print("Chatbot: ", response)