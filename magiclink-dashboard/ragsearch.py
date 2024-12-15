import openai
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

# Initialize OpenAI API
openai.api_key = 'your_openai_api_key'

# Initialize Azure AI Search client
search_client = SearchClient(
    endpoint='your_search_service_endpoint',
    index_name='your_index_name',
    credential=AzureKeyCredential('your_search_service_api_key')
)

def retrieve_legal_documents(query):
    results = search_client.search(query)
    documents = [result['content'] for result in results]
    return documents

def generate_answer(documents, question):
    context = " ".join(documents)
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Question: {question}\nContext: {context}\nAnswer:",
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    return answer

def get_answer(question):
    documents = retrieve_legal_documents(question)
    answer = generate_answer(documents, question)
    return answer

def main():
    question = input("Enter your question about Swiss legal regulations: ")
    answer = get_answer(question)
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
