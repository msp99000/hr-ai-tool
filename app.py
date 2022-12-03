# Load dependencies

import pickle
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

# Load  Model
pickle_in = open('classifier.pkl', 'rb') 
model = pickle.load(pickle_in)




def prediction(education, no_of_trainings, age, previous_year_rating, length_of_service, awards_won, avg_training_score):
    
    if education == "Master's & above":
        education = 3
    if education == "Bachelor's":
        education = 2
    if education == "Below Secondary":
        education = 1

    if awards_won == "Yes":
        awards_won = 1
    if awards_won == "No":
        awards_won = 0

    prediction =  model.predict([[education, no_of_trainings, age, previous_year_rating, length_of_service, awards_won, avg_training_score]])

    if prediction == 0:
        return False
    if prediction == 1:
        return True
    

def main():

    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">HR Analytics AI App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 

    education = st.selectbox("Select Education", ("Master's & above", "Bachelor's", "Below Secondary"))
    no_of_trainings = st.selectbox("Select the number of trainings for employee", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    age = st.slider("Select the age of employee", min_value = 20, max_value = 60, step = 1)
    previous_year_rating = st.selectbox("Select the previous year rating of the employee", (1, 2, 3, 4, 5))
    length_of_service = st.slider("Select length of service of employee", min_value = 1, max_value = 37, step = 1)
    awards_won = st.selectbox("Did the employee win any awards?", ("Yes", "No"))
    avg_training_score = st.text_input("What is the average training score of the employee?")
    result = True

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(education, no_of_trainings, age, previous_year_rating, length_of_service, awards_won, avg_training_score) 
        if result == True:
            st.success("The employee can be considered for promotion")
        if result == False:
            st.error("The employee cannot be considered for promotion")


if __name__=='__main__': 
    main()


