# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

# Define the main function for the Streamlit app
def main():

    # Create four columns for the images


    st.image("images/app/all_logos.png", use_column_width=True)
    

    st.markdown("<h1 style='text-align: center; color: white;'>Alimentário - Análises</h1>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; color: white;'>Clique no questionário que deseja ver os resultados!</h3>", unsafe_allow_html=True)

    # Create three columns for the images and buttons
    col1, col2, col3 = st.columns(3)

    # Display an image in each column
    col1.image("images/app/agricultores.jpeg", use_column_width=True)
    if col1.button("Agricultores e Familiares"):
        analysis_1()

    col2.image("images/app/consumidores.jpeg", use_column_width=True)
    if col2.button("Consumidores"):
        analysis_2()

    col3.image("images/app/teste.png", use_column_width=True)
    if col3.button("Sites e Plataformas"):
        analysis_3()

# Define the function for Analysis 1
def analysis_1():
    st.title("Agricultores e Familiares")
    # Sample data
    dates = pd.date_range("20220101", periods=12)
    sales = np.random.randn(12).cumsum()
    df = pd.DataFrame({"Date": dates, "Sales": sales})

    #Descriptive statistics table
    st.subheader("Estatística Descritiva")
    st.table(df.describe())

    # Line chart
    st.line_chart(df.set_index("Date"))
    
    # Area chart
    st.area_chart(df.set_index("Date"))

    # Bar chart
    st.bar_chart(df.set_index("Date"))

    # Histogram using plotly
    fig = px.histogram(df, x="Sales", nbins=20, title="Distribution of Sales")
    st.plotly_chart(fig)

    # Altair scatter plot
    scatter = alt.Chart(df).mark_circle(size=60).encode(
        x='Date:T',
        y='Sales:Q',
        tooltip=['Date', 'Sales']
    ).interactive()
    st.altair_chart(scatter, use_container_width=True)

    # Comment section
    st.subheader("Deixe um comentário sobre a análise de Agricultores e Familiares")
    comment = st.text_area("Your comment here...")
    if st.button("Submit"):
        save_comment("Agricultores e Familiares", comment)
        st.success("Comment saved!")

    display_comments("Agricultores e Familiares")

# Define the function for Analysis 2
def analysis_2():
    st.title("Consumidores")
    categories = ["Electronics", "Clothing", "Groceries", "Books"]
    sales = np.random.randint(50, 500, size=len(categories))
    df = pd.DataFrame({"Category": categories, "Sales": sales})

    # Descriptive statistics table
    st.subheader("Estatística Descritiva")
    st.table(df.describe())

    # Bar chart
    st.bar_chart(df.set_index("Category"))

    # Horizontal bar chart using plotly
    fig = px.bar(df, x="Sales", y="Category", orientation='h', title="Sales by Product Category (Horizontal)")
    st.plotly_chart(fig)

    # Area chart
    st.area_chart(df.set_index("Category"))

    # Line chart
    st.line_chart(df.set_index("Category"))

    # Altair scatter plot
    scatter = alt.Chart(df).mark_circle(size=60).encode(
        x='Category:O',
        y='Sales:Q',
        tooltip=['Category', 'Sales']
    ).interactive()
    st.altair_chart(scatter, use_container_width=True)

    # Comment section
    st.subheader("Deixe um comentário sobre a análise de Consumidores")
    comment = st.text_area("Your comment here...")
    if st.button("Submit"):
        save_comment("Consumidores", comment)
        st.success("Comment saved!")

    display_comments("Consumidores")

# Define the function for Analysis 3
def analysis_3():
    st.title("Sites e Plataformas")
    # Sample data
    products = ["Product A", "Product B", "Product C", "Product D"]
    market_share = np.random.randint(10, 100, size=len(products))
    df = pd.DataFrame({"Product": products, "Market Share": market_share})

    # Descriptive statistics table
    st.subheader("Estatística Descritiva")
    st.table(df.describe())

    # Pie chart using matplotlib
    fig, ax = plt.subplots()
    ax.pie(df["Market Share"], labels=df["Product"], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

    # Bar chart
    st.bar_chart(df.set_index("Product"))

    # Area chart
    st.area_chart(df.set_index("Product"))

    # Line chart
    st.line_chart(df.set_index("Product"))

    # Altair scatter plot
    scatter = alt.Chart(df).mark_circle(size=60).encode(
        x='Product:O',
        y='Market Share:Q',
        tooltip=['Product', 'Market Share']
    ).interactive()
    st.altair_chart(scatter, use_container_width=True)

    # Comment section
    st.subheader("Deixe um comentário sobre a análise de Sites e Plataformas")
    comment = st.text_area("Your comment here...")
    if st.button("Submit"):
        save_comment("Sites e Plataformas", comment)
        st.success("Comment saved!")

    display_comments("Sites e Plataformas")

# Define a function to save comments to a file
def save_comment(analysis_name, comment):
    with open("comments.txt", "a") as file:
        file.write(f"{analysis_name} - {comment}\n")

# Define a function to read and display comments for a specific analysis
def display_comments(analysis_name):
    comments = []
    try:
        with open("comments.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(analysis_name):
                    comments.append(line.split(" - ")[1])
    except FileNotFoundError:
        # If the file doesn't exist yet, just return an empty list
        pass

    if comments:
        st.subheader("Comments")
        for comment in comments:
            st.write(comment)

# Run the main function
if __name__ == "__main__":
    main()
