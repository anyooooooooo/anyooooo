import streamlit as st
st.title("Max重量は？")
st.write("あなたが上げられるMax重量を提示します！！")

def calculate_one_rep_max(weight, reps):
    """
    最大重量を計算する関数 (Epleyの公式)
    Max重量 = 重量 × (1 + 0.0333 × 回数)
    """
    if reps <= 1:
        return weight  # 1回しかできない場合はその重量がMax
    return round(weight * (1 + 0.0333 * reps), 2)

def main():
    print("=== 最大重量計算アプリ ===")
    exercises = ["ベンチプレス", "デッドリフト", "スクワット"]
    results = {}

    for exercise in exercises:
        print(f"\n{exercise}の情報を入力してください:")
        try:
            weight = float(input("使用した重量(kg): "))
            reps = int(input("挙げた回数: "))
            if weight <= 0 or reps <= 0:
                print("重量と回数は正の値を入力してください。")
                continue
            max_weight = calculate_one_rep_max(weight, reps)
            results[exercise] = max_weight
        except ValueError:
            print("数値を入力してください。")
    
    print("\n=== 結果 ===")
    for exercise, max_weight in results.items():
        print(f"{exercise}: 最大重量 {max_weight} kg")

if __name__ == "__main__":
    main()
