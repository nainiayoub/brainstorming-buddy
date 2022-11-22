import streamlit as st
import openai
from datetime import datetime
from streamlit.components.v1 import html
import webbrowser

st.set_page_config(page_title="Brainstorming Buddy")


html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """

button = """
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="nainiayoub" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
"""


with st.sidebar:
    st.markdown("""
    # About 
    Brainstorming Buddy is a helper tool built on GPT-3 to generate ideas on a given topic. 
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # How does it work
    Simply enter the topic of interest in the text field below and ideas will be generated.
    You can also download the output as txt.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    You can help sustain the project.<br/>
    Find me at: [Twitter](https://twitter.com/nainia_ayoub) | [LinkedIn](https://www.linkedin.com/in/ayoub-nainia/?locale=en_US) | [GitHub](https://github.com/nainiayoub) 
    
    """,
    unsafe_allow_html=True,
    )


input_text = None
if 'output' not in st.session_state:
    st.session_state['output'] = 0

if st.session_state['output'] <=2:
    st.markdown("""
    # Brainstorming Buddy
    """)
    input_text = st.text_input("Brainstorm ideas for", disabled=False)
    st.session_state['output'] = st.session_state['output'] + 1
else:
    # input_text = st.text_input("Brainstorm ideas for", disabled=True)
    st.info("💡Thank you! You can help support sustaining the Brainstorming Buddy through [buy me a coffee](https://www.buymeacoffee.com/nainiayoub).  🔁🔁🔁 Refresh for more brainstorming!")
    url = "https://twitter.com/intent/tweet?text=I%20just%20used%20the%20Brainstorming%20Buddy%20streamlit%20helper%20tool%20by%20@nainia_ayoub!%0A%0Ahttps://brainstorming-buddy.streamlit.app/"
    if st.button('Tweet about this!'):
        webbrowser.open_new_tab(url)

hide="""
<style>
footer{
	visibility: hidden;
    position: relative;
}
.viewerBadge_container__1QSob{
    visibility: hidden;
}
<style>
"""
st.markdown(hide, unsafe_allow_html=True)

html(button, height=70, width=220)
st.markdown(
    """
    <style>
        iframe[width="220"] {
            position: fixed;
            bottom: 60px;
            right: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
if input_text:
    prompt = "Brainstorm ideas for "+str(input_text)
    if prompt:
        openai.api_key = st.secrets["openaiKey"]
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150)
        brainstorming_output = response['choices'][0]['text']
        today = datetime.today().strftime('%Y-%m-%d')
        topic = "Brainstorming ideas for: "+input_text+"\n@Date: "+str(today)+"\n"+brainstorming_output
        
        st.info(brainstorming_output)
        filename = "brainstorming_"+str(today)+".txt"
        btn = st.download_button(
            label="Download txt",
            data=topic,
            file_name=filename
        )

        
        

        