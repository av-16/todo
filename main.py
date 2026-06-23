import customtkinter as ctk
from ctk_json_theme import CTkJsonTheme  # or paste class above

ctk.set_appearance_mode("dark")  # optional default until theme loads
ctk.set_default_color_theme("dark-blue")  # optional_builtin

theme = CTkJsonTheme("newnew.json")

app = ctk.CTk()  # use CTk (no tkinter.Tk)
app.geometry("420x240")

frame = ctk.CTkFrame(master=app)
frame.pack(padx=20, pady=20, fill="both", expand=True)
theme.apply_to(frame, "frame")

lbl = ctk.CTkLabel(master=frame, text="Themed label")
lbl.pack(pady=(8,4))
theme.apply_to(lbl, "label")

entry = ctk.CTkEntry(master=frame)
entry.pack(pady=6)
theme.apply_to(entry, "entry")

btn = ctk.CTkButton(master=frame, text="OK")
btn.pack(pady=6)
theme.apply_to(btn, "button")

app.mainloop()

