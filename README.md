# PDF word counter using Chat GPT

A Python program to parse the text inside of a PDF file using the OpenAI API, returning the word count.

## Requirements
Python libraries:
- PyPDF2
- dotenv
- OpenAI

An OpenAI API key needs to be placed in a '.env' file like so: 

`OPENAI_KEY='sk-proj-my_api_key'`

## Usage
To analyse 'example.pdf' and print result dictionary to console:
`python main.py example.pdf`

To analyse 'example.pdf' and save results to 'results.csv', run:
`python main.py example.pdf -r results.csv`

To analyse 'example.pdf' using GPT-3.5-turbo (defaults to GPT-4), run:
`python main.py example.pdf -m gpt-3.5-turbo`
