from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

from pytorch_transformers import BertTokenizer, BertForMaskedLM
import random
import torch

from transformers import BartForConditionalGeneration, BartTokenizer
import gpt_2_simple as gpt2

app = Flask(__name__)
CORS(app)
port = 5003


bert = "./Models/finetuned_bert"
bertModel = BertForMaskedLM.from_pretrained(bert, output_attentions=False)
bertTokenizer = BertTokenizer.from_pretrained(bert)

bart = "./Models/finetuned_bart"
bartModel = BartForConditionalGeneration.from_pretrained(bart, forced_bos_token_id=0)
bartTokenizer = BartTokenizer.from_pretrained(bart)



############ This is for BERT ###################################
def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

def predict_bert(input, length = 10):
    filler = ' '.join(['MASK' for _ in range(int(length))])
    if len(input.strip())==0:
        sentence = "[CLS] " + filler + " . [SEP]"
    else:
        sentence = "[CLS] " + " " + input + " " + filler + " . [SEP]"
    tokenized_text = bertTokenizer.tokenize(sentence)
    idxs = duplicates(tokenized_text, 'mask')
    for masked_index in idxs:
        tokenized_text[masked_index] = "[MASK]"
    generated = 0
    full_sentence = []
    while generated<int(length):
        mask_idxs = duplicates(tokenized_text, "[MASK]")
        focus_mask_idx = random.choice(mask_idxs)

        mask_idxs.pop(mask_idxs.index(focus_mask_idx))
        temp_tokenized_text = tokenized_text.copy()
        temp_tokenized_text = [j for i, j in enumerate(temp_tokenized_text) if i not in mask_idxs]
        temp_indexed_tokens = bertTokenizer.convert_tokens_to_ids(temp_tokenized_text)
        ff = [idx for idx, i in enumerate(temp_indexed_tokens) if i==103]
        temp_segments_ids = [0]*len(temp_tokenized_text)
        tokens_tensor = torch.tensor([temp_indexed_tokens])
        segments_tensors = torch.tensor([temp_segments_ids])

        with torch.no_grad():
            outputs = bertModel(tokens_tensor, token_type_ids=segments_tensors)
            predictions = outputs[0]

        k = 5
        predicted_index = random.choice(predictions[0, ff].argsort()[0][-k:]).item()
        predicted_token = bertTokenizer.convert_ids_to_tokens([predicted_index])[0]
        tokenized_text[focus_mask_idx] = predicted_token
        generated += 1
        output = ' '.join(tokenized_text[1:-1])
    return output.capitalize()
    
########################## This is for BART ################################
def predict_bart(prefix):
    input = prefix + " <mask>"
    min = len(prefix) + 5
    batch = bartTokenizer(input, return_tensors="pt")
    generated_ids = bartModel.generate(batch["input_ids"], min_length = min, max_length = min + 10, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
    output = bartTokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return output[0]

######################### This is for GPT- 2 ####################################
def predict_gpt2(prefix):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')
    output = gpt2.generate(sess, prefix= prefix, length=15, include_prefix=False, nsamples= 3,
              truncate='\n', return_as_list=True)

    for prediction in output:
        if prediction.upper().isupper():
            return prefix + " " + prediction
    return prefix + " " + output[0]
    
@app.route("/")
def index():
    return "Insult API is running."

# @app.route("/get-insult", methods = ["POST"])
@app.route("/get-insult", methods = ["POST"])
def get_insult():
    
    prefix = request.json.get('text')

    if len(prefix.strip())==0:
        prefix = "You "

    if prefix[-1] in ['.', '!', '?']:
        prefix = prefix + ", "

    bert_response = predict_bert(prefix,10)
    bart_response = predict_bart(prefix)
    gpt2_response = predict_gpt2(prefix)

    response_data = [
                        {
                            "model": "gpt-2",
                            "insult": gpt2_response
                        },
                        {
                            "model": "bert",
                            "insult": bert_response
                        },
                        {
                            "model": "bart",
                            "insult": bart_response
                        }
                    ]

    return jsonify(response_data)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
