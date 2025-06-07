
import streamlit as st
#from scrept_generator import generator

# --- INPUT MODULE ---
st.title("📝 Script & PPT Generator")
st.markdown("Enter your presentation details below:")

# Input Fields (Left Column)
with st.form("user_inputs"):
    col1, col2 = st.columns(2)
    
    with col1:
        # Required fields
        topic = st.text_input("Topic*", placeholder="E.g., Global Warming")
        audience = st.selectbox("Audience*", ["Students", "Faculty", "General Public"])
        
    with col2:
        # Optional fields
        tone = st.radio("Tone*", ["Formal", "Casual", "Persuasive"], horizontal=True)
        word_count = st.slider("Word Count", 100, 1000, 200)
    
    # Validation + Submit Button
    submitted = st.form_submit_button("Generate Script")
    if submitted and not topic:
        st.error("Please enter a topic!")
    elif submitted:
        st.success("Inputs captured!")
        prompt = f"Create a {tone.lower()} script about {topic} for {audience}, {word_count} words."
        
        # call the generator function
        # generated_scrept = scrept_generator(prompt)
        # 

        # ferther part will be done in the bases of scrept_generator_function.
        generated_scrept = "The Taj Mahal is a white marble mausoleum in Agra, India, built by the Mughal emperor Shah Jahan as a memorial for his wife, Mumtaz Mahal. It's considered a masterpiece of Indo-Islamic architecture and one of the world's most admired structures. The Taj Mahal is a UNESCO World Heritage Site and attracts millions of visitors annually."
        status.update(label="✅ Script generated!", state="complete")

        # --- SCRIPT DISPLAY SECTION ---
        stdivider()
        st.subheader("📜 Your Generated Script")

        st.write(generated_script)
        # --- DOWNLOAD BUTTON ---
        st.download_button(
            label="📥 Download Script",
            data=generated_script,
            file_name=f"script_{topic[:20]}.txt",
            mime="text/plain"
        )

