import streamlit as st
import plotly.graph_objects as go


# =========================================================
# 1. CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="GitHub Repository Popularity Dashboard",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# 2. SIDEBAR
# =========================================================

st.sidebar.title("Bộ lọc")

st.sidebar.write(
    "Các bộ lọc sẽ được kích hoạt sau khi "
    "có dữ liệu đã xử lý."
)

st.sidebar.divider()

st.sidebar.write("Ngôn ngữ lập trình")
st.sidebar.write("License")
st.sidebar.write("Thời gian tạo repository")


# =========================================================
# 3. TIÊU ĐỀ DASHBOARD
# =========================================================

st.title("GitHub Repository Popularity Dashboard")

st.write(
    "Phân tích các yếu tố liên quan đến mức độ phổ biến "
    "của các GitHub Repository."
)

st.divider()


# =========================================================
# 4. TỔNG QUAN - KPI
# =========================================================

st.subheader("Tổng quan dữ liệu")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Repositories",
        value="—"
    )

with col2:
    st.metric(
        label="Popularity",
        value="—"
    )

with col3:
    st.metric(
        label="Forks",
        value="—"
    )

with col4:
    st.metric(
        label="Programming Languages",
        value="—"
    )

st.caption(
    "Các KPI sẽ được tính từ bộ dữ liệu processed của nhóm."
)

st.divider()


# =========================================================
# 5. PHÂN TÍCH MỨC ĐỘ PHỔ BIẾN
# =========================================================

st.subheader("Phân tích mức độ phổ biến")

col_left, col_right = st.columns(2)


# ----- Biểu đồ 1 -----

with col_left:

    st.markdown("#### Phân phối mức độ phổ biến")

    fig_distribution = go.Figure()

    fig_distribution.add_annotation(
        text="Chờ dữ liệu processed",
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=18)
    )

    fig_distribution.update_layout(
        height=400,
        xaxis_title="Popularity",
        yaxis_title="Số lượng Repository"
    )

    st.plotly_chart(
        fig_distribution,
        use_container_width=True
    )


# ----- Biểu đồ 2 -----

with col_right:

    st.markdown("#### Mối quan hệ giữa các yếu tố")

    fig_relationship = go.Figure()

    fig_relationship.add_annotation(
        text="Chờ dữ liệu processed",
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=18)
    )

    fig_relationship.update_layout(
        height=400,
        xaxis_title="Yếu tố",
        yaxis_title="Popularity"
    )

    st.plotly_chart(
        fig_relationship,
        use_container_width=True
    )


st.divider()


# =========================================================
# 6. PHÂN TÍCH THEO NHÓM
# =========================================================

st.subheader("Phân tích theo đặc điểm Repository")

col_left2, col_right2 = st.columns(2)


# ----- Biểu đồ 3 -----

with col_left2:

    st.markdown("#### Repository theo ngôn ngữ lập trình")

    fig_language = go.Figure()

    fig_language.add_annotation(
        text="Chờ dữ liệu processed",
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=18)
    )

    fig_language.update_layout(
        height=400,
        xaxis_title="Programming Language",
        yaxis_title="Số Repository"
    )

    st.plotly_chart(
        fig_language,
        use_container_width=True
    )


# ----- Biểu đồ 4 -----

with col_right2:

    st.markdown("#### Popularity theo nhóm Repository")

    fig_group = go.Figure()

    fig_group.add_annotation(
        text="Chờ dữ liệu processed",
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=18)
    )

    fig_group.update_layout(
        height=400,
        xaxis_title="Nhóm",
        yaxis_title="Popularity"
    )

    st.plotly_chart(
        fig_group,
        use_container_width=True
    )


st.divider()


# =========================================================
# 7. TOP REPOSITORY
# =========================================================

st.subheader("Repository nổi bật")

st.info(
    "Bảng các repository nổi bật sẽ được hiển thị "
    "sau khi kết nối dữ liệu processed."
)


# =========================================================
# 8. GHI CHÚ
# =========================================================

st.divider()

st.caption(
    "Dashboard được xây dựng bằng Streamlit và Plotly."
)