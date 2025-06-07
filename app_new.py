
import streamlit as st
#from generator import generate_script  # Import your generator function

# --- INPUT MODULE ---
st.title("📝 Script & PPT Generator")
st.markdown("Enter your presentation details below:")

with st.form("user_inputs"):
    #col1, col2 = st.columns(2)
    
    #with col1:
    topic = st.text_input("Topic*", placeholder="E.g., Global Warming")
    audience = st.selectbox("Audience*", ["Students", "Faculty", "General Public"])
        
    #with col2:
    tone = st.radio("Tone*", ["Formal", "Casual", "Persuasive"], horizontal=True)
    word_count = st.slider("Word Count", 100, 1000, 200)
    
    submitted = st.form_submit_button("Generate Script")

# --- PROCESSING & OUTPUT ---
if submitted and not topic:
    st.error("Please enter a topic!")
elif submitted:
    with st.status("🔍 Generating your script...", expanded=True) as status:
        # Create prompt
        prompt = f"Create a {tone.lower()} script about {topic} for {audience}, {word_count} words."
        
        # Generate script
        generated_script = "Here will be the generated script."  # Call your generator function
        
        # Display results
        status.update(label="✅ Script generated!", state="complete")
    
    # --- SCRIPT DISPLAY SECTION ---
    st.divider()
    st.subheader("📜 Your Generated Script")
    
    # Option 1: Simple text display
    st.write(generated_script)
    
    # Option 2: In a scrollable expander
    #with st.expander("View Full Script", expanded=True):
        st.write(generated_script)
    
    # Option 3: With markdown formatting
    #st.markdown(generated_script)
    
    # Option 4: In a code block (good for preserving formatting)
    #st.code(generated_script, language="markdown")
    
    # --- DOWNLOAD BUTTON ---
    st.download_button(
        label="📥 Download Script",
        data=generated_script,
        file_name=f"script_{topic[:20]}.txt",
        mime="text/plain"
    )
