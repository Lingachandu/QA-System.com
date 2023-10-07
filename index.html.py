import streamlit as st
import streamlit.components.v1 as components
from transformers import pipeline

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <style>
         .jumbostron{
            background: lightcoral;
         }

          .display-4{
          display: flex;
    justify-content: center;
    color: red;
    font-weight: bold;
          }

          p{
          display: flex;
    justify-content: center;
          }
    </style>

    <div class="jumbotron jumbotron-fluid">
  <div class="container">
    <h1 class="display-4">QA SYSTEM</h1>
    <p class="lead">Find answer to the question of your article</p>
  </div>
</div>
    
     
      
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=300,
)
@st.cache_data
def load_model(allow_output_mutation=True):
    model=pipeline("question-answering")
    return model

qa=load_model()
st.title("Ask question based on your article")
articles=st.text_area("please enter your article")
quest=st.text_input("Ask your question based on  the article")
button = st.button ("Answer")
with st.spinner("Finding Answer..."):
    if button and articles:
        answers = qa(question=quest,context=articles)
        st.success(answers['answer'])

