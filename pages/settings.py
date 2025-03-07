import streamlit as st
import app.pages as pages
import app.utils as utils

# App title
pages.show_home()
pages.show_sidebar()

st.header("⚙️Settings")

# Get all styles
styles = utils.get_styles()

if styles:
    # Create a selection box for styles
    style_names = [style["name"] for style in styles if style.get("name")]
    if style_names:
        selected_style = st.selectbox(":blue[**Select a style to delete:**]", style_names)
        
        # Get the selected style's full details
        selected_style_data = next((style for style in styles if style["name"] == selected_style), None)
        
        if selected_style_data:            
            # Delete button
            if st.button(f":blue[**Delete '{selected_style}'**]"):
                try:
                    utils.styles_container.delete_item(
                        item=selected_style_data["id"], 
                        partition_key=selected_style_data["style"]
                    )
                    st.success(f"Style '{selected_style}' has been deleted successfully!")
                except Exception as e:
                    st.error(f"An error occurred while deleting the style: {str(e)}")
    else:
        st.info("No named styles found in the database.")
else:
    st.info("No styles found in the database.")