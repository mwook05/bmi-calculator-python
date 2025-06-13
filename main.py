import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height_cm = float(height_entry.get())
        weight_kg = float(weight_entry.get())

        if height_cm <= 0 or weight_kg <= 0:
            messagebox.showerror("입력 오류", "키와 몸무게는 양수여야 합니다.")
            return

        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "저체중"
        elif 18.5 <= bmi < 23:
            category = "정상"
        elif 23 <= bmi < 25:
            category = "과체중"
        else:
            category = "비만"

        result_label.config(text=f"당신의 BMI: {bmi}\n결과: {category}")

    except ValueError:
        messagebox.showerror("입력 오류", "숫자만 입력해주세요.")
    except ZeroDivisionError:
        messagebox.showerror("입력 오류", "키는 0이 될 수 없습니다.")

window = tk.Tk()
window.title("파이썬 BMI 계산기")
window.geometry("300x250")
window.resizable(False, False)

frame = tk.Frame(window, padx=20, pady=20)
frame.pack()

height_label = tk.Label(frame, text="신장 (cm):")
height_label.grid(row=0, column=0, sticky="w", pady=5)
height_entry = tk.Entry(frame)
height_entry.grid(row=0, column=1)

weight_label = tk.Label(frame, text="체중 (kg):")
weight_label.grid(row=1, column=0, sticky="w", pady=5)
weight_entry = tk.Entry(frame)
weight_entry.grid(row=1, column=1)

calculate_button = tk.Button(frame, text="계산하기", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2, pady=15, sticky="ew")

result_label = tk.Label(frame, text="결과가 여기에 표시됩니다.", font=("Helvetica", 12))
result_label.grid(row=3, columnspan=2)

window.mainloop()
