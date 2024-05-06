from openai import OpenAI
from PyPDF2 import PdfReader


class PDFAnalyser:

    def __init__(self, PDF_path, api_key, system_prompt, model):
        self.PDF_path = PDF_path
        self._load_pdf(PDF_path)
        self.client = OpenAI(
            api_key=api_key,
        )
        self.system_content = system_prompt
        self.model = model
        

    def _load_pdf(self, PDF_path: str):
        self.PDF = PdfReader(PDF_path)
        pages_raw = [page.extract_text() for page in self.PDF.pages]
        self.pages = pages_raw#[' '.join(page.split('\n')) for page in pages_raw]


    def gpt_parse(self, skip_api_call=False):
        messages = [{"role": "system", "content": self.system_content}]
        messages += [{"role": "user", "content": raw_str} for raw_str in self.pages]

        if not skip_api_call:    
            self.completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                seed=42
            )
            self.parsed_text = self.completion.choices[0].message.content
        else:
            self.parsed_text = 'This is some placeholder text to avoid calling the OpenAI API.'


    def analyse(self):
        self.result = {
            'file': self.PDF_path,
            'model': self.model
        }
        """
        lines_raw = self.parsed_text.split('\n')
        self.lines = [line_ for line_ in lines_raw if len(line_)]  # Remove empty lines
        self.words = []
        for line_ in self.lines:
            self.words += line_.split(' ')
        """
        word_count = int(self.parsed_text.split(' ')[-1])
        #self.result['num_lines'] = len(self.lines)
        self.result['num_words'] = word_count


    def write_result(self, out_path: str):
        if not len(self.result):
            raise ValueError('Result dict is empty, please run self.analyse first.')
        else:
            from datetime import datetime
            from os.path import exists

            self.result['timestamp'] = datetime.now().timestamp()
            keys = self.result.keys()
            mode = 'a' if exists(out_path) else 'w'
            with open(out_path, mode) as f:
                if mode == 'w':
                    f.write(','.join(keys) + '\n')
                f.write(','.join(str(self.result[key]) for key in keys) + '\n')
