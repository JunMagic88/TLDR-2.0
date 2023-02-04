from time import time, sleep
import textwrap
import os
import re
from revChatGPT.ChatGPT import Chatbot
import requests

# open the file at the given filepath and return its content
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# save the given content to the specified filepath
def save_file(content, filepath):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def start_gpt(token):
    return Chatbot({
        "session_token":token
    }, conversation_id=None, parent_id=None) 
    
# function to generate a summary of the input text using the GPT-3 model
def gpt3_completion(prompt, filename, count):

    while True:
        try:
            # send the prompt to the chatGPT to generate a summary
            response = chatbot.ask(prompt, conversation_id=None, parent_id=None)
            text = response['message'].strip()
            text = re.sub('\s+', ' ', text)
            
            #

            # save the prompt and the generated summary to a log file
            #
            return text
        except Exception as oops:
            print('Error communicating with chatGPT:', oops)
            complete_err_filename = f'{filename}_{count}_gpt3.txt'
            with open('gpt3_logs/%s' % complete_err_filename, 'w') as outfile:
                outfile.write('PROMPT:\n\n' + prompt)
            outfile.close()
            return "Error, trying again in 1 minute..." 
            

if __name__ == '__main__':
    # chatGPT accounts
    agent1 = 'xxxxxxxx'
    
    agent2='xxxxxxxx'
   
    agent3 = 'xxxxxxxx'
    
    temp = ''

    input_directory = 'Texts'

    # start first instance of chatGPT
    chatbot = start_gpt(agent1)

    for filename in os.listdir(input_directory):
        filepath = os.path.join(input_directory, filename)
        text = open_file(filepath)
        chunks = textwrap.wrap(text, 2000)
        count = 0
        
        # iterate over the chunks
        for chunk in chunks:
            count = count + 1

            # read the prompt template and replace the placeholder with the current chunk
            prompt = open_file('prompt.txt').replace('<<SUMMARY>>', chunk)
            prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()

            # generate the summary of the chunk using GPT-3
            import time

            while True:
                try:
                    if (count % 2 == 0):
                        chatbot.clear_conversations()
                        chatbot.reset_chat()
                        time.sleep(5)
                    summary = gpt3_completion(prompt,filename,count)
                    if "Error" not in summary:
                        break
                    # if error, change to 2nd and 3rd agent
                    temp = agent1
                    agent1 = agent2
                    agent2 = agent3
                    agent3 = temp
                    print('trying again..')
                    chatbot = start_gpt(agent1)
                except Exception as err:
                    print("Error:", err)
                    errfilename = f'{filename}_{count}.txt'
                    with open('gpt3_logs/%s' % errfilename, 'w') as errfile:
                        errfile.write('PROMPT:\n\n' + prompt)
                    errfile.close()
                    print("Waiting for 1 minute before trying again...")
                    time.sleep(60)
                    continue

            print('\n\n\n', count, 'of', len(chunks), ' - ', summary)

            # append to the end of the summary file
            with open(filename+'.txt', 'a', encoding='utf-8') as f:
                f.write(summary + '\n\n')
            f.close()