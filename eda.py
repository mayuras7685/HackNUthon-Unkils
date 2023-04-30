import streamlit as st
import pandas as pd
import numpy as np
import codecs
from streamlit.components.v1 import components


dff = pd.read_csv("Input file")

# sweetiz visualizations to kickstart EDA
def st_display_sweetiz(report_html, width=1000, height=500):
        report_file = codecs.open(report_html, 'r')
        page = report_file.read()
        components.html(page, width=width, height=height, scrolling=True)
        HtmlFile = open("test.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        print(source_code)
        components.html(source_code)

def SweetV(self, x):
        st.subheader('SweetVIZ Data Analysis Report')
        analysis = sv.analyze([x, 'EDA'])
        # analysis.show_html()
        analysis.show_html(filepath='./SWEETVIZ_REPORT.html',
                           open_browser=False, layout='vertical', scale=1.0)
        
        HtmlFile = open("SWEETVIZ_REPORT.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        print(source_code)
        components.html(source_code, height=2000)

def Exp1(self):
        with st.expander('See About SweetViz'):
            st.write(''' Sweetviz is a wonderful and very useful Python library that provides us with the EDA of a given dataset. Sweetviz let us perform a list of different analyses
          Single Dataset Analysis , Target Variable Analysis , Compare two datasets, Divide Dataset using boolean variable and Compare them.''')

def Map(self):
        dict = {'lat': [], 'lon': []}
        latlong = pd.DataFrame(dict)
        # coords = np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4]
        # df = pd.DataFrame(coords, columns=["lat", "lon"])
        # numpy.random.randn(1) / [50, 50] + [37.76, -122.4]
        for i in range(0, len(dff)):
            if dff.Country[i] == 'United Kingdom':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [55.9, -4.75]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [55.9, -4.75]

            elif dff.Country[i] == 'Germany':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [49.982, 8.27]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [49.982, 8.27]

            elif dff.Country[i] == 'France':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [45.89, 6.116]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [45.89, 6.116]

            elif dff.Country[i] == 'Sweden':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [60.613, 15.60]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [60.613, 15.60]

            elif dff.Country[i] == 'Finland':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [60.996, 24.4999]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [60.996, 24.4999]

            elif dff.Country[i] == 'EIRE':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [53.633, -8.183]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [53.633, -8.183]

            elif dff.Country[i] == 'Switzerland':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [47.3697, 7.349]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [47.3697, 7.349]

            elif dff.Country[i] == 'Greece':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [38.8989, 22.43458]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [38.8989, 22.43458]

            elif dff.Country[i] == 'Denmark':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [55.7090, 9.53449]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [55.7090, 9.53449]

            elif dff.Country[i] == 'Malta':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [35.937, 14.375]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [35.937, 14.375]

            elif dff.Country[i] == 'Australia':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [-33.420, 151.3004]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [-33.420, 151.3004]

            elif dff.Country[i] == 'Spain':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [38.912, 6.337]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [38.912, 6.337]

            elif dff.Country[i] == 'Belgium':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [50.445, 3.9390]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [50.445, 3.9390]

            elif dff.Country[i] == 'Netherlands':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [53.00, 6.5500]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [53.00, 6.5500]

            elif dff.Country[i] == 'Bahrain':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [26.066, 50.557]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [26.066, 50.557]

            elif dff.Country[i] == 'Denmark':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [55.709, 9.5344]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [55.709, 9.5344]

            elif dff.Country[i] == 'Portugal':
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [40.641, -8.657]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [40.641, -8.657]

            else:
                latlong.loc[len(latlong)] = np.random.randn(
                    1) / [50, 50] + [15.491, 73.815]
                latlong.loc[len(latlong)] = np.random.randn(
                    2) / [50, 50] + [15.491, 73.815]

        st.map(latlong)