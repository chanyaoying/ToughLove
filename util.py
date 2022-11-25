import nltk
nltk.download('punkt')

def pronoun_substitution(user_input):
    """
    replaces pronouns in the user input with pronouns that are more appropriate for the chatbot
    """
    word_list = nltk.word_tokenize(user_input.lower())
    substitution = {'i': 'you', 'am': 'are', 'my': 'your'}  # can add more words here
    new_word_list = []
    for word in word_list:
        if word in substitution:
            new_word_list.append(substitution[word])
        else:
            new_word_list.append(word)

    return ' '.join(new_word_list)


def process_output(output):
    """
    processes the output from the insult bot
    """
    output = output.strip()
    output = output[0].upper() + output[1:]
    return output