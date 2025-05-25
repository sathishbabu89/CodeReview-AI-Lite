from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import subprocess

# Load light-weight model
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-small")

def run_static_analysis(code_str):
    with open("temp.py", "w") as f:
        f.write(code_str)
    result = subprocess.run(["pylint", "temp.py", "--disable=all", "--enable=C,R,E,W"], 
                            capture_output=True, text=True)
    return result.stdout

def llm_suggestion(code_str):
    prompt = f"Suggest improvements for this code:\n{code_str}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=128)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
