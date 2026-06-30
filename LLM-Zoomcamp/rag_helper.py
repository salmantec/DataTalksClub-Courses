# This file contains the RAG logic

# Build context

# Prompt has two parts: instructions and the question + context. We can separate them for better readability and maintenance.
# Instructions are general guidelines for the model on how to use the context to answer questions. The question + context part is dynamic and changes with each user query.


INSTRUCTIONS = """
Your task is to answer questions from the course participants based on the provided context.
Use the context to find relevant information and provide accurate and helpful answers to the questions. 
If the context does not contain enough information to answer a question, respond with "I don't know".
"""

# Build the RAG prompt by combining the question with the provided context

USER_PROMPT_TEMPLATE = """
Question:
{question}

Context:
{context}
"""

# We use a class because index and openai_client are currently global variables. Move the functions to a separate file and those globals aren't there anymore. 
# We could import them back, but that ties the file to one specific index and one specific client. That makes the code hard to reuse and adjust.

# So we put the dependencies inside a class instead. The index and the LLM client become constructor arguments. Now we can pass any index or client we want when we create the object. 
# And because it's a class, we can subclass it later to override one piece without touching the rest. For example, we can swap OpenAI for a local model.


class RAGBase:

    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTIONS,
        prompt_template=USER_PROMPT_TEMPLATE,
        course="llm-zoomcamp",
        model="gpt-4.1-mini"
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.prompt_template = prompt_template
        self.course = course
        self.model = model

    # RAG starts with search

    def search(self, question, num_results=5):
        boost_dict={"question": 2.0, "section": 0.5} # Boost the question field twice as much as the section field
        filter_dict={"course": self.course} # Filter results to only include documents from the specified course

        return self.index.search(
            question, 
            boost_dict=boost_dict,
            filter_dict=filter_dict,
            num_results=num_results
        )
    
    def build_context(self, search_results):
        lines = []

        for doc in search_results:
            lines.append(doc["section"])
            lines.append("Q: " + doc["question"])
            lines.append("A: " + doc["answer"])
            lines.append("")

        return "\n".join(lines).strip()

    def build_prompt(self, query, search_results):
        context = self.build_context(search_results)
        return self.prompt_template.format(
            question=query, context=context
        )
    
    def llm(self, prompt):
        input_messages = [
            {"role": "developer", "content": self.instructions},
            {"role": "user", "content": prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )

        return response.output_text
    

    def rag(self, query):
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        answer = self.llm(prompt)
        return answer
