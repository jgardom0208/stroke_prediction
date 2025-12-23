### Flask app 
poetry run python src/stroke_prediction/stroke_predict_app.py
### Streamlit app
poetry run streamlit run src/stroke_prediction/stroke_predict_app_streamlit.py
### Pluggin export 
poetry self add poetry-plugin-export
### Exportar el requirements.txt 
poetry export -f requirements.txt --output requirements.txt