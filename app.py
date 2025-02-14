import streamlit as st
import cv2
import numpy as np

st.title("A vilag legszebb tonhal fuggojenek weboldala!!!")

# image = cv2.imread("reka.jpeg")

# # file_bytes = np.asarray(image, dtype=np.uint8)
# file_bytes = np.asarray(image)



# opencv_image = cv2.imdecode(file_bytes, 1)

# Now do something with the image! For example, let's display it:
st.image("reka.jpeg")

# st.write("Kerjuk adja meg a heten elfogyasztasra szant tonhal mennyiseget mg-ban!")

amount_tuna = st.number_input("Kerjuk adja meg a heten elfogyasztasra szant tonhal mennyiseget g-ban!")

bodyweight = st.number_input("Kerjuk adja meg testomeget kg-ban!")

healthy_amount_of_mercury_for_Reka = bodyweight * 0.1

amount_of_mercury_in_1g_tuna = 1.2

if (amount_tuna != 0) and (bodyweight != 0):
    if (amount_tuna * amount_of_mercury_in_1g_tuna) < healthy_amount_of_mercury_for_Reka * 7:
        st.write("Batran elfogyaszthatja az osszes tervezett tonhalat!")
    else:
        st.write("Kerjuk fogyasszon lehetoleg kevesebb tonhalat a heten, hogy tovabb gyonyorkodhessunk Onben!")