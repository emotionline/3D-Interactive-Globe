import streamlit as st
import pydeck as pdk

# 제공해주신 Mapbox 토큰을 연동합니다.
MAPBOX_API_KEY = "pk.eyJ1IjoiZW1vdGlvbmxpbmUiLCJhIjoiY21xMnA0aXkyMWJlbzJycHUxZmRlZWE0bCJ9.hV3ue5ZrVqdsOUkcBY1Tgg"

# Streamlit 레이아웃 설정
st.set_page_config(page_title="3D Interactive Globe", layout="wide")

st.title("🌍 3D 대화형 지구 모형")
st.markdown("마우스 왼쪽 버튼을 드래그하여 **지구를 회전**하고, 스크롤로 **확대/축소**해 보세요.")

# 3D 지구본의 초기 시점 및 렌더링 범위 설정
view_state = pdk.ViewState(
    latitude=37.5665,   # 초기 중심 위도 (서울)
    longitude=126.9780, # 초기 중심 경도
    zoom=1,             # 전체 지구가 한눈에 들어오는 줌 레벨
    min_zoom=0,
    max_zoom=15,
    pitch=0,
    bearing=0
)

# Pydeck Deck 설정 (GlobeView 엔진 활성화)
r = pdk.Deck(
    views=[pdk.View(type="GlobeView", controller=True)],
    initial_view_state=view_state,
    map_style="mapbox://styles/mapbox/satellite-v9", # 위성 지도 스타일
    mapbox_key=MAPBOX_API_KEY,                       # 토큰 주입
    layers=[]
)

# Streamlit에 3D 지구 렌더링
st.pydeck_chart(r)

st.info("💡 오른쪽 마우스 버튼을 누른 채 드래그하면 시점 각도(Pitch)를 입체적으로 조절할 수 있습니다.")
