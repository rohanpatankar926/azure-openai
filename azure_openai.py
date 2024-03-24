import streamlit as st
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, AIMessage

model = AzureChatOpenAI(
    openai_api_base="https://enterpriseml.openai.azure.com/",
    openai_api_version="2023-07-01-preview",
    openai_api_type="azure",
    streaming=False,
    openai_api_key=os.environ["OPENAI_API_KEY"],
    deployment_name="m1",
    temperature=0.0
)

def stream(message):
    response = model.stream([
        AIMessage(content="You are an intelligent AI bot which will answer the user questions."),
        HumanMessage(content=message),
    ])
    return "".join([mod.content for mod in response])

st.title("AzureChatOpenAI Demo")
question = st.text_input("Ask a question:")
if st.button("Submit"):
    if question:
        answer = stream(question)
        st.write("Response:")
        st.write(answer)

