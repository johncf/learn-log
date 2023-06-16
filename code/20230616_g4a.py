# requirements: gpt4all

import readline  # for better input() UX

from gpt4all import GPT4All
from gpt4all.pyllmodel import LLModelPromptContext

# see https://docs.gpt4all.io/gpt4all_python.html

gpt = GPT4All("ggml-mpt-7b-chat")  # ("ggml-gpt4all-j-v1.3-groovy")  # ("ggml-v3-13b-hermes-q5_1")
gpt.model.context = LLModelPromptContext(
    logits_size=0,
    tokens_size=0,
    n_past=0,
    n_ctx=1024,
    n_predict=4096,
    top_k=40,
    top_p=0.9,
    temp=0.1,
    n_batch=8,
    repeat_penalty=1.1,
    repeat_last_n=64,
    context_erase=0.5,
)

intro_prompt = "This is a conversation between a human and their assistant."
#intro_prompt = "These are snippets of English text followed by its translation in German."
human_prefix = "## Human:"
#human_prefix = "## English:"
assist_prefix = "## Assistant:"
#assist_prefix = "## Translation in German:"
print("Intro prompt:", intro_prompt)
lines = []

try:
    while True:
        if not lines:
            print(human_prefix)
        line = input('> ' if not lines else '. ')
        if line == "":  # empty line ends the human prompt
            prompt = human_prefix + '\n' + ''.join(lines) + assist_prefix + '\n'
            lines.clear()
            if intro_prompt:
                prompt = intro_prompt + '\n' + prompt
                intro_prompt = None
            print(assist_prefix)
            gpt.generate(prompt)
        else:
            lines.append(line + '\n')
except EOFError:
    pass
