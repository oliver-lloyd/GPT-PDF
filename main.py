from PyPDF2 import PdfReader
from dotenv import dotenv_values
from openai import OpenAI
from argparse import ArgumentParser
from funcs import gpt_parse, analyse, write_result

parser = ArgumentParser()
parser.add_argument('PDF_path')
parser.add_argument('--result_path', '-r')
parser.add_argument('--model', '-m', default='gpt-4')
args = parser.parse_args()

# Read in file
print('Loading PDF..')
reader = PdfReader(args.PDF_path)
pages_raw = [page.extract_text() for page in reader.pages]
pages = [' '.join(page.split('\n')) for page in pages_raw]

# Set up OpenAI client
api_key = dotenv_values()['OPENAI_KEY']
client = OpenAI(
    api_key=api_key,
)

# Parse the text
print('Parsing with ChatGPT. This may take a few seconds..')
completion = gpt_parse(pages, client, args.model)
parsed = completion.choices[0].message.content

# Analyse
print('Analysing text..')
out = analyse(parsed)

# Save results or print to console
print('Saving..')
out['file_path'] = args.PDF_path
out['model'] = args.model
if args.result_path:
    write_result(out, args.result_path)
else:
    print(out)
