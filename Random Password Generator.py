import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("随机密码生成器")

        # 设置默认密码长度
        self.password_length = tk.IntVar(value=12)

        # 设置默认字符种类
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        # 创建GUI元素
        self.create_widgets()

    def create_widgets(self):
        # 创建密码长度标签和输入框
        length_label = ttk.Label(self.root, text="密码长度:")
        length_label.grid(row=0, column=0, padx=10, pady=10)
        length_entry = ttk.Entry(self.root, textvariable=self.password_length)
        length_entry.grid(row=0, column=1, padx=10, pady=10)

        # 创建字符种类复选框
        options_frame = ttk.LabelFrame(self.root, text="字符种类")
        options_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="W")

        uppercase_cb = ttk.Checkbutton(options_frame, text="大写字母", variable=self.use_uppercase)
        uppercase_cb.grid(row=0, column=0, padx=10, pady=5, sticky="W")
        lowercase_cb = ttk.Checkbutton(options_frame, text="小写字母", variable=self.use_lowercase)
        lowercase_cb.grid(row=1, column=0, padx=10, pady=5, sticky="W")
        digits_cb = ttk.Checkbutton(options_frame, text="数字", variable=self.use_digits)
        digits_cb.grid(row=2, column=0, padx=10, pady=5, sticky="W")
        symbols_cb = ttk.Checkbutton(options_frame, text="符号", variable=self.use_symbols)
        symbols_cb.grid(row=3, column=0, padx=10, pady=5, sticky="W")

        # 创建生成密码按钮
        generate_button = ttk.Button(self.root, text="生成密码", command=self.generate_password)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # 创建密码输出框
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(self.root, textvariable=self.password_var, state="readonly", font=("Courier", 12))
        password_entry.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="WE")

        # 创建复制密码按钮
        copy_button = ttk.Button(self.root, text="复制密码", command=self.copy_to_clipboard)
        copy_button.grid(row=4, column=0, columnspan=2, pady=10)

    def generate_password(self):
        # 检查密码长度
        length = self.password_length.get()
        if not 8 <= length <= 256:
            messagebox.showwarning("警告", "密码长度必须在8到256之间")
            return

        # 选择字符种类
        character_set = ""
        if self.use_uppercase.get():
            character_set += string.ascii_uppercase
        if self.use_lowercase.get():
            character_set += string.ascii_lowercase
        if self.use_digits.get():
            character_set += string.digits
        if self.use_symbols.get():
            character_set += string.punctuation

        # 生成密码
        password = ''.join(random.choice(character_set) for _ in range(length))

        # 显示密码
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        pyperclip.copy(password)
        messagebox.showinfo("提示", "密码已复制到剪贴板")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
