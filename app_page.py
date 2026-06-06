import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Product Analyzer",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.hero {
    background: linear-gradient(135deg,#667eea,#764ba2);
    padding: 30px;
    border-radius: 20px;
    text-align:center;
    color:white;
    margin-bottom:20px;
}

.metric-card {
    background:#1e1e1e;
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
    border:1px solid #333;
}

.result-box {
    background:#1a1a1a;
    padding:25px;
    border-radius:20px;
    border:1px solid #444;
    color:white;
}

.stTextInput input {
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
<h1>🤖 AI Product Analyzer</h1>
<h4>Analyze Any Product Website Using Generative AI</h4>
<p>Get Features • Pros • Cons • Ratings • Buying Recommendations</p>
</div>
""", unsafe_allow_html=True)

# ---------------- FEATURE CARDS ----------------
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
    <h2>⭐</h2>
    <h4>Features</h4>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
    <h2>🔥</h2>
    <h4>Pros & Cons</h4>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
    <h2>📊</h2>
    <h4>Specifications</h4>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
    <h2>💰</h2>
    <h4>Value Analysis</h4>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------- URL INPUT ----------------
url = st.text_input(
    "🔗 Enter Product URL",
    placeholder="https://www.smartprix.com/..."
)

# ---------------- ANALYZE BUTTON ----------------
if st.button("🚀 Analyze Product", use_container_width=True):

    with st.spinner("Analyzing Product..."):

        load_dotenv()

        loader = WebBaseLoader(url)
        docs = loader.load()

        template = ChatPromptTemplate.from_messages([
            (
                "system",
                """
                You are an expert Product Analysis AI.

                Analyze the webpage and generate:

                🛍️ Product Name
                📖 Overview
                ⭐ Features
                🔥 Pros
                ❌ Cons
                📊 Specifications
                🎯 Best For
                💰 Value For Money
                🏆 Final Verdict

                Use emojis and attractive formatting.
                """
            ),
            ("human", "{content}")
        ])

        llm = ChatMistralAI(
            model="mistral-large-latest"
        )

        content = docs[0].page_content[:10000]

        prompt = template.format_messages(
            content=content
        )

        response = llm.invoke(prompt)

        st.markdown("""
        <div class="result-box">
        """, unsafe_allow_html=True)

        st.markdown(response.content)

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Powered by LangChain + Mistral AI + Streamlit")
