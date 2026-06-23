import customtkinter as ctk

# Set up the app window theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("./newnew.json")


class MultiPageApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Page App Tutorial")
        self.geometry("600x400")

        # Configure layout: Left side is Menu Sidebar, Right side is Container for Pages
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 1. Create the Sidebar Menu (Always stays on screen)
        self.sidebar = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.menu_label = ctk.CTkLabel(self.sidebar, text="Navigation", font=ctk.CTkFont(weight="bold"))
        self.menu_label.grid(row=0, column=0, padx=20, pady=20)

        # Sidebar Buttons to switch pages
        self.btn_page1 = ctk.CTkButton(self.sidebar, text="Go to Page 1", command=lambda: self.show_page("page1"))
        self.btn_page1.grid(row=1, column=0, padx=20, pady=10)

        self.btn_page2 = ctk.CTkButton(self.sidebar, text="Go to Page 2", command=lambda: self.show_page("page2"))
        self.btn_page2.grid(row=2, column=0, padx=20, pady=10)

        # 2. Create a dictionary to hold our different pages
        self.pages = {}

        # Initialize the pages inside our right-side column (column 1)
        self.pages["page1"] = PageOne(parent=self)
        self.pages["page2"] = PageTwo(parent=self)

        # 3. Show the first page by default on startup
        self.show_page("page1")

    def show_page(self, page_name):
        """Hides all pages and displays the selected one."""
        # Hide all pages first using grid_forget()
        for page in self.pages.values():
            page.grid_forget()
        
        # Display the requested page in column 1
        self.pages[page_name].grid(row=0, column=1, padx=20, pady=20, sticky="nsew")


# =====================================================================
# DEFINE YOUR PAGES AS SEPARATE CLASSES (Inheriting from CTkFrame)
# =====================================================================

class PageOne(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=15)
        
        # Design elements for Page 1
        self.label = ctk.CTkLabel(self, text="Welcome to Page 1", font=ctk.CTkFont(size=22, weight="bold"))
        self.label.pack(pady=40, padx=40)
        
        self.description = ctk.CTkLabel(self, text="This is where your primary dashboard features live.")
        self.description.pack(pady=10)


class PageTwo(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=15)
        
        # Design elements for Page 2
        self.label = ctk.CTkLabel(self, text="Welcome to Page 2", font=ctk.CTkFont(size=22, weight="bold"))
        self.label.pack(pady=40, padx=40)
        
        self.description = ctk.CTkLabel(self, text="This could be your Settings page or Database History logs.")
        self.description.pack(pady=10)


if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()
