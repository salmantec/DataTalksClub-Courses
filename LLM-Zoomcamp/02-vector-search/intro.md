In previous sessions, we used minsearch / sqlitesearch

- It mathces exact words
- If you search `Docker`, the document has to contain `Docker` to comeback

But look at these two questions:

1. "Can I still join the course after the start date?"
2. "Is it possible to enroll late?"

They mean the same thing, yet they share almost no words. A keyword engine struggles to match them. We need something that works on meaning, not on the exact worlds

That something is _**`Vector search`**_ - Instead of matching words, it maches ideas

## The vector search process

We run vector search in two stages:

1. Offline (Indexing): we convert all documents into vectors (arrays of numbers) and store them in an index
2. Online (Querying): We convert the user's query into a vector with the same model, then find the closest document vectors by similarity

An embedding model produces these vectors. It's a neural network trained to capture meaning, so texts that mean similar things land on similar vectors.
We measure how close two vectors are with a distance metric - The most common one is cosine similarity

Cosine similarity measures the angle between two vectors:

- Vectors pointing in the same direction: similarity close to 1 (Similar)
- Vectors at right angles: similarity close to 0 (unrelated)
- Vectors pointing in opposite directions: similarity close to -1 (Opposite meaning)

The larger the cosine similarity, the more similar the two texts are in meaning.


## Keyword search vs vector search
---

Here's how the two approaches differ:

- Keyword search matches exact words. Vector search matches meaning.
- Keyword search suits specific terms, IDs, and names. Vector search suits paraphrased questions and natural language.
- Keyword search example: "pandas dataframe". Vector search example: "How do I work with tabular data?"
- Keyword search uses an inverted index (BM25, TF-IDF). Vector search uses a vector index based on cosine similarity.
- Keyword search misses synonyms and paraphrases. Vector search misses exact term matches.

Vector search is usually better, but it adds a lot of operational complexity. Start with text search, and reach for vectors once you can show they're worth the extra cost.

In practice the two work best together. Hybrid search combines them.
