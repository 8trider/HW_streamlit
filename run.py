import streamlit as st
st.title("올라운더 러닝화 3")
st.divider()
st.subheader("운동화말고 러닝화를 신어보아요!")

st.write("""
여러가지 이유가 있지만 우선 모두의 관절을 위해 달릴 때는 러닝화를 신어야 합니다.

러닝화엔 쿠션화, 중립화, 레이싱화 등 여러 종류가 있지만, 

본 페이지에선 조깅, 템포런, 10km, 하프(20km)에 두루 아우르는 올라운더 러닝화를 소개합니다.
""")
st.divider()

tab_menus = ["나이키", "써코니", "푸마"]
tab1, tab2, tab3 = st.tabs(tab_menus)
tab1.image("img/n1.png")
tab1.write("""
**리액트 인피니티 3**

* 어퍼 : 엔지니어드 메쉬
* 미드솔 : 리액트 폼
* 아웃솔 : 러버솔. 내구성 보통
* 무게 약 270g
* 특징 
    * 칼발이 아니면 신기 어렵다
    * 아울렛 세일가로 싸게 구할수 있다
    * 온라인상엔 짝퉁이 많다
    * 나이키의 브랜드 파워
""")
tab2.image("img/s1.png")
tab2.write("""
**엔돌핀 스피드 3**

* 어퍼 : 엔지니어드 메쉬
* 미드솔 : PWRRUN PEVA 폼
* 아웃솔 : 카본러버솔. 내구성 좋음
* 무게 약 230g
* 특징 : 
    * 미드솔 중간에 나일론 플레이트 탑재
    * 에이비씨마트 외엔 해외 직구로만 구할 수 있다
    * 아마존 세일로 싸게 구할 수 있다
    * 런닝화 외길인생 100년의 기술력
    * 기능에 치중한 나머지 디자인은 구리다
""")
tab3.image("img/p1.png")
tab3.write("""
**디비에이트 나이트로 2**

* 어퍼 : 엔지니어드 메쉬
* 미드솔 : 나이트로 엘리트 폼
* 아웃솔 : 푸마그립. 내구성과 접지력 좋음
* 무게 약 270g
* 특징 : 
    * 미드솔 중간에 카본 플레이트 탑재 
    * 독일 브랜드라서 미국에선 구하기 힘들다
    * 러닝화 브랜드 파워가 다소 약하다
    * 그 덕분에 나이키보다 기능성 대비 가격이 싸다
""")

st.divider()
col1, col2, col3 = st.columns(3)
r = col1.radio("그래서 뭘 신어볼까요?", ["나이키", "써코니", "푸마"])

if r == "나이키":
        st.write("발볼이 넓으면 신지마세요, 쳐다도 보지 마세요")
elif r == "써코니":
        st.write("디자인 상관없이 기능성만 보신다면 추천합니다")
elif r == "푸마":
        st.write("디자인도 좋고, 기능성도 좋고, 오래 신고 싶으면 아주 추천합니다")