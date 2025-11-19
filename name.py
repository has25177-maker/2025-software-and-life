import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="베스킨라빈스 키오스크",
    page_icon="🍨",
    layout="centered",
)

# 간단한 CSS로 전체 톤 꾸미기
st.markdown(
    """
    <style>
    body {
        background: #fff7fb;
    }
    .main {
        background: linear-gradient(180deg, #fff7fb 0%, #ffffff 40%);
    }
    .br-card {
        border-radius: 18px;
        padding: 18px 20px;
        border: 1px solid #ffd9e8;
        background-color: #ffffffee;
        box-shadow: 0 6px 16px rgba(255, 158, 194, 0.18);
    }
    .br-tag {
        display: inline-block;
        padding: 2px 10px;
        border-radius: 999px;
        font-size: 11px;
        background-color: #ffe4f1;
        color: #ff4b6e;
        margin-bottom: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    # 헤더
    st.markdown(
        """
        <h1 style="text-align:center; color:#ff4b6e; margin-bottom:6px;">
            🍦 베스킨라빈스 아이스크림 키오스크
        </h1>
        <p style="text-align:center; font-size:16px; color:#555;">
            오늘도 달콤한 하루 준비되셨나요? 주문을 도와드릴게요 😊
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")

    # ─────────────────────────────────────────────
    # 0. 기본 메뉴 / 가격 정보 (실제 매장 기준)
    # ─────────────────────────────────────────────
    # 가격은 2024년 기준 온라인 메뉴 가격 참고 (매장별 상이 가능)
    menu_items = {
        # CONE & CUP (1~2스쿱)
        "싱글레귤러 (콘/컵 · 1스쿱) 🍧": {
            "category": "CONE & CUP",
            "scoops": 1,
            "price": 3500,
            "desc": "한 가지 맛을 센스 있게 즐기는 기본 사이즈 (중량 약 115g)",
        },
        "싱글킹 (콘/컵 · 1스쿱, 대) 👑": {
            "category": "CONE & CUP",
            "scoops": 1,
            "price": 4300,
            "desc": "좋아하는 맛 하나를 듬뿍 즐기는 사이즈 (중량 약 145g)",
        },
        "더블주니어 (콘/컵 · 2스쿱) 💕": {
            "category": "CONE & CUP",
            "scoops": 2,
            "price": 4700,
            "desc": "두 가지 맛을 조금씩 한 번에! (중량 약 150g)",
        },
        "더블레귤러 (콘/컵 · 2스쿱, 대) 🍨🍨": {
            "category": "CONE & CUP",
            "scoops": 2,
            "price": 6700,
            "desc": "아이스크림 마니아를 위한 든든한 더블 사이즈 (중량 약 230g)",
        },
        # HAND PACK (3~6스쿱)
        "파인트 (3스쿱) 🥄": {
            "category": "HAND PACK",
            "scoops": 3,
            "price": 8900,
            "desc": "3가지 맛을 골라먹는 재미가 있는 사이즈 (중량 약 320g)",
        },
        "쿼터 (4스쿱) 🎉": {
            "category": "HAND PACK",
            "scoops": 4,
            "price": 17000,
            "desc": "4가지 맛을 골고루 즐기는 기본 패밀리 사이즈 (중량 약 620g)",
        },
        "패밀리 (5스쿱) 👨‍👩‍👧‍👦": {
            "category": "HAND PACK",
            "scoops": 5,
            "price": 24000,
            "desc": "가족, 친구들과 나눠먹기 좋은 사이즈 (중량 약 960g)",
        },
        "하프갤런 (6스쿱) 🍼": {
            "category": "HAND PACK",
            "scoops": 6,
            "price": 29000,
            "desc": "파티용 대용량! 6가지 맛을 넉넉하게 (중량 약 1,200g)",
        },
    }

    # 대표 맛 리스트 (실제 배라 상시 메뉴 기준, 일부만 예시)
    flavors = [
        "엄마는 외계인 👽",
        "소금우유 아이스크림🧂",
        "슈팅스타 💫",
        "민트 초코칩 🌿🍫",
        "체리쥬빌레 🍒",
        "뉴욕 치즈케이크 🧀",
        "레인보우 샤베트 🌈",
        "베리베리 스트로베리 🍓",
        "바람과 함께 사라지다 🌪️",
        "오레오 쿠키앤크림 🍪",
        "피스타치오 아몬드 🌰",
        "초코나무 숲 🌳🍫",
        "초콜릿 무스 🍫",
        "31요거트 🥛",
        "바닐라 🍦",
        "초콜릿 🍫",
        "그린티 🍵",
        "블랙 소르베 ⚫",
        "아몬드 봉봉 🥜",
        "애플 민트 🍏",
    ]

    # ─────────────────────────────────────────────
    # 1. 매장 / 포장 선택
    # ─────────────────────────────────────────────
    st.subheader("1️⃣ 이용 방식 선택")

    col1, col2 = st.columns(2)
    with col1:
        eat_type = st.radio(
            "어디에서 드시나요? 😊",
            ["매장에서 먹고 갈게요 🪑", "포장해서 가져갈게요 🛍️"],
        )
    with col2:
        st.markdown(
            """
            <div class="br-card">
                <div class="br-tag">TIP</div>
                <div style="font-size:13px; color:#555;">
                    • 매장은 바로 드실 분들께 추천<br>
                    • 포장은 집·학교·공원에서 천천히 즐기기 좋아요 💕
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ─────────────────────────────────────────────
    # 2. 용기 선택 (메뉴 + 가격)
    # ─────────────────────────────────────────────
    st.subheader("2️⃣ 용기(사이즈) 선택")

    tabs = st.tabs(["🍧 Cone & Cup", "🧁 Hand Pack"])

    cone_cup_names = [
        name for name, info in menu_items.items() if info["category"] == "CONE & CUP"
    ]
    handpack_names = [
        name for name, info in menu_items.items() if info["category"] == "HAND PACK"
    ]

    with tabs[0]:
        st.caption("콘/컵으로 바로 즐기는 1~2스쿱 메뉴에요.")
        cone_choice = st.radio("메뉴를 골라주세요 👇", cone_cup_names)

    with tabs[1]:
        st.caption("집이나 모임에서 나눠먹기 좋은 핸드팩 메뉴에요.")
        hand_choice = st.radio("메뉴를 골라주세요 👇", handpack_names)

    # 현재 선택된 메뉴: 탭별로 마지막 클릭 기준
    # (Hand Pack을 선택하고 싶으면 탭에서 해당 메뉴를 선택하도록 안내)
    selected_menu_name = cone_choice if tabs[0].selected else cone_choice
    # Streamlit에서 어떤 탭이 선택됐는지 직접 알 수 없으므로
    # 아래와 같이 selectbox로 한 번 더 확실히 결정하게 만들자.

    st.markdown("#### ✅ 최종 용기 선택")
    selected_menu_name = st.selectbox(
        "실제 주문에 사용할 용기를 다시 한 번 골라주세요 😉",
        cone_cup_names + handpack_names,
    )

    selected_menu = menu_items[selected_menu_name]
    max_scoops = selected_menu["scoops"]
    base_price = selected_menu["price"]

    st.markdown(
        f"""
        <div class="br-card" style="margin-top:6px; margin-bottom:4px;">
            <div class="br-tag">{selected_menu['category']}</div>
            <div style="font-size:15px;">
                <b>{selected_menu_name}</b><br>
                <span style="color:#777;">{selected_menu['desc']}</span><br>
                <span style="color:#ff4b6e; font-weight:bold;">💰 {base_price:,}원</span>
                <span style="color:#999; font-size:12px;"> · 최대 {max_scoops}가지 맛 선택</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # ─────────────────────────────────────────────
    # 3. 맛 선택 (이하값으로)
    # ─────────────────────────────────────────────
    st.subheader("3️⃣ 아이스크림 맛 선택")

    st.caption(f"최대 **{max_scoops}가지 맛**까지 선택할 수 있어요. (같은 맛 여러 번 선택은 매장 직원에게 말씀해주세요 🙌)")

    selected_flavors = st.multiselect(
        "원하시는 맛을 골라주세요 😋",
        flavors,
        max_selections=None,  # 직접 검증할 거라 제한 X
        help=f"최대 {max_scoops}가지 맛까지 선택 가능합니다.",
    )

    flavor_count = len(selected_flavors)

    if flavor_count == 0:
        st.info("🍦 아이스크림 맛을 한 가지 이상 골라주세요!")
    elif flavor_count > max_scoops:
        st.error(f"⚠️ {max_scoops}가지까지만 선택할 수 있어요. (현재 {flavor_count}가지 선택됨)")

    st.markdown("---")

    # ─────────────────────────────────────────────
    # 4. 결제 방법 선택 (현금/카드/모바일페이/기프티콘)
    # ─────────────────────────────────────────────
    st.subheader("4️⃣ 결제 방법 선택")

    pay_method = st.radio(
        "어떻게 결제하시겠어요? 💳",
        [
            "현금 결제 💵",
            "카드 결제 💳",
            "모바일페이 (카카오페이·네이버페이 등) 📱",
            "기프티콘 사용 🎁",
        ],
    )

    st.markdown("---")

    # ─────────────────────────────────────────────
    # 5. 주문 요약 & 확정
    # ─────────────────────────────────────────────
    st.subheader("5️⃣ 주문 내용 확인하기 ✅")

    button_disabled = (flavor_count == 0) or (flavor_count > max_scoops)

    st.markdown('<div class="br-card">', unsafe_allow_html=True)
    st.markdown("### 🧾 주문 요약")

    st.write(f"- 이용 방식: **{eat_type}**")
    st.write(f"- 용기(사이즈): **{selected_menu_name}**")
    st.write(f"- 선택한 맛: **{flavor_count} / {max_scoops}가지**")

    if selected_flavors:
        for f in selected_flavors:
            st.write(f"  • {f}")
    else:
        st.write("  • (선택된 맛이 아직 없어요)")

    st.write(f"- 결제 방법: **{pay_method}**")
    st.write(f"### 💰 최종 결제 금액: **{base_price:,}원**")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    confirm = st.button("✨ 이대로 주문 확정하기 ✨", disabled=button_disabled)

    if confirm:
        st.success("주문이 완료되었습니다! 🍨 달콤한 아이스크림 즐겨주세요 😆")
        st.balloons()
        st.markdown(
            """
            <p style="text-align:center; font-size:15px; color:#666; margin-top:4px;">
                직원에게 이 화면을 보여주시면 주문이 더욱 빠르게 처리돼요 🙌
            </p>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()
