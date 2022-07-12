import pandas as pd
import numpy as np
import torch
from transformers import AutoModel, AutoTokenizer
import random
from scipy.spatial.distance import cdist
import nltk
nltk.download('nps_chat')
nltk.download('punkt')

data = "./fashion_dataset_embeddings.pkl"
df = pd.read_pickle(data)
# Use pretrained simCSE model
tokenizer = AutoTokenizer.from_pretrained("princeton-nlp/sup-simcse-roberta-large")
model = AutoModel.from_pretrained("princeton-nlp/sup-simcse-roberta-large")


def get_input(txt):
    res_list = txt.split(';')
    res_list = [x.strip() for x in res_list]
    intention = res_list.pop()
    return res_list, intention


def embed(list_input):
    inputs = tokenizer(list_input, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        embeddings = model(**inputs, output_hidden_states=True, return_dict=True).pooler_output
    return embeddings


def fashion_advisor(txt):
    items, intention = get_input(txt)
    query_embed = embed(items)
    rows = []
    embeddings = df['embeddings']
    for i in range(len(embeddings)):
        sim = 1 - cdist(query_embed, embeddings[i], 'cosine')
        sim_check = np.any((sim > 0.65), axis=1)
        if sim_check.all():
            rows.append(i)
    # There are two scenarios depending on user intent
    # First
    if intention == 'advice':
        # Empirically derived coefficient for obtaining ranks
        helper_coef = len(embeddings) / 33 / (len(items) / 2)
        occur = len(rows)
        if occur >= helper_coef:
            return 'Top-ranked 5 star combination!'
        elif helper_coef*0.5 < occur < helper_coef:
            return '4 star combination.'
        elif helper_coef*0.1 < occur <= helper_coef*0.5:
            return '3 star combination.'
        elif helper_coef*0.05 < occur <= helper_coef*0.1:
            return '2 star combination.'
        else:
            return '1 star combination.'

    # Second
    elif intention == 'match':
        upd_df = df['labels_with_attributes'].iloc[rows].apply('; '.join)
        res = pd.Series(' '.join(upd_df).split(';')).value_counts()
        fin_res = res[res > 2]  # remove single occurrences
        n_items = len(items)
        fin_res = fin_res[n_items:]  # remove items that match the items the user provided
        rating = int(len(fin_res)/3)
        if rating < 5:
            return 'There is nothing to add to these items. Please try something different.'
        num_top = random.sample(range(0, rating), 5)
        num_medium = random.sample(range(rating, rating*2), 5)
        num_low = random.sample(range(rating*2, rating*3), 5)
        res_div = fin_res.reset_index().rename(columns={'index': 'occurrences', 0: 'count'})
        top_ranked = res_div['occurrences'].iloc[num_top].to_list()
        mainstream = res_div['occurrences'].iloc[num_medium].to_list()
        unpopular = res_div['occurrences'].iloc[num_low].to_list()
        return f"Fashion adviser suggests the following options: 1. Top ranked items: {';'.join(top_ranked)}; " \
               f"2. Mainstream items: {';'.join(mainstream)}; 3. Unpopular items: {';'.join(unpopular)}"
    else:
        return 'Please type /help for instructions. Please follow the instructions when submitting a request.'
