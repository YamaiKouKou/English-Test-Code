import customtkinter
import os
from PIL import Image

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("英単語テスト_改")
        self.geometry("700x500")

        #定義する理由：フレーム内のマス目を設定するため。
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #画像読み込み
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "画像たち")
        self.home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home_dark.png")))
        self.test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "test_icon.png")))
        self.study_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "study_icon.png")))

        #ナビゲーションフレーム作成
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_title_label = customtkinter.CTkLabel(self.navigation_frame, text="""English Tests
-改-""",
                                                                   font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_title_label.grid(row=0, column=0, padx=20, pady=20)
        #ホーム画面移行ボタン作成
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   fg_color="transparent", text_color="gray10", image=self.home_image,
                                                   hover_color="gray70", text="Home", anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        #テスト画面移行ボタン作成
        self.test_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   fg_color="transparent", text_color="gray10", image=self.test_image,
                                                   hover_color="gray70", text="Testing", anchor="w", command=self.test_button_event)
        self.test_button.grid(row=2, column=0, sticky="ew")
        #単語勉強画面移行ボタン作成
        self.study_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   fg_color="transparent", text_color="gray10",image=self.study_image,
                                                   hover_color="gray70", text="Studying", anchor="w", command=self.study_button_event)
        self.study_button.grid(row=3, column=0, sticky="ew")

        #ホームフレーム
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_rowconfigure((0,1,2), weight=1)
        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid(row=0, column=1, sticky="snew")

        self.home_label = customtkinter.CTkLabel(self.home_frame, text="HOME1")
        self.home_label.grid(row=0, column=0, sticky="ew", padx=10)

        self.home_label = customtkinter.CTkLabel(self.home_frame, text="HOME1")
        self.home_label.grid(row=0, column=1, sticky="ew")

        self.home_label = customtkinter.CTkLabel(self.home_frame, text="HOME1")
        self.home_label.grid(row=0, column=2, sticky="ew")

        #テスト画面フレーム
        self.test_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        #単語勉強フレーム
        self.study_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        #デフォルトフレーム
        self.select_by_frame("home")
        
    def select_by_frame(self, name):
        self.home_button.configure(fg_color="gray75" if name == "home" else "transparent")
        self.test_button.configure(fg_color="gray75" if name == "test" else "transparent")
        self.study_button.configure(fg_color="gray75" if name == "study" else "transparent")
        #ホーム画面遷移
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="snew")
        else:
            self.home_frame.grid_forget()
        #テスト画面遷移
        if name == "test":
            self.test_frame.grid(row=0, column=1, sticky="snew")
        else:
            self.test_frame.grid_forget()
        #単語勉強画面遷移
        if name == "study":
            self.study_frame.grid(row=0, column=1, sticky="snew")
        else:
            self.study_frame.grid_forget()
            

        

    def home_button_event(self):
        self.select_by_frame("home")
        
    def test_button_event(self):
        self.select_by_frame("test")
        
    def study_button_event(self):
        self.select_by_frame("study")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
