import streamlit as st

# Initialize session state variables if they don't exist
if 'groups' not in st.session_state:
    st.session_state.groups = []
if 'current_group' not in st.session_state:
    st.session_state.current_group = None

# Function to handle group creation
def create_group(group_name):
    st.session_state.current_group = group_name
    st.session_state.groups.append(group_name)
    st.success(f"Group '{group_name}' created!")
    st.session_state.page = 'home'  # Redirect to the home page after creation

# Page 1: Select or Create a Group
def select_or_create_group():
    st.title("Select your group to begin recording expenses.")
    
    # Display existing groups if any
    if st.session_state.groups:
        st.subheader("Recent Groups")
        for group in st.session_state.groups:
            if st.button(f"Select {group}"):
                st.session_state.current_group = group
                # Redirect to group's expense page here if needed
    
    # Buttons for creating or joining a group
    if st.button("Create a new group"):
        # Redirect to the group creation page
        st.session_state.page = 'create_group'

# Page 2: Create a Group
def create_group_page():
    
    # "Back" button to return to the home page
    if st.button("← Back"):
        st.session_state.page = 'home'
        
    st.title("Create a new group")

    group_name = st.text_input("Group Name", key='group_name_input')
    if st.button("Create Group"):
        if group_name:
            create_group(group_name)
        else:
            st.warning("Please enter a group name.")

# Setup page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if st.session_state.page == 'home':
    select_or_create_group()
elif st.session_state.page == 'create_group':
    create_group_page()