import streamlit as st

def calculate_one_rep_max(weight, reps):
    if reps <= 1:
        return weight
    return round(weight * (1 + 0.0333 * reps), 2)

st.title("Max重量は？")
st.write("最大重量計算アプリ")
st.write("あなたが上げられるMax重量を提示します！！")
st.write("種目ごとに重量と回数を入力して、最大重量を計算します。")
exercises = ["ベンチプレス", "デッドリフト", "スクワット"]
results = {}

for exercise in exercises:
    st.header(exercise)
    weight = st.number_input(f"{exercise}の使用した重量 (kg)", min_value=0.0, step=1.0, key=f"{exercise}_weight")
    reps = st.number_input(f"{exercise}の挙げた回数", min_value=0, step=1, key=f"{exercise}_reps")
    
    if weight > 0 and reps > 0:
        max_weight = calculate_one_rep_max(weight, reps)
        results[exercise] = max_weight
        st.write(f"最大重量: {max_weight} kg")

if results:
    st.write("### すべての計算結果")
    
    summary_table = [{"種目": exercise, "最大重量 (kg)": max_weight} for exercise, max_weight in results.items()]
    
    st.table(summary_table)