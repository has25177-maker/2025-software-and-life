import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------
# 데이터 불러오기
# ----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

st.title("🌍 국가별 MBTI 비율 시각화 대시보드")
st.write("국가를 선택하면 각 MBTI 유형의 비율을 인터랙티브 그래프로 확인할 수 있어요.")

# ----------------------
# 국가 선택
# ----------------------
country = st.selectbox("국가를 선택하세요", df["Country"].unique())

country_data = df[df["Country"] == country].iloc[0]

# MBTI 타입과 값 분리
mbti_types = df.columns[1:]
values = [country_data[col] for col in mbti_types]

# 데이터프레임 변환
plot_df = pd.DataFrame({
    "MBTI": mbti_types,
    "Value": values
})

# ----------------------
# 색상 설정: 1등 빨간색, 나머지는 그라데이션
# ----------------------
plot_df = plot_df.sort_values(by="Value", ascending=False)
max_value = plot_df.iloc[0]["Value"]

colors = []
for v in plot_df["Value"]:
    if v == max_value:
        colors.append("red")     # 1등 빨간색
    else:
        # 값 비율에 따라 밝은 파란색 ~ 진한 파란색 그라데이션
        ratio = v / max_value
        blue_intensity = int(255 * ratio)
        colors.append(f"rgb(0, {blue_intensity}, 255)")

# ----------------------
# Plotly 막대 그래프
# ----------------------
fig = px.bar(
    plot_df,
    x="MBTI",
    y="Value",
    title=f"📊 {country} MBTI 비율",
    color=plot_df["MBTI"],
    color_discrete_sequence=colors
)

fig.update_layout(
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)
