#初版
#v0

import streamlit as st
import pandas as pd
import random
from collections import defaultdict

@st.cache_data
def read_yi_csv(filepath: str) -> dict:
    df = pd.read_csv(filepath, encoding="utf-8-sig")
    pack = defaultdict(list)
    # grouped = df.groupby("gua_number")
    # pack = {num: group.to_dict("records") for num, group in grouped}
    for number, group in df.groupby("gua_number"):
        rows = group.to_dict("records")
        pack[number].extend(rows)
    return dict(pack)

DATA_PACK = read_yi_csv("yi_data.csv")

def next_phase():
    st.session_state.phase_idx += 1
    if st.session_state.phase_idx >= len(st.session_state.phase_order):
        st.session_state.is_finished = True

def is_valid_cell(val):
    if pd.isna(val):
        return False
    if str(val).strip() in ["", "nan"]:
        return False
    return True

if "initialized" not in st.session_state:
    all_phases = list(DATA_PACK.keys())
    random.shuffle(all_phases)
    st.session_state.update(
        phase_order = all_phases,
        phase_idx = 0,
        random_seed = random.randint(1, 9999),
        is_finished = False,
        initialized = True,
    )

st.set_page_config(page_title="周易64卦练习", layout="centered")
st.title("卦辞爻辞象彖练习")

if st.session_state.is_finished:
    st.balloons()
    st.success("恭喜已完成全部64卦练习")
    if st.button("重新开始"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()
    st.stop()

phase_name = st.session_state.phase_order[st.session_state.phase_idx]
col_a, col_b = st.columns([2, 1])
col_a.subheader(f"当前卦: {phase_name}")
col_b.markdown(f"### 进度: {st.session_state.phase_idx + 1} / {len(st.session_state.phase_order)}")

with st.form(key=f"form_{phase_name}_{st.session_state.phase_idx}"):
    st.info("请在完成后提交")
    user_answer = []
    for 

# st.write(all_phases[0])
st.write(all_phases)
# st.write(DATA_PACK)
