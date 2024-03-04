import os
import streamlit as st




url= "Recipes"


# Define the main content area for viewing existing blog posts
def create_main_content():
    st.title("Genie at the Square : Menu Today ")
    post_files = os.listdir("pages/menu_posts")
    s = len(post_files)
    post_files=post_files[s-3:]
    if not post_files:
        st.info("No Menu posted")
        
    for post_file in post_files:
        with open(f"pages/menu_posts/{post_file}", "r") as f:
            post_content = f.read()
            post_lines = post_content.split("\n")
            post_usr = post_lines[0][6:]
            post_title = post_lines[1][7:]
            post_timestamp = post_lines[2][10:]           
            post_content = "\n".join(post_lines[4:])
            c = st.container()
            st.subheader(f"{post_title}")
            c.write(f"*User :* {post_usr}  "f"   Date/Time :   {post_timestamp}")           
            
            if st.button('Get Recipe',key=post_title):
                c.markdown(post_content)
               
           

# Run the app
create_main_content()