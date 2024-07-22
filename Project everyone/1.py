
# 导入模块 Tkinter库用于创建gui界面 # 导入messagebox模块用于显示消息框 但未使用
import tkinter as tk
from tkinter import messagebox


# 定义程序类型 为应用程序 ， 定义一个名为BottomNavigationBarApp的类 设置窗口标题
class BottomNavigationBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bottom Navigation Bar App")
        
        # 设置顶部标题
        self.title_label = tk.Label(self.root, text="这是顶部标题", font=("Helvetica", 18), pady=20)
        self.title_label.pack() 

        # 设置四个底部导航按钮 创建一个Frame容器，用于放置按钮 用pack方法将Frame放置在窗口底部 创建四个按钮，分别命名为“页面1”、“页面2”、“页面3”和“页面4”，并设置宽度为10，点击按钮时调用show_content方法显示相应内容
        self.button_frame = tk.Frame(self.root, pady=10)
        self.button_frame.pack()

        self.button1 = tk.Button(self.button_frame, text="首页", width=10, command=lambda: self.show_content("首页"))
        self.button1.grid(row=0, column=0, padx=10)

        self.button2 = tk.Button(self.button_frame, text="活动", width=10, command=lambda: self.show_content("活动"))
        self.button2.grid(row=0, column=1, padx=10)

        self.button3 = tk.Button(self.button_frame, text="更多", width=10, command=lambda: self.show_content("更多"))
        self.button3.grid(row=0, column=2, padx=10)

        self.button4 = tk.Button(self.button_frame, text="我的", width=10, command=lambda: self.show_content("我的"))
        self.button4.grid(row=0, column=3, padx=10)

        # 显示内容的区域
        self.content_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.content_label.pack(pady=20)

    # 定义一个方法show_content，用于更新显示内容的标签文本
    def show_content(self, page):
        self.content_label.config(text=f"这是{page}的内容。")

# 创建Tkinter的主窗口，实例化BottomNavigationBarApp类，并启动事件循环。
if __name__ == "__main__":
    root = tk.Tk()
    app = BottomNavigationBarApp(root)
    root.mainloop()

# 这段代码实现了一个简单的导航栏应用程序，用户可以通过点击底部导航栏的按钮来切换显示不同的页面内容。适用于需要简单页面切换功能的GUI应用程序。
# 注意事项
# 布局管理：使用pack和grid方法来管理窗口组件的布局，可以根据需要选择适合的布局管理器。
# 事件绑定：通过command参数将按钮点击事件绑定到show_content方法，实现页面内容的动态更新。
# 文本更新：使用config方法更新标签的文本内容，实现页面内容的动态显示。