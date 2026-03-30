import streamlit as st
import time
import os
import random
from gtts import gTTS
from io import BytesIO

# --- 0. 系統配置 ---
st.set_page_config(
    page_title="阿美語 - 動物 Aadopen", 
    page_icon="🐾", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# --- CSS 視覺魔法 (森林大地螢光科技風) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Noto+Sans+TC:wght@400;700&display=swap');

    /* 全局背景：深綠黑 */
    .stApp { 
        background-color: #001008;
        background-image: radial-gradient(circle at 50% 0%, #1B5E20 0%, #001008 80%);
        font-family: 'Noto Sans TC', sans-serif;
        color: #E8F5E9;
    }
    
    .block-container { padding-top: 1rem !important; padding-bottom: 5rem !important; }

    /* --- Header --- */
    .header-container {
        background: rgba(27, 94, 32, 0.3);
        border: 1px solid #00E676;
        box-shadow: 0 0 15px rgba(0, 230, 118, 0.3);
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin-bottom: 40px;
        backdrop-filter: blur(10px);
    }
    
    .main-title {
        font-family: 'Roboto Mono', monospace;
        color: #00E676;
        font-size: 40px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 0 0 10px #00E676;
        margin: 0;
    }
    
    .sub-title { color: #C8E6C9; font-size: 18px; margin-top: 10px; letter-spacing: 1px; }
    .teacher-tag { display: inline-block; margin-top: 15px; padding: 5px 15px; border: 1px solid #FFB300; color: #FFB300; border-radius: 50px; font-size: 12px; font-weight: bold; letter-spacing: 1px; }

    /* --- Cards --- */
    .word-card {
        background: rgba(255, 255, 255,
