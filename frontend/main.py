import streamlit as st
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

import api_cilent

st.title('Movie Recommendation System')



# ======================
# INIT SESSION STATE
# ======================
if 'images' not in st.session_state:
    st.session_state.images = []

if 'page' not in st.session_state:
    st.session_state.page = 1

IMAGES_PER_PAGE = 5

# ======================
# SEARCH
# ======================
name = st.selectbox('Search', options=api_cilent.get_name_movies())

if st.button('Recommend'):

    recommended_movies = api_cilent.recommend(name, limit=13)
    st.session_state.images = [api_cilent.get_movie_image(movie) for movie in recommended_movies]
    st.session_state.page = 1  # reset page

images = st.session_state.images
total_images = len(images)

if total_images > 0:
    total_pages = (total_images - 1) // IMAGES_PER_PAGE + 1

    start = (st.session_state.page - 1) * IMAGES_PER_PAGE
    end = start + IMAGES_PER_PAGE

    st.subheader(f"Page {st.session_state.page} / {total_pages}")

    cols = st.columns(IMAGES_PER_PAGE)

    for col, img_url in zip(cols, images[start:end]):
        col.image(img_url, use_container_width=True)

    # ======================
    # PAGE CONTROLS
    # ======================
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅ Prev", disabled=st.session_state.page == 1):
            st.session_state.page -= 1

    with col3:
        if st.button("Next ➡", disabled=st.session_state.page == total_pages):
            st.session_state.page += 1