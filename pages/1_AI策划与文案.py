import streamlit as st
from openai import OpenAI

import os
API_KEY = os.getenv("ZHIPU_API_KEY")  # 新代码，去环境变量里找
BASE_URL = "https://open.bigmodel.cn/api/paas/v4/"
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

st.title("✨ AI策划与文案生成")
st.caption("输入活动基本信息，AI为你生成策划大纲、宣传推文，并自动评估执行风险。")

topic = st.text_input("活动主题（例如：中秋游园会）：")
budget = st.number_input("活动预算（元）：", value=5000)
venue = st.selectbox("活动场地", ["镜湖公园", "鸠兹广场", "中山路步行街", "芜湖古城"])

if st.button("生成策划案"):
    if not topic:
        st.warning("请先输入活动主题！")
    else:
        with st.spinner("AI正在疯狂思考中..."):
            try:
                prompt = f"""
                你是芜湖市镜湖区文旅局的活动策划专家。你非常熟悉镜湖区的历史文化（如镜湖、鸠兹广场、芜湖古城、广济寺等）、商圈分布（中山路步行街、苏宁广场等）和本地居民消费习惯。
                请结合这些真实背景，为'{topic}'写一份活动策划大纲。
                活动场地：{venue}
                活动预算：{budget}元。
                要求包含：活动背景、目标人群、活动流程、预算分配建议、宣传推广建议。
                最后附上【执行风险提醒】，指出该活动可能面临的天气、人流、交通等风险，并提出防范措施。
                """
                response = client.chat.completions.create(
                    model="GLM-5.3",
                    messages=[{"role": "user", "content": prompt}]
                )
                st.success("策划案生成成功！")
                st.markdown(response.choices[0].message.content)
                
                # 增加下载按钮
                st.download_button(
                    label="📥 下载策划案 (Markdown)",
                    data=response.choices[0].message.content,
                    file_name=f"{topic}_策划案.md",
                    mime="text/markdown"
                )
            except Exception as e:
                st.error(f"调用AI出错了：{e}")