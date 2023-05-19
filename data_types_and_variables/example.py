def analyze_text(text):
    char_count = len(text)

    word_count = len(text.split())

    sentence_count = text.count('.') + text.count('!') + text.count('?')

    # calculate average word length
    words = text.split()
    total_word_length = sum(len(word) for word in words)
    average_word_length = total_word_length / word_count

    # Display info
    print('Text analysis:')
    print('Number of characters:', char_count)
    print('Number of word:', word_count)
    print('Number of sentences:', sentence_count)
    print('Average word length:', average_word_length)


while True:
    user_choice = input('Enter \'E\' to exit or \'A\' to analyze text: ')

    if user_choice.upper() == 'E':
        print('Exiting the program...')
        break

    elif user_choice.upper() == 'A':
        user_text = input('Enter some text: ')
        analyze_text(user_text)

    else:
        print('Invalid choice. Please try again!')