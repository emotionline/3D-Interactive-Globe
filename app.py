import streamlit as st
from streamlit_folium import st_folium  # 호환성이 완벽한 라이브러리로 변경
import folium

# Streamlit 페이지 설정
st.set_page_config(page_title="고해상도 3D 인터랙티브 지도", layout="wide")
st.title("🗺️ 고해상도 줌인 대화형 지도 (내 위치 중심)")
st.markdown("마우스 스크롤로 확대(Zoom-in)해 보세요! **확대할 때마다 실시간으로 더 세밀하고 선명한 고화질 위성 지도**가 로드됩니다.")

# 1. 지도 초기화 (성남시 분당구 판교동 중심 좌표: 37.401, 127.098)
m = folium.Map(
    location=[37.401, 127.098], 
    zoom_start=16, 
    max_zoom=20, # 최대 20단계까지 줌인 가능
    control_scale=True
)

# 2. 전 세계 오픈 고해상도 위성 지도 레이어(Esri Satellite) 추가
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri',
    name='Esri Satellite',
    overlay=False,
    control=True
).add_to(m)

# 3. 일반 도로망/건물명 레이어 레이블 추가 (위성 지도 위에 겹침)
folium.TileLayer(
    tiles='https://{s}.basemaps.cartocdn.com/dark_only_labels/{z}/{x}/{y}{r}.png',
    attr='CartoDB',
    name='Labels',
    overlay=True,
    control=True
).add_to(m)

# 4. 내 위치(판교)에 마커 꽂기
folium.Marker(
    location=[37.401, 127.098],
    popup="내 위치 (Pangyo)",
    tooltip="여기에 계십니다!",
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)

# 5. 호환성이 뛰어난 st_folium 컴포넌트로 지도 렌더링
st_folium(m, width="100%", height=700, jumping_style=True)

st.info("💡 오른쪽 상단의 레이어 메뉴를 이용하거나, 마우스 스크롤을 끝까지 당겨 판교원마을 건물의 형태와 도로 상세 정보까지 확인해 보세요!")
