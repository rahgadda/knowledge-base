# Streamlit

## Overview
- Streamlit is a `free and open-source framework` to rapidly build and share beautiful machine learning and data science web apps without prior knowledge of Web Development.
- It allows you to create user interfaces with minimal code.
- Unlike gradio, Streamlit is component based, there are product components, third-party and sdk to create your own comopnents.
- It was built in `React` and first release in `October 2019`, by a software company founded by `Adrien Treuille, Amanda Kelly, and Thiago Teixeira in 2018 in San Francisco, California`
- Below are some high-level ML & Datascience libraries that are supported by Streamlit.

  | Usecase          	| Python Libraries                           	                    |
  |------------------	|---------------------------------------------------------------	|
  | Data Processing  	| Pandas, Numpy, PyArrow, Snowpark, PySpark                       |
  | Visualization    	| Matplotlib, Altair, Vega-Lite, Plotly, Bokeh, PyDeck, GraphViz 	|
  | Machine Learning 	| PyTorch, Tensorflow, Keras, Scikit-learn   	                    |
  | Computer Vision  	| OpenCV, imgaug, SimpleCV, BoofCV           	                    |

## Installation
- It is a python library that can be installed using
  ```sh
  pip install streamlit
  ```
- Create streamlit hello application
  ```python
  # Create streamlit python application hello.py
  import streamlit as st

  st.write("Hello World!!!!")
  ```  
- To run a streamlit application
  ```sh
  # Running hello.py using python
  python -m streamlit run hello.py

  # It is equivalent to
  streamlit run hello.py
  ```
- If there are any changes applied on `hello.py`, a message `Source file changed` shown. The `Rerun` button will run all the code blocks from the start and display the changes thereafter.
  ![](00-images/01-streamlit-source-chaged.png)

## Reference
- [Streamlit Documentation](https://docs.streamlit.io/library/get-started)
- [Component API](https://docs.streamlit.io/library/api-reference)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Awesome Streamlit](https://awesome-streamlit.org/)
- Beginner's Guide to Streamlit with Python -Ebook