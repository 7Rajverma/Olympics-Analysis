# streamlit run app.py
import plotly.figure_factory as ff
import seaborn as sns
import streamlit as st
import processing, helper
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv("athlete_events_25mb.csv")
region = pd.read_csv("noc_regions.csv")

df = processing.preprocess(df, region)


st.sidebar.title('OLYMPICS ANALYSIS')
user_menu = st.sidebar.radio(
    'Select an option',
    ("Medal Tally", 'Overall Analysis', 'Country wise Analysis', 'Athlete wise Analysis', )
)
# st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox('Select Year', years)
    selected_country = st.sidebar.selectbox('Select Year', country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in" + str(selected_year) + "Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " Overall performance in Olympics")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " Overall performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

if user_menu == "Overall Analysis":
    st.header("Top Statistics")
    editions = df['Year'].unique().shape[0]-1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nation = df['region'].unique().shape[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Edition")
        st.title(editions)
    with col2:
        st.header("Host")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Athletes")
        st.title(athletes)
    with col3:
        st.header("Nations")
        st.title(nation)


    nation_over_year = helper.participating_nations_over_year(df)
    # Plot graph
    fig = px.line(nation_over_year, x='Year', y='count', color_discrete_sequence=['#FF5733'])
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_year = helper.participating_events_over_year(df)
    fig = px.line(events_over_year, x='Year', y="count")
    st.title("Events over the years")
    st.plotly_chart(fig)

    athletes_over_year = helper.participating_athletes_over_year(df)
    fig = px.line(athletes_over_year, x='Year', y="count", color_discrete_sequence=['#FF5733'])
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    sport_over_year = helper.participating_sports_over_year(df)
    fig = px.line(sport_over_year, x='Year', y="count")
    st.title("Sports over the years")
    st.plotly_chart(fig)

    st.title("Number of events over time(Every Sport)")
    fig, ax = plt.subplots(figsize=(25, 25))
    x = df.drop_duplicates(["Year", "Sport", "Event"])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc="count").fillna(0)
                     .astype('int'), annot=True)
    st.pyplot(fig)



    st.title("Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    selected_sport = st.selectbox('Select a Sport', sport_list)
    x = helper.most_successful(df, selected_sport)
    st.table(x)

# Country wise Analysis

if user_menu == "Country wise Analysis":
    st.title("Country wise Analysis")
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.sidebar.selectbox('Select a Country', country_list)
    country_df = helper.year_wise_medal_tally(df, selected_country)
    fig = px.line(country_df, x='Year', y="Medal", color_discrete_sequence=['#FF5733'])
    st.title(selected_country + " Madel Tally over the years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt, annot=True)
    st.pyplot(fig)


    st.title("Top 10 Athletes of " + selected_country)
    top_10_df = helper.most_successful_country_wise(df, selected_country)
    st.table(top_10_df)

if user_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bzonze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.header("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df, selected_sport)
    fig, ax = plt.subplots()
    ax = sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], s=60)
    st.pyplot(fig)

    st.title('Men vs Woman Participation Over the Years')
    final = helper.men_vs_woman(df)
    fig = px.line(final, x="Year", y=['Male', 'Female'])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)



