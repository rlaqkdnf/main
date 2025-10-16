import tkinter as tk
from tkinter import scrolledtext

# 기본 창 생성
window = tk.Tk()
window.title("기본 편집기")
window.geometry("800x600")

# 스크롤 가능한 텍스트 상자 생성
# wrap=tk.WORD: 단어 단위로 자동 줄바꿈
# undo=True: 실행 취소(Ctrl+Z) 기능 활성화
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, undo=True)

# 텍스트 상자를 창에 가득 채우도록 배치
text_area.pack(expand=True, fill='both')

# 창 실행
window.mainloop()
