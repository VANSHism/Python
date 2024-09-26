import re
import long_responses as long

def message_probability(user_msg, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts number of words that are present in pre-defined messages
    for word in user_msg:
        if word in recognised_words:
            message_certainty += 1

    # Percentage of recognised words in the user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that required words are in the user message 
    for word in required_words:
        if word not in user_msg:
            has_required_words = False
            break

    # Must have either the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage*100)
    else: 
        return 0 


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation/adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    
    # Responses ----------
    response('Namaste! How may I help you?' , ['hello', 'hi', 'hey', 'sup', 'namaste', 'ram ram'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Dhanyawaad! You\'re welcome', ['thank', 'thanks'], single_response=True)
    response('Dhanyawaad!', ['i', 'love', 'you'], required_words=['love', 'you'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)
    #print(f'Best Match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_msg = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_msg)
    return response

# The response system
while True:
    user_inp = get_response(input('You: '))
    print('Bot: ' + user_inp)
    if user_inp.lower() in ['quit', 'exit', 'stop']:
        break