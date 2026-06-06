import re

summarizer = None


def get_summarizer():
    global summarizer
    if summarizer is None:
        from transformers import pipeline
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer


def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()



def remove_duplicate_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    unique = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        duplicate = False
        for u in unique:
            if s in u or u in s:
                duplicate = True
                break
        if not duplicate:
            unique.append(s)
    return " ".join(unique)


def remove_repeated_phrases(text):
    words = text.split()
    cleaned = []
    for word in words:
        if len(cleaned) > 6:
            recent = cleaned[-6:]
            if word in recent:
                continue
        cleaned.append(word)
    return " ".join(cleaned)


def chunk_text_by_tokens(text, tokenizer, max_tokens=400, overlap=80):
    tokens = tokenizer.encode(text)
    chunks = []
    start = 0
    while start < len(tokens):
        end = start + max_tokens
        chunk_tokens = tokens[start:end]
        chunk_text = tokenizer.decode(chunk_tokens, skip_special_tokens=True)
        chunks.append(chunk_text)
        start += max_tokens - overlap
    return chunks


def summarize_text(text):
    pipeline_instance = get_summarizer()
    tokenizer = pipeline_instance.tokenizer
    text = clean_text(text)
    chunks = chunk_text_by_tokens(text, tokenizer)
    chunk_summaries = []
    for chunk in chunks:
        chunk_tokens = len(tokenizer.encode(chunk))
        max_len = int(chunk_tokens * 0.6)
        min_len = int(chunk_tokens * 0.3)
        max_len = max(120, min(max_len, 400))
        min_len = max(60, min(min_len, 200))
        result = pipeline_instance(
            chunk,
            max_length=max_len,
            min_length=min_len,
            truncation=True,
            do_sample=False,
            no_repeat_ngram_size=3,
            repetition_penalty=1.2
        )
        chunk_summaries.append(result[0]["summary_text"])

    combined_summary = " ".join(chunk_summaries)
    combined_summary = remove_duplicate_sentences(combined_summary)
    combined_summary = remove_repeated_phrases(combined_summary)

    combined_tokens = len(tokenizer.encode(combined_summary))
    final_max = int(combined_tokens * 0.85)
    final_min = int(combined_tokens * 0.45)
    final_max = max(150, min(final_max, 500))
    final_min = max(80, min(final_min, 250))

    final = pipeline_instance(
        combined_summary,
        max_length=final_max,
        min_length=final_min,
        truncation=True,
        do_sample=False,
        no_repeat_ngram_size=3,
        repetition_penalty=1.2
    )
    return final[0]["summary_text"]