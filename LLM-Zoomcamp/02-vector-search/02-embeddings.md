## Embeddings
---

Before do vector search, need to turn our text into vectors. this process is called as _**embedding**_.

We embed text into a vector space. The vectors we get back are also called _**embedding**_.

### Word embeddings and sentence embeddings
---

This idea comes from [word2vec](https://en.wikipedia.org/wiki/Word2vec). The model learns to place words as points in a multi-dimensional space. Words with similar meanings land close to each other.


The same idea works for entire sentences:

```text
Q1: "I just discovered the course. Can I still join it?"
Q2: "I just found out about the program. Can I still enroll?"

These two are close - they mean the same thing.

Q3: "How do I run Docker on Windows?"

This one is far away from Q1 and Q2.
```

Now imagine all 1200 documents in our FAQ dataset. Each one becomes a point in this space. When a user asks a question, we embed it into the same space and find the closest documents. Those nearest neighbors are our search results.

We'll use [sentence-transformers](https://www.sbert.net/), a popular
open-source library for embeddings. It runs locally on your machine, so
there are no API costs.