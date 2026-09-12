import streamlit as st
from openai import OpenAI

import os
API_KEY = os.getenv("ZHIPU_API_KEY")  # 新代码，去环境变量里找
BASE_URL = "https://open.bigmodel.cn/api/paas/v4/"
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

st.title("📊 数据复盘与总结")
st.caption("输入活动实际数据，AI 自动生成复盘报告，分析成效与不足。")

col1, col2, col3 = st.columns(3)
with col1:
    actual_people = st.number_input("实际参与人数", value=500)
with col2:
    actual_cost = st.number_input("实际花费（元）", value=4800)
with col3:
    actual_consumption = st.number_input("带动消费额（元）", value=25000)

if st.button("生成复盘报告"):
    with st.spinner("AI正在分析数据，生成复盘报告..."):
        try:
            prompt = f"""
            你是芜湖市镜湖区文旅局的活动复盘专家。
            刚刚结束了一场活动，数据如下：
            - 实际参与人数：{actual_people} 人
            - 实际花费：{actual_cost} 元
            - 带动周边消费：{actual_consumption} 元
            
            请写一份简明的复盘报告，包含：
            1. 活动成效（用数据说话，计算人均消费、投入产出比等）
            2. 亮点与不足
            3. 下一步改进建议
            请用清晰的 Markdown 格式输出。
            """
            response = client.chat.completions.create(
                model="GLM-5.3",
                messages=[{"role": "user", "content": prompt}]
            )
            st.success("复盘报告生成成功！")
            st.markdown(response.choices[0].message.content)
        except Exception as e:
            st.error(f"调用AI出错了：{e}")