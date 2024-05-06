from dotenv import dotenv_values
from argparse import ArgumentParser

from PDFAnalyser import PDFAnalyser


# Get user args
parser = ArgumentParser()
parser.add_argument('PDF_path')
parser.add_argument('--result_path', '-r')
parser.add_argument('--model', '-m', default='gpt-4')
args = parser.parse_args()

env = dotenv_values()

# Construct the PDF parser
with open('system_prompt.txt', 'r') as f:
    sys_prompt = f.read()

pdfa = PDFAnalyser(
    args.PDF_path,
    env['OPENAI_KEY'],
    sys_prompt,
    args.model
)

# Parse the text
print('Sending data to ChatGPT. This may take a few seconds..')
pdfa.gpt_parse()

# Analyse
print('Analysing text..')
pdfa.analyse()

# Save results or print to console
print('Saving..')
if args.result_path:
    pdfa.write_result(args.result_path)
else:
    print(pdfa.result)
