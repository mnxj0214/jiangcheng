import streamlit as st

# 设置全局页面配置
st.set_page_config(
    page_title="江城智旅 | 文旅运营智能体",
    page_icon="🏞️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 侧边栏
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/mountain.png", width=80)
    st.title("江城智旅")
    st.caption("芜湖市镜湖区文旅局 · 智能运营助手")
    st.divider()
    st.markdown("### 📌 系统简介")
    st.info("本系统面向文旅活动运营场景，提供排期冲突检测、AI策划、资源联动和数据复盘功能。")
    st.divider()
    st.caption("技术栈：Python + Streamlit + 智谱AI")

# 主页内容
st.title("🏞️ 江城智旅——文旅活动运营智能体")
# 在主页内容里，st.title 之后加上：
st.divider()
st.subheader("🚨 智能预警中心")
st.caption("系统自动扫描当前排期与活动数据，主动提示风险")

# 模拟预警逻辑
import pandas as pd
try:
    df = pd.read_excel("data.xlsx")
    # 1. 检测排期重叠
    conflict_count = 0
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            if df.iloc[i]["场地"] == df.iloc[j]["场地"]:
                if df.iloc[i]["开始日期"] <= df.iloc[j]["结束日期"] and df.iloc[i]["结束日期"] >= df.iloc[j]["开始日期"]:
                    conflict_count += 1
    
    if conflict_count > 0:
        st.warning(f"⚠️ 检测到 {conflict_count} 处排期冲突，请前往【排期冲突检测】处理。")
    else:
        st.success("✅ 当前排期正常，无冲突。")
    
    # 2. 天气/人流预警（模拟逻辑）
    import datetime
    today = datetime.date.today()
    upcoming = df[pd.to_datetime(df["开始日期"]).dt.date >= today]
    if len(upcoming) > 0:
        st.info(f"📅 未来有 {len(upcoming)} 场活动即将举办，建议提前做好安保与交通预案。")
except:
    st.info("暂无排期数据，请先导入。")
st.subheader("芜湖市镜湖区文旅局")

st.markdown("""
### 👋 欢迎使用
请点击左侧导航栏，选择需要的功能模块：

- **✨ AI策划与文案**：生成活动策划大纲与宣传推文
- **⚠️ 排期冲突检测**：检测新活动与已有活动的时间冲突
- **🗺️ 资源统筹与路线**：推荐联动商圈与消费路线
- **📊 数据复盘**：自动生成活动复盘报告
""")

st.divider()
st.caption("© 2026 江城智旅项目组 | 仅为比赛演示原型")