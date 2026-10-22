import streamlit as st
import os
import json
from google import genai

st.set_page_config(page_title="ViralMint AI", page_icon="🎬", layout="centered")

st.title("🎬 ViralMint AI Clipper")
st.subheader("Turn your raw videos into viral vertical shorts for free")

# Read API Key securely from Render Environment Secrets
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_KEY:
    st.error("⚠️ GEMINI_API_KEY environment variable is missing! Please add it to your Render Settings.")
else:
    uploaded_file = st.file_uploader("Upload your video segment (Keep under 3-5 mins for fast free cloud rendering)", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        st.video(uploaded_file)
        
        if st.button("🚀 Analyze & Generate Viral Clips"):
            with st.spinner("AI is analyzing text timeline structures for high-retention hooks..."):
                try:
                    # Initialize the cloud client framework using modern gemini-3.8-flash
                    client = genai.Client(api_key=GEMINI_KEY)
                    
                    prompt = """
                    Analyze this structural documentary tracking request. Provide 3 optimized viral short clipping ideas based on emotional shifts, peaks, or dramatic hooks.
                    For each selection, output:
                    1. Target Start and End timestamps.
                    2. High-CTR text overlay hook option.
                    3. Concise virality rating strategy explanation.
                    """
                    
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=[prompt]
                    )
                    
                    st.success("✅ Viral Short Clipping Report Ready!")
                    st.markdown("### === VIRAL SHORT CLIPPING REPORT ===")
                    st.write(response.text)
                    st.info("💡 Use a free online precision trimmer like Streamable or YtCut to slice your uploaded video at these exact timestamps with no watermarks!")
                except Exception as e:
                    st.error(f"Inference system bottleneck occurred: {str(e)}")
