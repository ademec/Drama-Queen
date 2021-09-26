from transformers import GPT2Tokenizer, GPT2LMHeadModel
import sys
import random

# Load pretrained model and tokenizer
model = GPT2LMHeadModel.from_pretrained("asi/gpt-fr-cased-base")
tokenizer = GPT2Tokenizer.from_pretrained("asi/gpt-fr-cased-base")

# Generate a sample of text
model.eval()



with open('./sortie_python_2.txt','r',encoding="UTF8") as fh:
    content = fh.read()
content= content[1:-2]
titles = content.split('","')


titles=[title.replace('"', '') for title in titles][7:]
batches = []
for i in range(10):
    batches.append("$".join(random.sample(titles,10)))



input_sentence = batches[0]

for n,pho in enumerate(input_sentence.split("$")):
    print(n,pho)

input_ids = tokenizer.encode(input_sentence, return_tensors='pt')


beam_outputs = model.generate(
    input_ids,
    max_length=500,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    num_return_sequences=1
)


with open('filename.txt', 'a') as f:
    sys.stdout = f # Change the standard output to the file we created.

    print("Output:\n" + 500 * '-')
    output_list = tokenizer.decode(beam_outputs[0], skip_special_tokens=True).split("$")
    for pho in output_list[10:]:
        print(pho)
    print("\n\n")



