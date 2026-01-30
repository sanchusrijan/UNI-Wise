from transformers import pipeline
import re
from collections import Counter

# ----------------------------
# Load summarization model
# ----------------------------
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

# ----------------------------
# Chunk text safely by tokens
# ----------------------------
def chunk_text_by_tokens(text, tokenizer, max_tokens=900):
    tokens = tokenizer.encode(text)
    chunks = []

    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        chunk_text = tokenizer.decode(
            chunk_tokens,
            skip_special_tokens=True
        )
        chunks.append(chunk_text)

    return chunks


# ----------------------------
# Adaptive summary length
# ----------------------------
def get_summary_lengths(text, tokenizer):
    token_count = len(tokenizer.encode(text))

    # % based control
    max_len = int(token_count * 0.35)   # ~35%
    min_len = int(token_count * 0.2)    # ~20%

    # Safety bounds for BART
    max_len = min(max_len, 280)
    min_len = max(min_len, 60)

    return min_len, max_len


# ----------------------------
# Importance-based extraction
# (generic, no keywords)
# ----------------------------
def extract_key_sentences(text, max_sentences=5):
    sentences = re.split(r'(?<=[.!?])\s+', text)

    words = re.findall(r'\b\w+\b', text.lower())
    freq = Counter(words)

    sentence_scores = []
    for sentence in sentences:
        score = sum(
            freq[word]
            for word in re.findall(r'\b\w+\b', sentence.lower())
        )
        sentence_scores.append((score, sentence))

    sentence_scores.sort(reverse=True)

    return " ".join(
        sentence for _, sentence in sentence_scores[:max_sentences]
    )


# ----------------------------
# MAIN summarization pipeline
# ----------------------------
def summarize_text(text):
    tokenizer = summarizer.tokenizer

    # Step 1: Chunk input
    chunks = chunk_text_by_tokens(text, tokenizer)

    # Step 2: Abstractive summarization per chunk
    chunk_summaries = []

    for chunk in chunks:
        min_len, max_len = get_summary_lengths(chunk, tokenizer)

        result = summarizer(
            chunk,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )

        chunk_summaries.append(result[0]["summary_text"])

    # Step 3: Combine chunk summaries
    combined_summary = " ".join(chunk_summaries)

    # Step 4: Extractive grounding (generic)
    final_summary = extract_key_sentences(
        combined_summary,
        max_sentences=5
    )

    return final_summary