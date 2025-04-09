import streamlit as st
import ollama

# Set Streamlit page configuration
st.set_page_config(
    page_title="Human-Like Blog Generator",
    page_icon="📝",
    layout="centered"
)

# Sidebar instructions
st.sidebar.title("📋 How to Use")
st.sidebar.info(
    "1. Enter a blog topic\n"
    "2. Let the AI write casually like a human\n"
    "3. Review, refine, or share it freely!\n\n"
    "⚙️ Powered by LLaMA 3.2 + Ollama"
)

# Optional header image
st.image(
    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
    caption="Creating blogs that sound like *you* ☕",
    use_column_width=True
)

# App title and intro
st.title("📝 Human-Like Blog Generator")
st.markdown("""
No stiff AI tone. No outlines. No robotic phrasing.  
This tool helps you write in a way that sounds real — like you’re talking to a friend, not filling in a template.
""")

# 👤 Refined, human-style prompt
def generate_blog(topic):
    prompt = f"""
Forget templates, outlines, or robotic phrasing. Just write a blog post about "{topic}" like a real human would.

Imagine you’re writing from a cozy café or your couch — it’s casual, maybe a bit quirky. Add personality. Talk to the reader like a friend. It’s okay to include a side story, a joke, or an off-topic thought that somehow loops back.

Avoid sounding polished or professional. No step-by-step structure, no corporate tone. Just a fluid, honest, slightly imperfect blog post with heart and voice.

Don’t explain that you're going to write. Don’t mention the format or the request. Just write the blog itself — like it came straight from your own mind.
"""

    response = ollama.chat(
        model="llama3.2:latest",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

# Input field for blog topic
st.markdown("### ✍️ Enter a blog topic:")
blog_topic = st.text_input("e.g. Why Explainable AI Actually Matters")

# Generate and display blog
if blog_topic:
    with st.spinner("🧠 Writing like a human would..."):
        blog = generate_blog(blog_topic)
        st.success("✅ Blog created!")
        st.subheader("📄 Here's your blog:")
        st.markdown(blog)  # Better formatting than st.write
