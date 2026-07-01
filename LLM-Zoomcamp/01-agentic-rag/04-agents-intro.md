In Part 1 of this module we built RAG pipelines.

Every pipeline we wrote followed the same flow:

- search the FAQ,
- build a prompt with the results,
- send it to the LLM.

This returns good answers when the user's query matches the documents.
The search finds the right entry, the LLM reads it, and you get a
helpful reply.

Often, though, the search returns nothing useful.

- Maybe the user made a typo.
- Maybe they asked the question in an unusual way.
- Maybe they need information from two different searches.

We use lexical search here, so the search looks for an exact match.
One typo and it misses the entry it needed. In our pipeline there's
no recovery. The search runs once, and if it returns garbage the LLM
gets garbage. Our pipeline always does the same thing, no matter what.

Instead of routing the user question straight to search, we can hand
control to the LLM and let it drive.

The LLM is in charge now, and it can:

- fix typos
- search again with different terms
- ask the user a clarifying question

A fixed flow can't do any of this. Once we put the LLM in control,
our system becomes agentic, so it's flexible rather than rigid.

An agent uses an LLM to decide which actions to take and in which
order. Instead of a fixed flow, the LLM chooses what to do at each
step.