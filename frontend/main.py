import streamlit as st
import sys
import os

# --- Cấu hình đường dẫn ---
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

import api_cilent  # Giữ nguyên tên module của bạn

@st.cache_data(ttl=600)
def get_all_movie_names():
    return api_cilent.get_all_name()

st.title('Movie Recommendation System')

if 'info_movies' not in st.session_state:
    st.session_state.info_movies = []

if 'page' not in st.session_state:
    st.session_state.page = 1

if 'your_movie' not in st.session_state:
    st.session_state.your_movie = None

IMAGES_PER_PAGE = 5


# ======================
# HELPER FUNCTIONS (CALLBACKS)
# ======================
# Các hàm này sẽ chạy TRƯỚC khi giao diện được vẽ lại
def next_page():
    st.session_state.page += 1


def prev_page():
    st.session_state.page -= 1


def reset_page():
    st.session_state.page = 1


# ======================
# SEARCH
# ======================

name = st.selectbox('Search', options=get_all_movie_names())




# Thêm on_click=reset_page để đảm bảo tìm phim mới là về trang 1 ngay
if st.button('Recommend', on_click=reset_page):
    info_search = api_cilent.get_info(name)
    st.session_state.your_movie = info_search
    recommended_movies = api_cilent.recommend(name, limit=13)
    st.session_state.info_movies = [api_cilent.get_movie_image(movie) for movie in recommended_movies]

if st.session_state.your_movie:
    st.subheader('You are watching:')
    st.image(st.session_state.your_movie['image_url'], width=200)
    st.markdown(f"**{st.session_state.your_movie['name']}**")
    st.caption(f"Genres: {st.session_state.your_movie['genres']}")

# ======================
# DISPLAY LOGIC
# ======================
movies = st.session_state.info_movies
total_images = len(movies)

if total_images > 0:
    # Tính tổng số trang
    st.subheader('Recommendation')
    total_pages = (total_images - 1) // IMAGES_PER_PAGE + 1

    # Kiểm tra an toàn: Nếu đang ở trang 3 mà list mới chỉ có 1 trang -> Reset về trang 1
    if st.session_state.page > total_pages:
        st.session_state.page = 1

    start = (st.session_state.page - 1) * IMAGES_PER_PAGE
    end = start + IMAGES_PER_PAGE

    # Hiển thị số trang
    st.subheader(f"Page {st.session_state.page} / {total_pages}")

    # Hiển thị ảnh
    cols = st.columns(IMAGES_PER_PAGE)

    # Dùng zip để loop an toàn (tránh lỗi nếu trang cuối ít hơn 5 ảnh)
    for col, movie, i in zip(cols, movies[start:end], range(start, end + 1)):
        with col:
            st.image(movies[i]['image_url'], use_container_width=True)
            st.markdown(f"**{movies[i]['name']}**")
            st.caption(f"Genres: {movies[i]['genres']}")

            # ======================
    # PAGE CONTROLS
    # ======================
    st.write("---")  # Kẻ ngang phân cách
    col1, col2, col3 = st.columns([1, 8, 1])

    with col1:
        # Dùng on_click thay vì if st.button: logic
        st.button("⬅ Prev",
                  disabled=(st.session_state.page == 1),
                  on_click=prev_page)

    with col3:
        # Dùng on_click thay vì if st.button: logic
        st.button("Next ➡",
                  disabled=(st.session_state.page == total_pages),
                  on_click=next_page)


