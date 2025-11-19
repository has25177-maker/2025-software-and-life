import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="베스킨라빈스 키오스크",
    page_icon="🍨",
    layout="centered",
)

def main():
    # 헤더 영역
    st.markdown(
        """
        <h1 style="text-align:center; color:#ff4b6e;">
            🍦 베스킨라빈스 키오스크
        </h1>
        <p style="text-align:center; font-size:18px;">
            안녕하세요! 상큼 달콤한 아이스크림 주문을 도와드릴게요 😊
        </p>
        <hr>
        """,
        unsafe_allow_html=True
    )

    # 1. 매장 / 포장 선택
    st.subheader("1️⃣ 어디에서 드시나요?")
    eat_type = st.radio(
        "이용 방식을 골라주세요 😄",
        ["매장에서 먹고 갈게요 🪑", "포장해서 가져갈게요 🛍️"],
        horizontal=True
    )

    # 2. 용기 선택
    st.subheader("2️⃣ 어떤 용기를 선택할까요?")
    st.caption("용기에 따라서 선택할 수 있는 아이스크림 맛 개수가 달라져요!")

    container_options = {
        "싱글 레귤러 (1스쿱) 🍧": {"scoops": 1, "price": 3700},
        "더블 레귤러 (2스쿱) 🍨": {"scoops": 2, "price": 6700},
        "파인트 (3스쿱) 🥄": {"scoops": 3, "price": 8200},
        "쿼터 (4스쿱) 🎉": {"scoops": 4, "price": 15500},
    }

    container_name = st.selectbox(
        "용기를 골라주세요 👇",
        list(container_options.keys())
    )

    max_scoops = container_options[container_name]["scoops"]
    base_price = container_options[container_name]["price"]

    # 3. 맛 선택 (이하 값으로)
    st.subheader("3️⃣ 아이스크림 맛을 골라주세요!")
    st.caption(f"최대 **{max_scoops}가지 맛**까지 선택 가능해요 🍦")

    flavors = [
        "엄마는 외계인 👽🍫",
        "민트 초코칩 🌿🍫",
        "슈팅스타 💫",
        "바람과 함께 사라지다 🌬️",
        "레인보우 샤베트 🌈",
        "뚱바 아이스크림 🍫🍦",
        "체리쥬빌레 🍒",
        "뉴욕 치즈케이크 🧀",
        "오레오 쿠키앤크림🍪",
        "피스타치오 아몬드 🌰"
    ]

    selected_flavors = st.multiselect(
        "원하시는 맛을 골라주세요 😋",
        flavors,
        help=f"최대 {max_scoops}가지까지 선택할 수 있어요!"
    )

    # 개수 검증
    flavor_count = len(selected_flavors)
    if flavor_count == 0:
        st.info("아이스크림 맛을 한 가지 이상 골라주세요 😉")
    elif flavor_count > max_scoops:
        st.error(f"⚠️ {max_scoops}가지까지만 선택할 수 있어요! (현재 {flavor_count}가지 선택됨)")

    # 4. 결제 수단 선택
    st.subheader("4️⃣ 결제 방법을 선택해주세요 💳")
    pay_method = st.radio(
        "어떻게 결제하시겠어요?",
        ["현금 결제 💵", "카드 결제 💳"],
        horizontal=True
    )

    # 5. 최종 가격 및 주문 확인
    st.subheader("5️⃣ 주문 내용 확인하기 ✅")

    # 버튼 비활성화 조건
    button_disabled = (
        flavor_count == 0 or
        flavor_count > max_scoops
    )

    with st.container():
        st.markdown(
            """
            <div style="
                border-radius: 15px;
                padding: 15px;
                border: 1px solid #ffd1dc;
                background-color: #fff6f8;
            ">
            """,
            unsafe_allow_html=True
        )

        st.markdown("### 🧾 주문 요약")
        st.write(f"- 이용 방식: **{eat_type}**")
        st.write(f"- 용기: **{container_name}**")
        st.write(f"- 선택한 맛 ({flavor_count} / {max_scoops}):")

        if selected_flavors:
            for f in selected_flavors:
                st.write(f"  • {f}")
        else:
            st.write("  • (아직 선택된 맛이 없어요)")

        st.write(f"- 결제 방법: **{pay_method}**")
        st.write(f"### 💰 최종 결제 금액: **{base_price:,}원**")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    confirm = st.button(
        "✨ 주문 확정하기 ✨",
        disabled=button_disabled
    )

    if confirm:
        st.success("주문이 완료되었어요! 🍨 감사합니다, 맛있게 드세요 😆")
        st.balloons()

        st.markdown(
            """
            <p style="text-align:center; font-size:16px;">
                잠시 후 직원에게 이 화면을 보여주세요 🙌
            </p>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
