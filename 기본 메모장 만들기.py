import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class Notepad:
    def __init__(self, root):
        """메모장 애플리케이션 초기화"""
        self.root = root
        self.root.title("Gemini 메모장")
        self.root.geometry("800x600")

        # 현재 열려있는 파일 경로 (없으면 None)
        self.current_file = None

        # 텍스트 위젯 생성
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill='both')

        # 메뉴바 생성
        self.create_menu()

    def create_menu(self):
        """메뉴바와 메뉴 항목들을 생성합니다."""
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # 파일 메뉴
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="파일(F)", menu=file_menu)
        file_menu.add_command(label="새 파일", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="열기", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="저장", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="다른 이름으로 저장", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="종료", command=self.exit_app)

        # 편집 메뉴
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="편집(E)", menu=edit_menu)
        edit_menu.add_command(label="실행 취소", command=self.text_area.edit_undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="다시 실행", command=self.text_area.edit_redo, accelerator="Ctrl+Y")

        # 정보 메뉴
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="정보(A)", menu=help_menu)
        help_menu.add_command(label="메모장 정보", command=self.show_about)
        
        # 단축키 바인딩
        self.root.bind_all("<Control-n>", lambda event: self.new_file())
        self.root.bind_all("<Control-o>", lambda event: self.open_file())
        self.root.bind_all("<Control-s>", lambda event: self.save_file())
        self.root.bind_all("<Control-Shift-S>", lambda event: self.save_as_file())


    def new_file(self):
        """새 파일을 위한 텍스트 영역을 초기화합니다."""
        if self.text_area.get(1.0, tk.END).strip():
            if not messagebox.askyesno("경고", "저장하지 않은 변경사항이 있습니다. 계속하시겠습니까?"):
                return
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.root.title("Gemini 메모장 - 새 파일")

    def open_file(self):
        """파일을 열어 텍스트 영역에 표시합니다."""
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not file_path:
            return
        
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, file.read())
            self.current_file = file_path
            self.root.title(f"Gemini 메모장 - {file_path}")
        except Exception as e:
            messagebox.showerror("오류", f"파일을 여는 중 오류가 발생했습니다: {e}")

    def save_file(self):
        """현재 파일을 저장합니다. 새 파일이면 save_as_file을 호출합니다."""
        if self.current_file:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.current_file, "w", encoding="utf-8") as file:
                    file.write(content)
                self.root.title(f"Gemini 메모장 - {self.current_file}")
            except Exception as e:
                messagebox.showerror("오류", f"파일을 저장하는 중 오류가 발생했습니다: {e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        """새로운 파일로 저장합니다."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not file_path:
            return

        try:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            self.current_file = file_path
            self.root.title(f"Gemini 메모장 - {file_path}")
        except Exception as e:
            messagebox.showerror("오류", f"파일을 저장하는 중 오류가 발생했습니다: {e}")

    def exit_app(self):
        """애플리케이션을 종료합니다."""
        if messagebox.askokcancel("종료", "메모장을 종료하시겠습니까?"):
            self.root.destroy()

    def show_about(self):
        """'메모장 정보' 메시지 박스를 표시합니다."""
        messagebox.showinfo(
            "Gemini 메모장 정보",
            "Version 1.0\n\nCreated by Gemini Code Assist"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
