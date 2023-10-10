# Import necessary libraries
import streamlit as st

# Define the main function for the Streamlit app
def main():
    st.title("Analysis Selection")

    # Create three columns for the buttons
    col1, col2, col3 = st.columns(3)

    # Place a button in each column
    if col1.button("Analysis 1"):
        analysis_1()
    if col2.button("Analysis 2"):
        analysis_2()
    if col3.button("Analysis 3"):
        analysis_3()

# Define the function for Analysis 1
def analysis_1():
    st.title("Analysis 1")
    st.write("Here is the content for Analysis 1.")

# Define the function for Analysis 2
def analysis_2():
    st.title("Analysis 2")
    st.write("Here is the content for Analysis 2.")

# Define the function for Analysis 3
def analysis_3():
    st.title("Analysis 3")
    st.write("Here is the content for Analysis 3.")

# Run the main function
if __name__ == "__main__":
    main()
