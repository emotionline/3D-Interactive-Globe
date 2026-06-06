import streamlit as st
import pydeck as pdk

# Streamlit 페이지 설정
st.set_page_config(page_title="3D Interactive Globe", layout="wide")

st.title("🌍 3D 대화형 지구 모형")
st.markdown("마우스 왼쪽 버튼을 클릭한 채로 드래그하면 **지구를 회전**할 수 있고, 스크롤을 통해 **확대/축소**가 가능합니다.")

# Pydeck의 3D 지구본(Globe) 뷰 설정
view_state = pdk.ViewState(
    latitude=37.5665,   # 초기 중심 위도 (서울 기준)
    longitude=126.9780, # 초기 중심 경도
    zoom=1,             # 초기 줌 레벨 (지구 전체가 보이도록 낮게 설정)
    min_zoom=0,
    max_zoom=15,
    pitch=0,
    bearing=0
)

# 지구본의 배경 및 레이어 스타일 설정 (기본 위성/지도 레이어 사용)
r = pdk.Deck(
    views=[pdk.View(type="GlobeView", controller=True)], # GlobeView를 설정해야 3D 구체로 표현됩니다.
    initial_view_state=view_state,
    map_style="mapbox://styles/mapbox/satellite-v9", # 위성 지도로 설정 (원하는 스타일로 변경 가능)
    # 특별한 데이터 포인트(핀, 바 차트 등)를 시각화하고 싶다면 여기에 layers=[...]를 추가합니다.
    layers=[] 
)

# Streamlit에 Pydeck 차트 렌더링
st.pydeck_chart(r)

# 추가 제어 단추나 설명 피드
st.info("💡 오른쪽 마우스 버튼을 누른 채 드래그하면 시점의 각도(Pitch/Bearing)도 조절할 수 있습니다.")
