import os
import streamlit as st
import google.generativeai as genai

# API 키 설정
os.environ["GOOGLE_API_KEY"] = "AIzaSyDq6DsEk_f4sJWmlGPYC1Msxme1zNTwAh0"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit 앱 제목
st.title("맞춤법 검사기")
st.subheader("전지 전능한 Google Gemini를 활용한 맞춤법 검사기")

# 텍스트 입력 받기
user_input = st.text_area("텍스트 입력", "여기에 텍스트를 입력하세요.")

# 맞춤법 검사 버튼
if st.button("맞춤법 검사"):
    if user_input.strip():  # 입력이 비어있지 않은 경우
        try:
            # 구글 제미나이 API 호출
            prompt = f"다음 텍스트의 맞춤법과 문법 오류를 수정해주세요:\n\n{user_input}"
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            
            # 수정된 결과 출력
            st.write("**수정된 텍스트:**")
            st.success(response.text)

        except Exception as e:
            st.error(f"맞춤법 검사 중 오류가 발생했습니다: {e}")
    else:
        st.warning("텍스트를 입력하세요.")
