import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⚠️ 排期冲突检测")
# 在文件开头，st.title 之后加上：
st.write("### 📁 数据管理")
uploaded_file = st.file_uploader("上传活动排期表 (Excel格式)", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.success("数据导入成功！下方图表已更新。")
else:
    # 原来的默认数据逻辑保留
    try:
        df = pd.read_excel("data.xlsx")
    except:
        df = pd.DataFrame([...]) # 原来的模拟数据
st.caption("输入新活动的时间，系统会自动检测是否与已有活动冲突，并用甘特图展示排期。")

try:
    df = pd.read_excel("data.xlsx")
except:
    df = pd.DataFrame([
        {"活动名称": "国庆灯光秀", "开始日期": "2026-10-01", "结束日期": "2026-10-03", "场地": "镜湖公园"},
        {"活动名称": "中秋游园会", "开始日期": "2026-09-25", "结束日期": "2026-09-27", "场地": "鸠兹广场"}
    ])

# 指标卡片
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("已排期活动总数", len(df))
with col2:
    st.metric("涉及场地数", df["场地"].nunique())
with col3:
    st.metric("最早活动日期", df["开始日期"].min())

st.divider()

# 甘特图
st.write("### 📊 活动排期甘特图")
fig = px.timeline(df, x_start="开始日期", x_end="结束日期", y="活动名称", color="场地", text="场地")
fig.update_yaxes(autorange="reversed")
fig.update_layout(height=300, margin=dict(l=0, r=0, t=30, b=0))
st.plotly_chart(fig, use_container_width=True)

st.divider()

# 冲突检测
st.write("### ➕ 新增活动排期检测")
new_name = st.text_input("新活动名称（例如：汉服文化节）")
new_venue = st.selectbox("选择场地", ["镜湖公园", "鸠兹广场", "中山路步行街", "芜湖古城"], key="conflict_venue")

col1, col2 = st.columns(2)
with col1:
    new_start = st.date_input("开始日期")
with col2:
    new_end = st.date_input("结束日期")

if st.button("检测冲突"):
    conflict = False
    for index, row in df.iterrows():
        if row["场地"] == new_venue:
            if str(new_start) <= str(row["结束日期"]) and str(new_end) >= str(row["开始日期"]):
                st.error(f"❌ 严重冲突！在 {new_venue} 已有活动【{row['活动名称']}】占用时间：{row['开始日期']} 至 {row['结束日期']}。建议改期或更换场地。")
                conflict = True
                break
    if not conflict:
        st.success(f"✅ 场地 {new_venue} 在 {new_start} 至 {new_end} 期间空闲，可以排期！")