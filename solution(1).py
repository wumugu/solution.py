from pathlib import Path

CHAINS_FILE = Path("twc12_protein_chains.txt")
CORPUS_FILE = Path("twc12_protein_corpus.txt")


def read_sequences(path):
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


chains = read_sequences(CHAINS_FILE)
corpus = read_sequences(CORPUS_FILE)

for i, chain in enumerate(chains):
    best_errors = float("inf")
    best_number = None

    for j, known_chain in enumerate(corpus):
        if len(chain) != len(known_chain):
            continue

        errors = sum(a != b for a, b in zip(chain, known_chain))

        if errors < best_errors:
            best_errors = errors
            best_number = j

    if best_errors <= 10:
        print(i, best_number)
