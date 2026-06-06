import streamlit as st
import streamlit.components.v1 as components
from pyecharts import options as opts
from pyecharts.charts import MapGlobe

# Streamlit 페이지 설정
st.set_page_config(page_title="3D Interactive Globe", layout="wide")
st.title("🌍 3D 대화형 진짜 지구 모형")
st.markdown("마우스 왼쪽 버튼으로 **지구를 잡고 이리저리 돌려볼 수 있으며**, 스크롤로 **확대/축소**가 가능합니다.")

# 3D 지구본 컴포넌트 생성 (pyecharts 활용)
# 별도의 토큰 없이 실제 세계 지도 데이터가 구체에 매핑됩니다.
globe = (
    MapGlobe()
    .add_schema(
        maptype="world",
        itemstyle_opts=opts.ItemStyleOpts(
            color="#2e5c8a",          # 대륙 색상
            border_color="#111",      # 국경선 색상
        ),
        background_color="#0f172a"    # 우주 배경 색상 (다크 모드)
    )
    .add(
        series_name="",
        data_pair=[],
        is_map_symbol_show=False,
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="진짜 지구 모형 (3D Globe)", pos_left="center", title_textstyle_opts=opts.TextStyleOpts(color="#fff")),
        visualmap_opts=opts.VisualMapOpts(is_show=False),
    )
)

# Streamlit 환경에서 html로 렌더링하기 위해 차트 빌드
globe.render("globe.html")

# 생성된 HTML 파일을 읽어서 Streamlit 화면에 주입
with open("globe.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# 화면에 3D 지구본 표시 (너비와 높이 조절 가능)
components.html(html_data, height=750, scrolling=False)

st.info("💡 마우스 드래그를 통해 대륙과 바다의 위치를 구석구석 돌려가며 확인해 보세요!")
