import customtkinter as ctk

# Set the theme and color style
ctk.set_appearance_mode("Dark")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue") # Options: "blue", "green", "dark-blue"

class ModernApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Configure Window
        self.title("Smart Dashboard v1.0")
        self.geometry("800x500")
        self.resizable(False, False) # Prevents the layout from breaking

        # 2. Configure Grid Layout (Crucial for alignment)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 3. Create UI Elements
        self.create_sidebar()
        self.create_main_content()

    def create_sidebar(self):
        # Sidebar Frame
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        # App Title
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="App Menu", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)

        # Menu Buttons
        self.btn_dashboard = ctk.CTkButton(self.sidebar_frame, text="Dashboard", command=self.dashboard_click)
        self.btn_dashboard.grid(row=1, column=0, padx=20, pady=10)

        # Theme Toggle
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Theme:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.theme_switch = ctk.CTkSwitch(self.sidebar_frame, text="Dark Mode", command=self.toggle_theme)
        self.theme_switch.grid(row=6, column=0, padx=20, pady=10)

    def create_main_content(self):
        # Main Display Content Frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Welcome Text
        self.welcome_label = ctk.CTkLabel(self.main_frame, text="Welcome Back!", font=ctk.CTkFont(size=24, weight="bold"))
        self.welcome_label.pack(pady=20)

        # User Input Field
        self.entry_field = ctk.CTkEntry(self.main_frame, placeholder_text="Type something here...")
        self.entry_field.pack(pady=10, padx=20, fill="x")

        # Submit Button
        self.submit_btn = ctk.CTkButton(self.main_frame, text="Process Data", fg_color="green", hover_color="darkgreen",command=self.search)
        self.submit_btn.pack(pady=10)

    def dashboard_click(self):
        print("Dashboard Button Clicked!")

    def toggle_theme(self):
        if self.theme_switch.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")
    def search(self):
        text = self.entry_field.get()
        print("searching",text)
        self.welcome_label.text = text

if __name__ == "__main__":
    app = ModernApp()
    app.mainloop()
