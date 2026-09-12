import streamlit as st
import plotly.graph_objects as go

st.title("🗺️ 资源统筹与路线推荐")
st.caption("根据活动场地，智能推荐联动商圈与消费路线，提升区域文旅消费带动能力。")

resources = {
    "镜湖公园": {"商圈": "中山路步行街", "推荐路线": "镜湖公园（游园） → 中山路步行街（购物/用餐） → 鸠兹广场（夜景打卡）", "消费建议": "凭活动门票可在步行街指定商户享受 9 折优惠，联动发放消费券。"},
    "鸠兹广场": {"商圈": "中山路步行街、苏宁广场", "推荐路线": "鸠兹广场（主活动） → 苏宁广场（餐饮） → 镜湖公园（散步）", "消费建议": "与苏宁广场合作推出“文旅消费套餐”，拉动夜间经济。"},
    "中山路步行街": {"商圈": "自身即为核心商圈", "推荐路线": "步行街（主活动） → 镜湖公园（打卡） → 芜湖古城（文化体验）", "消费建议": "联动步行街商户推出“满减券”，与古城门票打包销售。"},
    "芜湖古城": {"商圈": "古城内部商业街", "推荐路线": "芜湖古城（文化体验） → 中山路步行街（购物） → 镜湖公园（休闲）", "消费建议": "推出“古城+步行街”联票，打造夜游路线。"}
}

selected_venue = st.selectbox("选择活动场地", ["镜湖公园", "鸠兹广场", "中山路步行街", "芜湖古城"], key="route_venue")

if st.button("查看推荐路线与资源"):
    data = resources[selected_venue]
    st.markdown(f"""
    <div style="background-color: #f0f7ff; padding: 25px; border-radius: 12px; border-left: 6px solid #1E88E5; margin-top: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h3 style="margin-top: 0; color: #1E88E5;">🎯 推荐联动商圈：{data['商圈']}</h3>
        <p style="font-size: 17px; line-height: 1.8;"><b>🗺️ 推荐消费路线：</b><br>{data['推荐路线']}</p>
        <p style="font-size: 17px; line-height: 1.8;"><b>💰 消费联动建议：</b><br>{data['消费建议']}</p>
    </div>
    """, unsafe_allow_html=True)

    import plotly.graph_objects as go

# 模拟地点坐标（经度、纬度）
locations = {
    "镜湖公园": [118.38, 31.34],
    "中山路步行街": [118.36, 31.33],
    "鸠兹广场": [118.37, 31.35],
    "芜湖古城": [118.39, 31.31]
}

# 绘制路线图
fig = go.Figure()

# 添加地点点
for name, coord in locations.items():
    fig.add_trace(go.Scatter(
        x=[coord[0]], y=[coord[1]],
        mode='markers+text',
        marker=dict(size=20, color='#1E88E5'),
        text=[name],
        textposition="top center",
        name=name
    ))

# 添加路线连线（根据推荐路线）
route_lines = {
    "镜湖公园": [["镜湖公园", "中山路步行街"], ["中山路步行街", "鸠兹广场"]],
    "鸠兹广场": [["鸠兹广场", "中山路步行街"], ["中山路步行街", "镜湖公园"]],
    "中山路步行街": [["中山路步行街", "镜湖公园"], ["镜湖公园", "芜湖古城"]],
    "芜湖古城": [["芜湖古城", "中山路步行街"], ["中山路步行街", "镜湖公园"]]
}

for line in route_lines[selected_venue]:
    p1, p2 = locations[line[0]], locations[line[1]]
    fig.add_trace(go.Scatter(
        x=[p1[0], p2[0]], y=[p1[1], p2[1]],
        mode='lines',
        line=dict(width=3, color='#FF9800', dash='dot'),
        showlegend=False
    ))

fig.update_layout(
    title="推荐消费路线示意图",
    xaxis_title="经度",
    yaxis_title="纬度",
    height=400,
    showlegend=False
)
st.plotly_chart(fig, use_container_width=True)