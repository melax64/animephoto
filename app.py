import numpy as np
import streamlit as st
from PIL import Image, UnidentifiedImageError

MAX_SIDE = 512
ALLOWED_TYPES = ["jpg", "jpeg", "png"]


def load_image(uploaded_file):
    """Buka file upload, validasi, ubah ke RGB, dan perkecil sisi terpanjang ke MAX_SIDE."""
    try:
        img = Image.open(uploaded_file)
        img.load()
    except (UnidentifiedImageError, OSError) as exc:
        raise ValueError("File bukan gambar yang valid.") from exc

    img = img.convert("RGB")
    img.thumbnail((MAX_SIDE, MAX_SIDE), Image.Resampling.LANCZOS)
    return img


def to_float_array(img):
    """Ubah gambar RGB ke array numpy float32 dengan rentang 0-1."""
    return np.asarray(img, dtype=np.float32) / 255.0


st.set_page_config(page_title="AnimeTale", layout="wide")
st.title("AnimeTale")
st.caption("Konversi gambar ke gaya anime dengan pengolahan citra digital terlebih dahulu.")

uploaded = st.file_uploader("Pilih gambar (JPG atau PNG)", type=ALLOWED_TYPES)

if uploaded is not None:
    try:
        img = load_image(uploaded)
    except ValueError as err:
        st.error(str(err))
        st.stop()

    arr = to_float_array(img)

    col_img, col_info = st.columns([2, 1])
    with col_img:
        st.image(img, caption="Gambar asli (sudah diperkecil)", width=320)
    # with col_info:
    #     st.subheader("Informasi array")
    #     st.write(f"Ukuran: {img.width} x {img.height} px")
    #     st.write(f"Shape numpy: {arr.shape}")
    #     st.write(f"Tipe data: {arr.dtype}")
    #     st.write(f"Nilai min-max: {arr.min():.3f} - {arr.max():.3f}")
