# main.py
import streamlit as st
from crawler import WebCrawler

st.set_page_config(page_title="Image Search", layout="wide")

st.markdown("""
    <style>
    .gallery-img {
        border-radius: 10px;
        transition: transform 0.3s;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .gallery-img:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔍 Image Search")

crawler = WebCrawler()

# Search bar
keyword = st.text_input("Enter a keyword to search for images", value="", help="Type any word like 'cats', 'sunset', etc.")
search_btn = st.button("Search")

if search_btn and keyword:
    with st.spinner("Searching for images..."):
        images = crawler.search_images(keyword)
        if images and isinstance(images[0], str) and images[0].startswith("Error"):
            st.error(images[0])
        elif not images or images[0] == "No images found.":
            st.warning(f"No images found for '{keyword}'.")
        else:
            st.success(f"Found {len(images)} images for '{keyword}'")
            # Paginate results
            images_per_page = 10
            page = st.number_input("Page", min_value=1, max_value=(len(images) - 1) // images_per_page + 1, step=1)
            start_idx = (page - 1) * images_per_page
            end_idx = start_idx + images_per_page

            cols = st.columns(5)
            for i, img_url in enumerate(images[start_idx:end_idx]):
                with cols[i % 5]:
                    st.image(img_url, use_column_width=True, caption=f"Image {start_idx + i + 1}")
elif search_btn and not keyword:
    st.warning("Please enter a keyword.")
