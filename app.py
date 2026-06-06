import streamlit as st
import pydeck as pdk

# 복사한 Mapbox 토큰을 여기에 붙여넣습니다.
MAPBOX_API_KEY = "pk.eyJ1IjoiZW1vdGlvbmxpbmUiLCJhIjoiY21xMnA0aXkyMWJlbzJycHUxZmRlZWE0bCJ9.hV3ue5ZrVqdsOUkcBY1Tgg"

st.set_page_config(page_title="3D Interactive Globe", layout="wide")
st.title("🌍 3D 대화형 지구 모형")

view_state = pdk.ViewState(
    latitude=37.5665, longitude=126.9780, zoom=1, min_zoom=0, max_zoom=15
)

# pdk.Deck 안에 mapbox_key를 반드시 지정해줍니다.
r = pdk.Deck(
    views=[pdk.View(type="GlobeView", controller=True)],
    initial_view_state=view_state,
    map_style="mapbox://styles/mapbox/satellite-v9",
    mapbox_key=MAPBOX_API_KEY, # ⭐ 이 부분이 핵심입니다!
    layers=[]
)

st.pydeck_chart(r)
