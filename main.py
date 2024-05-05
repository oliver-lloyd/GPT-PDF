from PyPDF2 import PdfReader
from dotenv import dotenv_values
from openai import OpenAI
from argparse import ArgumentParser
from funcs import gpt_parse, analyse

parser = ArgumentParser()
parser.add_argument('PDF_path')
args = parser.parse_args()

# Read in file
reader = PdfReader(args.PDF_path)
pages_raw = [page.extract_text() for page in reader.pages]
pages = [' '.join(page.split('\n')) for page in pages_raw]

# Set up OpenAI client
api_key = dotenv_values()['OPENAI_KEY']
client = OpenAI(
    api_key=api_key,
)

# Parse the text
completion = gpt_parse(pages, client)
parsed = completion.choices[0].message.content

# Analyse text
out = analyse(parsed)
print(out)
quit()
