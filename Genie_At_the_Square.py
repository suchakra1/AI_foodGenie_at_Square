import streamlit as st
import os
import datetime
import google.generativeai as palm

API_KEY="AIzaSyDVWOEtgVZlELozCd0iGavardeJt83GekA"



palm.configure(api_key=API_KEY)

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}




# Set up a directory for saving the menu
if not os.path.exists("pages/menu_posts"):
    os.makedirs("pages/menu_posts")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True
    
    
    
# Define the sidebar for creating AI menu
def create_data(usr,prompt,recipe):       
        # Save the  order 
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    post_filename = f"{timestamp}-{prompt}.md"
    with open(f"pages/menu_posts/{post_filename}", "w") as f:
        f.write(f"User: {usr}\n")
        f.write(f"Prompt: {prompt}\n")
        f.write(f"Timestamp: {timestamp}\n")            
        f.write("\n")
        f.write(recipe)
        
def generate_ai_menu():
    usr = st.text_input('Please use your email','anonymous@gmail.com')
    
    if prompt := st.chat_input(placeholder="write a recipe with pineapple and chicken"):
        st.chat_message("user").write(prompt)
        
    if prompt == None:
        st.subheader("Please generate your recipe with Google Palm AI")        
    else:
        response = palm.generate_text(
   	     **defaults,
          prompt=prompt
            )
        st.write(response.result)
        create_data(usr,prompt,response.result)  
        st.success("Your recipe wish is sent to the Genie")
        
        
def main():
    """
    The main function for the Streamlit app.

    :return: None.
    """
    st.title("Genie at the Square")    
    
    data = generate_ai_menu()    
    
    
           
if __name__ == "__main__":
    main()


#