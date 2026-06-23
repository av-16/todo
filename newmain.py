import customtkinter as ctk
from ctkdateentry import CTkDateEntry

ctk.set_appearance_mode("Light") 
ctk.set_default_color_theme("./teal.json") 

class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Todo App")
        self.geometry("800x500")
#        self.resizable(False, False) # Prevents the layout from breaking

        # 2. Configure Grid Layout (Crucial for alignment)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 3. Create UI Elements
        self.sidebar()
        self.create_main_content()

    def sidebar(self):

        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.sidebar_label = ctk.CTkLabel(self.sidebar_frame, text="Menu", font=ctk.CTkFont(size=20, weight="bold"))
        self.sidebar_label.grid(row=0, column=0, padx=20, pady=20)

        self.btn_viewtasks = ctk.CTkButton(self.sidebar_frame, text="View Tasks", command=lambda: self.show_page("ViewPage"))
        self.btn_viewtasks.grid(row=1, column=0, padx=20, pady=10)

        self.btn_createtasks = ctk.CTkButton(self.sidebar_frame, text="Create Task", command=lambda: self.show_page("CreatePage"))
        self.btn_createtasks.grid(row=2, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Theme:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.theme_switch = ctk.CTkSwitch(self.sidebar_frame, text="Dark Mode", command=self.toggle_theme)
        self.theme_switch.grid(row=6, column=0, padx=20, pady=10)

    def create_main_content(self):
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.pages = {}

        ViewPage = ctk.CTkFrame(self.main_frame,corner_radius=15)
        ViewPage.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.welcome_label = ctk.CTkLabel(ViewPage, text="View Tasks", font=ctk.CTkFont(size=24, weight="bold"))
        self.welcome_label.pack(pady=20)
        self.entry_field = ctk.CTkEntry(ViewPage, placeholder_text="Type something here...")
        self.entry_field.pack(pady=10, padx=20, fill="x")
        self.submit_btn = ctk.CTkButton(ViewPage, text="Process Data", fg_color="green", hover_color="darkgreen",command=self.search)
        self.submit_btn.pack(pady=10)

        self.pages["ViewPage"] = ViewPage


        CreatePage = ctk.CTkFrame(self.main_frame,corner_radius=15)
        CreatePage.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.welcome_label = ctk.CTkLabel(CreatePage, text="Create Tasks", font=ctk.CTkFont(size=24, weight="bold"))
        self.welcome_label.pack(pady=20)
        self.entry_title = ctk.CTkEntry(CreatePage, placeholder_text="Enter title")
        self.entry_title.pack(pady=10, padx=20, fill="x")
        self.entry_desc = ctk.CTkEntry(CreatePage, placeholder_text="Enter Description")
        self.entry_desc.pack(pady=10, padx=20, fill="x")
        self.submit_btn = ctk.CTkButton(CreatePage, text="Process Data", fg_color="green", hover_color="darkgreen",command=self.search)
        self.submit_btn.pack(pady=10)
        self.date_entry = CTkDateEntry(CreatePage)
        self.date_entry.pack(pady=10)
        def open_calendar_fixed():
            self.update_idletasks()
            self.after_idle(original)
        self.date_entry.open_calendar = open_calendar_fixed
        self.pages["CreatePage"] = CreatePage


        self.pages["ViewPage"].tkraise()

    def viewtask_click(self):
        print("fetching all tasks.")

    def toggle_theme(self):
        if self.theme_switch.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")
    def search(self):
        text = self.entry_field.get()
        print("searching",text)
        self.welcome_label.text = text
    def show_page(self,name):
        self.pages[name].tkraise()

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
