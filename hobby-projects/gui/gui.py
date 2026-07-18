import tkinter as tk
from tkinter import ttk

def validate():
    pass

def switch_frame(show, hide):
    hide.pack_forget()
    show.pack(fill="both", expand=True)

def main():
    # set root widget
    root = tk.Tk()
    root.geometry("500x350")
    root.title("Corporate Buddy")
    root.configure(background="#FFFFFF")
    root.resizable(False, False)

    # =====================    MAIN FRAME  ============================= 
    main_frame = tk.Frame(root)
    main_frame.configure(bg="white")

    # set the text
    label = tk.Label(main_frame, 
                     text="🇵🇭 Corporate Buddy", 
                     font=("Arial", 21, "bold"), 
                     bg="white")
    label.pack(pady=20)

    # set the buttons
    for i in ["Tax Calculator", "Setup Your Government Contributions", "Others"]:
        button = tk.Button(main_frame,
                        text=i, 
                        font=("Arial", 11, "bold"), 
                        width=10,
                        relief="raised",
                        bg="#a9d6e5",
                        activebackground="white",
                        activeforeground="#a9d6e5",
                        fg="white",
                        command=lambda: switch_frame(val_frame, main_frame),
                        cursor="hand2",
                        bd=0,
                        padx=20)
        button.pack(pady=8)

    # =====================    VALIDATION FRAME  =============================  
    val_frame = tk.Frame(root)
    val_frame.config(bg="white")
    label = tk.Label(val_frame, text="Hello World", bg="white")
    label.pack()
    button = tk.Button(val_frame,
                        text="⬅️ Return to Menu", 
                        font=("Arial", 11, "bold"), 
                        width=13,
                        relief="raised",
                        bg="#a9d6e5",
                        activebackground="white",
                        activeforeground="#a9d6e5",
                        fg="white",
                        command=lambda: switch_frame(main_frame, val_frame),
                        cursor="hand2",
                        bd=0,
                        padx=30)
    button.pack(pady=20, side="bottom")

    # run the GUI
    main_frame.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()