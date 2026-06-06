import streamlit as st
import streamlit.components.v1 as components

# Streamlit 페이지 설정
st.set_page_config(page_title="3D Interactive Globe", layout="wide")
st.title("🌍 3D 대화형 진짜 지구 모형")
st.markdown("마우스 왼쪽 버튼으로 **지구를 잡고 이리저리 돌려볼 수 있으며**, 스크롤로 **확대/축소**가 가능합니다.")

# CDN을 통해 Globe.gl 라이브러리를 불러오고 실제 지구 이미지를 매핑하는 콤팩트한 HTML/JS 코드
html_code = """
<!DOCTYPE html>
<html>
<head>
  <style> body { margin: 0; background-color: #0f172a; overflow: hidden; } </style>
  <script src="//unpkg.com/globe.gl"></script>
</head>
<body>
  <div id="globeViz"></div>

  <script>
    const myGlobe = Globe()
      (document.getElementById('globeViz'))
      // 실제 지구의 대륙과 바다가 표현된 전용 텍스처 이미지를 입힙니다.
      .globeImageUrl('//unpkg.com/three-globe/example/img/earth-blue-marble.jpg')
      // 입체감을 위한 지형 밤 비주얼 스타일 추가 (선택사항)
      .bumpImageUrl('//unpkg.com/three-globe/example/img/earth-topology.png')
      .width(window.innerWidth)
      .height(window.innerHeight - 50);

    // 창 크기가 바뀔 때 지구본 크기도 자동으로 조절되도록 설정
    window.addEventListener('resize', () => {
      myGlobe.width(window.innerWidth).height(window.innerHeight - 50);
    });
  </script>
</body>
</html>
"""

# Streamlit의 components 기능을 이용해 렌더링 (가장 안전하고 오류 없음)
components.html(html_code, height=750, scrolling=False)

st.info("💡 마우스 드래그를 통해 실제 대륙과 바다의 위치를 구석구석 돌려가며 확인해 보세요!")
