from openai import OpenAI


def gpt_parse(raw: list, client: OpenAI, model: str):
    system_content = 'You are an assistant that helps correctly parse strings. The strings are misformatted, with some spaces added randomly and others missing. You will accept one or more string(s) as input, correct these errors in the string(s), and return the result.'
    messages = [{"role": "system", "content": system_content}]
    messages += [{"role": "user", "content": raw_str} for raw_str in raw]

    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        seed=42
    )
    return completion


def analyse(content: str):
    lines = content.split('\n')
    lines = [line_ for line_ in lines if len(line_)]
    words = []
    for line_ in lines:
        words += line_.split(' ')
    result = {
        'num_lines': len(lines),
        'num_words': len(words)
    }
    return result


def write_result(result: dict, out_path: str):
    from datetime import datetime
    from os.path import exists

    result['timestamp'] = datetime.now().timestamp()
    mode = 'a' if exists(out_path) else 'w'
    keys = result.keys()
    with open(out_path, mode) as f:
        if mode == 'w':
            f.write(','.join(keys) + '\n')
        f.write(','.join(str(result[key]) for key in keys) + '\n')

