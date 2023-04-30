import streamlit as st
import matplotlib as plt
import numpy as np
from RFM import rfm
from sklearn.preprocessing import StandardScaler

def Pre_hybrid(self):
        # Scaling the feature
        scale = StandardScaler()
        cols = ['Recency', 'Frequency', 'Monetary']
        RFM_table_scaler = scale.fit_transform(rfm.RFMvalues()[cols])
        # Linkage
        qq = plt.figure(figsize=(20, 20))
        mergings = linkage(
            RFM_table_scaler, method='complete', metric='euclidean')
        dendrogram(mergings)
        plt.xlabel('Observations')
        plt.ylabel('Number of similarities')
        st.pyplot(qq)

# skew values
def skew_data(self):
     return rfm.RFMvalues().agg(['skew', 'kurtosis']).transpose()

def Transform(self):
        RFM_h = rfm.RFMvalues().filter(
            ['CustomerID', 'Recency', 'Frequency', 'Monetary'])

        RFM_h['r_quartile'] = pd.qcut(
            RFM_h['Recency'], 5, labels=[5, 4, 3, 2, 1])

        RFM_h['f_quartile'] = pd.qcut(RFM_h['Frequency'].rank(
            method="first"), 5, labels=[1, 2, 3, 4, 5])

        RFM_h['rev_quartile'] = pd.qcut(
            RFM_h['Monetary'], 5, labels=[1, 2, 3, 4, 5])

        RFM_h['Monetary_T'] = np.log10(RFM_h['Monetary'])

        RFM_h['Frequency_T'] = np.cbrt(RFM_h['Frequency'])

        RFM_h['Frequency_T'] = np.cbrt(RFM_h['Frequency_T'])

        RFM_h['Frequency_T'] = np.sqrt(RFM_h['Frequency_T'])

        RFM_h['Recency_T'] = np.cbrt(RFM_h['Recency'])

        return RFM_h

def Trans_data(self):
        COLUMNS = ['Recency', 'Frequency', 'Monetary',
                   'Recency_T', 'Monetary_T', 'Frequency_T']
        COL = st.sidebar.selectbox("Select Feature", COLUMNS, key='7')
        ww = plt.figure(figsize=(6, 2))
        sns.distplot(h_rfm.Transform()[COL])
        st.pyplot(ww)


def rr(self):
       scaler = StandardScaler()
       scaler.fit(h_rfm.Transform())
       RFM_Table_scaled = scaler.transform(h_rfm.Transform())
       RFM_Table_scaled = pd.DataFrame(
       RFM_Table_scaled, columns=h_rfm.Transform().columns)
       XX = RFM_Table_scaled.iloc[:, 4:7].values
       XX = pd.DataFrame(
       XX, columns=['Monetary_T', 'Frequency_T', 'Recency_T'])
       
       return XX


def elbow(self):
        Within_Cluster_Sum_of_Square = []
        for i in range(1, 10, 1):
            km1 = KMeans(n_clusters=i, init='k-means++', random_state=50)
            km1.fit(h_rfm.rr())
            Within_Cluster_Sum_of_Square.append(km1.inertia_)
        zz = plt.figure(figsize=(15, 15))
        sns.set()
        plt.plot(range(1, 10, 1), (Within_Cluster_Sum_of_Square))
        plt.title('RFM Clustering: The Elbow Method')
        plt.ylabel('WCSS')
        plt.xlabel('Number of Clusters')
        st.pyplot(zz)


def Best_K(self):
        r = []
        sil = []
        for y in range(2, 10, 1):
            km1 = KMeans(n_clusters=y, init='k-means++', random_state=50)
            YY = km1.fit_predict(h_rfm.rr())
            XXX = h_rfm.rr()
            XXX['Clusters'] = km1.labels_
            XX = h_rfm.Transform()
            XX = XX.astype('object')
            XX['Clusters'] = km1.labels_
            score = silhouette_score(XX, km1.labels_, metric='euclidean')
            sil.append(score)
        return sil.index(max(sil)) + 2


def KM(self):
        km1 = KMeans(n_clusters=h_rfm.Best_K(),
                     init='k-means++', random_state=50)
        YY = km1.fit_predict(h_rfm.rr())
        XXX = h_rfm.rr()
        XXX['Clusters'] = km1.labels_
        XX = h_rfm.Transform()
        XX = XX.astype('object')
        XX['Clusters'] = km1.labels_
        return XX


def BOX(self):
        # Opt = ['Recency','Frequency','Monetary','Monetary_T','Frequency_T','Recency_T']
        st.sidebar.subheader("box plot")
        # add select widget
        N = st.sidebar.radio(label='SELECT FEATURE of Box Plot', options=(
            'Recency', 'Frequency', 'Monetary', 'Monetary_T', 'Frequency_T', 'Recency_T'), key='2f6gd5d45gd5')
        # N = st.sidebar.selectbox("Select Feature",Opt, key = '5')
        ee = plt.figure(figsize=(6, 2))
        sns.boxplot(x='Clusters', y=N, data=h_rfm.KM())
        st.pyplot(ee)

def scatter_Cluster(self):
        c = plt.figure(figsize=(20, 15))
        a = st.sidebar.radio(label='SELECT FEATURE For Clustering', options=(
            'Recency', 'Frequency', 'Monetary', 'Monetary_T', 'Frequency_T', 'Recency_T'), key='2f6gd5d455')
        b = st.sidebar.radio(label='SELECT FEATURE For  Clustering', options=(
            'Recency', 'Frequency', 'Monetary', 'Monetary_T', 'Frequency_T', 'Recency_T'), key='2f6gd5d4555gd5')
        plt.scatter(x=h_rfm.KM()[a], y=h_rfm.KM()[b], c=h_rfm.KM()[
                    'Clusters'], s=200, cmap='viridis', edgecolor='black')
        plt.grid(color='black', linewidth=0.5)

def Access_hybrid(self):
        CI = st.number_input('Enter a Customer ID', 0,
                             9000000, 0, 1, key='100')
        for i in range(len(Hybrid_Analysis().KM())):
            if h_rfm.KM().CustomerID[i] == CI:
                st.write('Clusters   :', h_rfm.KM().Clusters[i])
                st.write('Recency :', h_rfm.KM().Recency[i])
                st.write('Frequency:', h_rfm.KM().Frequency[i])
                st.write('Monetary:', h_rfm.KM().Monetary[i])