from openai import OpenAI

openai = OpenAI(
    api_key = ('API KEY HERE')

conversation = []

def get_gpt_response(user_input):
    message = {
        "role": "user",
        "content": user_input
    }
    conversation.append(message)

    response = openai.chat.completions.create(
        messages = conversation,
        model = "gpt-3.5-turbo"
    )

    conversation.append(response.choices[0].message)

    return response.choices[0].message.content

def chat():
    while True:
        user_input = input("You: ")
        if user_input in ["exit", "bye", "goodbye"]:
            print("Chatbot: Goodbye!")
            break
        response = get_gpt_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat()