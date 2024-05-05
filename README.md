# PDF word counter using Chat GPT

A Python program to parse the text inside of a PDF file, returning some relevant statistics. Current functionality is very basic (prog simply returns line and word counts of the file) but more will be added soon.

## Requirements
Python libraries:
- PyPDF2
- dotenv
- OpenAI

An OpenAI API key needs to be placed in a '.env' file like so: 

`OPENAI_KEY='sk-proj-my_api_key'`

## Usage:
`python main.py test.pdf`