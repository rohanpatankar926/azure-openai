FROM python
RUN pip install langchain==0.0.298 openai==0.27.8 streamlit
ENV OPENAI_API_KEY=20d8bed178514a44864f608756e6d878
ENTRYPOINT [ "streamlit run azure_openai.py" ]