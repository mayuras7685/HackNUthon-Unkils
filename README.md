## ML for CRM 

This document serves as a guide to the ML for CRM(Customer Relationship Management) project. It provides an overview of the project, and instructions on how to use it.

# Project Overview
This ML model is a web-based application designed to help businesses manage their interactions with customers. The application provides features such as:
- Data Visualization and Analysis
- Customer Segmentation
- Customer Classification
- Sales Forecasting
- Customer Linked Prediction (work in progress...)

# Features
The ML model include the following features:
- Data Visualization and Analysis: Users can see the data inserted in the format of csv, and can also do prediction
- Customer Segmentation: In this feature, customers are segregated into number of segments like (Champions, New_customers, About to sleep, etc.)
  Their are two methods of segmenting customers, one via the RFM metrics here we can view the data in differnt types of graph and another unique method is Hybrid methods.
- Customer Classification: It will classify the customer into 2 types if the percentage is very high then it will return 0 else it will return 1
- Sales Forecasting: This section will provide you the insights of your business performance in future by considering your present & past. So, get, set, forecast…

# Installation
To install this project, follow these steps:

1. Clone the project repository from Github.
2. Create a virtual environment and activate it.
3. Install the project requirements using the command `pip install -r requirements.txt`
4. Start the app by using `streamlit run crm.py`
