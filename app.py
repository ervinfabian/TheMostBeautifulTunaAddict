import streamlit as st
import cv2
import numpy as np

st.title("A világ legszebb tonhal függőjenek !!!")

# image = cv2.imread("reka.jpeg")

# # file_bytes = np.asarray(image, dtype=np.uint8)
# file_bytes = np.asarray(image)



# opencv_image = cv2.imdecode(file_bytes, 1)

# Now do something with the image! For example, let's display it:
st.image("reka.jpeg")


amount_tuna = st.number_input("Kérjük adja meg a héten elfogyasztásra szánt tonhal mennyiségét grammban!")

bodyweight = st.number_input("Kérjük adja meg a testtömegét kg-ban!")

healthy_amount_of_mercury_for_Reka = bodyweight * 0.1

amount_of_mercury_in_1g_tuna = 1.2

if (amount_tuna != 0) and (bodyweight != 0):
    if (amount_tuna * amount_of_mercury_in_1g_tuna) < healthy_amount_of_mercury_for_Reka * 7:
        st.write("Bátran elfogyaszthatja az összes tervezett tonhal mennyiséget!")
    else:
        st.write("Kérjük fogyasszon lehetőleg kevesebb tonhalat a héten, hogy tövább gyönyörködhessünk Önben!")