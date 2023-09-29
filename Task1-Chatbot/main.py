"""/** Author: Rawan Khaled   https://github.com/RawanKhaled20/Codsoft-AI.git """

# Define a function to get the chatbot's response
def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define some predefined rules and responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm just a computer program, but thanks for asking!"

    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    elif "help" in user_input:
        return "I can assist with basic inquiries. Try asking me something."

    elif "what is your name" in user_input:
        return "I'm a simple chatbot."

    elif "what can you do" in user_input:
        return "I can answer basic questions and engage in simple conversations."

    elif "tell me a joke" in user_input:
        return "Why did the computer keep freezing? Because it left its Windows open!"

    elif "who created you" in user_input:
        return "I was created by a developer called Rawan."

    elif "what's the weather like today" in user_input:
        return "I'm sorry, I can't provide real-time information. Please check a weather website or app."

    elif "how old are you" in user_input:
        return "I don't have an age as I'm just a computer program."

    elif "where are you from" in user_input:
        return "I exist in the digital world, so I don't have a physical location."

    elif "what is your favourite color" in user_input:
        return "I am a computer model so i don't have a favourite color.'"

    else:
        return "I'm not sure how to respond to that. Please ask another question."

def main():
    print("Chatbot: Hi there! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = simple_chatbot(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()







