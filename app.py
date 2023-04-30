import stramlit as st
import pandas as pd
import numpy as np




st.set_page_config(
    page_title="CRM",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded")

colT1, colT2, colT3 = st.columns(3)
with colT2:
    st.title('ML for CRM')
#

col6, col3, col4, col5 = st.columns([0.5, 1.5, 0.5, 3])


st.sidebar.title('Use sidebar to execute activities')
# Taking File input
# global dff
global mm
global RFM_table

col1, col2 = st.columns(2)
with col1:
    data_file = st.file_uploader("Upload Main CSV", type=["csv"],  key='89')
    if data_file is not None:

        # file details
        file_details = {"filename": data_file.name,
                        "filetype": data_file.type, "filesize": data_file.size}
        st.write(file_details)

        # data wranggling
        dff = pd.read_csv(data_file)
        dff['TotalAmount'] = dff.apply(
            lambda row: (row['Quota']*row['Amount']), axis=1)
        # dff['CustomerID'] = dff['CustomerID'].astype(np.int64)
        dff['BillDate'] = pd.to_datetime(dff['BillDate'])
        dff.dropna(axis=0, subset=['Product', 'CustomerID'], inplace=True)

        # Display data
        if st.sidebar.checkbox('Display Main Data', False, key='29'):
            st.subheader('Show Main Input dataset')
            st.write(dff)
            st.write('''Take a look at the Main dataset you have fed to our CRM tool. Check for the attributes
and data values before moving further!!''')

        count = 1
    # test case for both none and is not none
    if data_file is None:
        dff = pd.read_csv("data/Main_Demo.csv")
        dff['TotalAmount'] = dff.apply(
            lambda row: (row['Quota']*row['Amount']), axis=1)
        dff['BillDate'] = pd.to_datetime(dff['BillDate'])
        dff.dropna(axis=0, subset=['Product', 'CustomerID'], inplace=True)
        if st.sidebar.checkbox('Display Main Data', False, key='29'):
            st.subheader('Show Main Input dataset')
            st.write(dff)
            st.write('''Take a look at the Main dataset you have fed to our CRM tool. Check for the attributes
and data values before moving further!!''')

            # Particular customer_id data
        if st.sidebar.checkbox('Access Input Main Data ', key='4254354'):
            CI1 = st.number_input('Enter a Customer ID',
                                  0, 9000000, 0, 1, key='1878')
            for i in range(len(dff)):
                if dff.CustomerID[i] == CI1:
                    st.subheader('Transaction No. {}'.format(count))
                    st.write('The Bill id of this Customer is {},This Customer Belongs to {}.The Product Purchased is {},its Merchnadise id is {} and the amount of Product Purchased is/are{} and the Price of each is {}.Total Transaction Amount is {}'.format(
                        dff.Bill[i], dff.Country[i], dff.Product[i], dff.MerchandiseID[i], dff.Quota[i], dff.Amount[i], dff.TotalAmount[i]))
#                st.write('Bil :', dff.Bill[i])
#                st.write('country :',dff.Country[i])
#                st.write('Merchandise ID', dff.MerchandiseID[i])
#                st.write('Product :', dff.Product[i])
#                st.write('Quota: ', dff.Quota[i])
#                st.write('Amount: ', dff.Amount[i])
#                st.write('Total Amount', dff.TotalAmount[i])
                    count = 1 + count
            st.write('Looks like this customer has a greater place in your revenue stream. Please find the details of this customer as per the dataset you provided.')

# prediction dataset upload
with col2:
    mm = st.file_uploader("Upload CSV for Prediction",
                          type=["csv"], key='8998')
    if mm is not None:
        file_details1 = {"filename": mm.name,
                         "filetype": mm.type, "filesize": mm.size}
        st.write(file_details1)

        dff1 = pd.read_csv(mm)
        dff1['TotalAmount'] = dff1.apply(
            lambda row: (row['Quota']*row['Amount']), axis=1)
        dff1['BillDate'] = pd.to_datetime(dff1['BillDate'])
        # dff['CustomerID'] = dff['CustomerID'].astype(np.int64)
        dff1.dropna(axis=0, subset=['Product', 'CustomerID'], inplace=True)

        # same as Main data
        if st.sidebar.checkbox('Display Data of for prediction', False, key='200'):
            st.subheader('Show Input dataset for prediction')
            st.write(dff1)
            st.write('''Take a look at the dataset for prediction you have fed to our CRM tool. Check for the attributes 
and data values before moving further!!''')
        count1 = 1

    if mm is None:
        dff1 = pd.read_csv("data/pred_trash.csv")
        dff1['TotalAmount'] = dff1.apply(
            lambda row: (row['Quota']*row['Amount']), axis=1)
        dff1['BillDate'] = pd.to_datetime(dff1['BillDate'])
        # dff['CustomerID'] = dff['CustomerID'].astype(np.int64)
        dff1.dropna(axis=0, subset=['Product', 'CustomerID'], inplace=True)

        if st.sidebar.checkbox('Display Data of for prediction', False, key='200'):
            st.subheader('Show Input dataset for prediction')
            st.write(dff1)
            st.write('''Take a look at the dataset for prediction you have fed to our CRM tool. Check for the attributes 
and data values before moving further!!''')

        if st.sidebar.checkbox('Access Input Pred Data ', key='698955312'):
            CI2 = st.number_input('Enter a Customer ID',
                                  0, 9000000, 0, 1, key='1875ss58')
            for i in range(len(dff1)):
                if dff1.CustomerID[i] == CI2:
                    st.subheader('Transaction No.'.format(count1))
                    st.write('The Bill id of this Customer is {}, This Customer Belongs to {}. The Product Purchased is {}, its Merchnadise id is {} and the amount of Product Purchased is/are {} and the Price of each is {}. Total Transaction Amount is {}'.format(
                        dff1.Bill[i], dff1.Country[i], dff1.Product[i], dff1.MerchandiseID[i], dff1.Quota[i], dff1.Amount[i], dff1.TotalAmount[i]))
#                st.subheader('Transaction No.', count)
#                st.write('Bil :', dff1.Bill[i])
#                st.write('country :',dff1.Country[i])
#                st.write('Merchandise ID', dff1.MerchandiseID[i])
#                st.write('Product :', dff1.Product[i])
#                st.write('Quota: ', dff1.Quota[i])
#                st.write('Amount: ', dff1.Amount[i])
#                st.write('Total Amount', dff1.TotalAmount[i])
                    count1 = count1 + 1
            st.write('Looks like this customer has a greater place in your revenue stream. Please find the details of this customer as per the dataset you provided.')


st.write("Note : This Datasets should have utmost eight attributes to enrich your analysis viz., any Identification number of order (Bill/Invoice Number/Order ID), Identification number of product (Merchandise ID/Stock Code/Product ID), short description or label of the product (Product name/Description), time indicator (Bill date/Invoice date in form of MM/DD/YY), product quantity (Quota/Quantity/Order) pricing details (Amount/Price per product), Total amount of products, Identification number of Customer (Customer ID/User ID) and region details (country/state/city).")
