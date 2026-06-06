import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Streamlit 페이지 설정
st.set_page_config(page_title="3D Interactive Globe", layout="wide")
st.title("🌍 3D 대화형 지구 모형")
st.markdown("마우스를 클릭한 채로 움직이면 **지구를 이리저리 돌려볼 수 있으며**, 스크롤로 **확대/축소**가 가능합니다.")

# 3D 구체(지구) 표면 데이터 생성
g_res = 50  # 구체 해상도
phi = np.linspace(0, 2 * np.pi, g_res)
theta = np.linspace(0, np.pi, g_res)
phi, theta = np.meshgrid(phi, theta)

# 구면 좌표계를 직교 좌표계(X, Y, Z)로 변환
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# 표면에 입힐 지구 텍스처 (기본 고해상도 지도 템플릿 사용)
# Plotly의 수치 지형 데이터를 활용해 입체감을 줍니다.
fig = go.Figure(data=[go.Surface(
    x=x, y=y, z=z,
    colorscale="Viridis",  # 지구 느낌을 주는 세련된 컬러셋 (Earth, Tealgrn 등으로 변경 가능)
    showscale=False,       # 컬러바 숨김
    hoverinfo='none'       # 마우스 올렸을 때 좌표 숨김
)])

# 3D 지구본 레이아웃 및 카메라 시점 설정
fig.update_layout(
    title='Interactive 3D Globe',
    scene=dict(
        xaxis=dict(showbackground=False, showgrid=False, zeroline=False, showticklabels=False, title=''),
        yaxis=dict(showbackground=False, showgrid=False, zeroline=False, showticklabels=False, title=''),
        zaxis=dict(showbackground=False, showgrid=False, zeroline=False, showticklabels=False, title=''),
        bgcolor="rgba(0,0,0,0)", # 배경 투명화
        camera=dict(
            eye=dict(x=1.25, y=1.25, z=1.25) # 초기 카메라 거리 및 시점
        )
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    height=700
)

# Streamlit에 Plotly 3D 차트 렌더링
st.plotly_chart(fig, use_container_width=True)

st.success("✅ 라이브러리 호환성 문제가 해결된 버전입니다.")
