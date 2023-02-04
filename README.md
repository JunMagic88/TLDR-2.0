# TLDR-2.0
New version of TLDR with more optimised code

## Setup
1. Install Python: https://www.python.org/
2. Download chromedriver https://chromedriver.chromium.org/downloads - NOTE: make sure you download the version that matches your Google Chrome version (check in *About Chrome*)
3. Put the chromedriver executable file in a location and add that location to the **PATH** - follow guide [here](https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver) for Windows:  and [here](https://www.swtestacademy.com/install-chrome-driver-on-mac/) for Mac: 
4. Create 3 chatGPT accounts: https://chat.openai.com/chat
5. For each of your chatGPT accounts, log in using Google Chrome and press **F12** to open console in Chrome. Go to Application > Cookies and Copy the session token value in **__Secure-next-auth.session-token** for each account
6. Download or git clone this repository to a local folder of your choice
```python
git clone https://github.com/JunMagic88/TLDR-2.0.git
```
8. Using a text editor, open TLDR.py. Replace XXXXXXX for agent1, agent2 and agent 3 with the session tokens you got from step 5. 
9. Navigate to the TLDR-2.0 folder in **Terminal (Mac)** or **Command Prompt (Windows)** and run: 
```python
pip install -r requirements
```

## Adding texts to summarise
1. Add any **.txt** files in the **/Texts** folder 
2. Add any **.epub** or **.pdf** files in the **/00.EPUBs+PDFs** folder
3. Add any **YouTube links** (can be video or public playlist URLs) to the Youtube

## Let's TLDR!
1. Run this to download the **transcripts** of the YouTube videos to the **/Texts** folder
```python
python get_transcripts.py
```
2. Run this to convert the epub and PDF files into **.txt** and save them in the **/Texts** folder
```python
python parse_to_txt.py
```
3. Run this to start the summarisation. This should start a Chrome window. Do not try to login and allow it to close automatically. The summarised chunks are saved in **/TLDR-2.0** folder. When it runs into an error (e.g. due to rate limit), it will rotate to another agent and log the last text it tried to summarise in **gpt3_log**. Check the content and delete text from your .txt file in **/Texts** up to that point before running TLDR.py again
```python
python TLDR.py
```
## Custom Prompt 
- You can change the prompt to your own by updating the **promp.txt** file.

## Common issues & workarounds
Every week or so, you may need to update your session tokens - follow step 5 in Setup above.
