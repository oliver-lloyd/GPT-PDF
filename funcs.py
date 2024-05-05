from openai import OpenAI

def gpt_parse(raw: list, client: OpenAI):
    system_content = 'You are an assistant that helps correctly parse strings. The strings are misformatted, with some spaces added randomly and others missing. You will accept one or more string(s) as input, correct these errors in the string(s), and return the result.'
    messages = [{"role": "system", "content": system_content}]
    messages += [{"role": "user", "content": raw_str} for raw_str in raw]

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion


def analyse(content: str):
    lines = content.split('\n')
    lines = [line_ for line_ in lines if len(line_)]
    words = []
    for line_ in lines:
        words += line_.split(' ')
    return f'Line count: {len(lines)}. Word count: {len(words)}'
