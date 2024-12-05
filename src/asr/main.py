# The file contains the Huggingface interface for using openAI's Whisper transformer model
# to test it for ASR functionality.
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import Audio, load_dataset


device = "cuda:0" if torch.cuda.is_available() else "cpu"
print("device", device)
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3-turbo"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
)


generate_kwargs = {
    "temperature": (0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
    "return_timestamps": True,
    "language": "english"
}


result = pipe("Pour_2.mp3", generate_kwargs=generate_kwargs)

print(result["text"])


#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
