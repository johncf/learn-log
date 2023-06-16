# requirements: sentencepiece torch transformers

import readline  # for better input() UX

from transformers import T5Tokenizer, T5ForConditionalGeneration, GenerationConfig

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")
config = GenerationConfig(max_new_tokens=100)

while True:
    try:
        line = input("> ")
    except EOFError:
        break
    input_ids = tokenizer(line + "\n", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, generation_config=config)
    print(tokenizer.decode(outputs[0]))
