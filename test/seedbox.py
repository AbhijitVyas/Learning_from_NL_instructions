import transformers
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "seedboxai/Llama-3-KafkaLM-8B-v0.1"

model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16)
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)

pipeline = transformers.pipeline(
    model=model, tokenizer=tokenizer,
    return_full_text=True,
    task='text-generation',
    device="cuda",
)

messages = [
    {"role": "system", "content": "Du bist ein hilfreicher KI-Assistent."},
    {"role": "user", "content": "Wer ist eigentlich dieser Kafka?"},
]

prompt = pipeline.tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = pipeline(
    prompt,
    max_new_tokens=1200,
    num_beams=5,
    num_return_sequences=1,
    early_stopping=True,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.4,
    top_p=0.9,
)

print(outputs[0]["generated_text"][len(prompt):])
