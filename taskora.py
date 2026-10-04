import tkinter as tk
from tkinter import messagebox


class TaskoraApp:

    def __init__(self, root):

        self.root = root
        self.root.title("TASKORA | Smart To-Do List")
        self.root.geometry("1100x700")
        self.root.configure(bg="#F4F7FB")
        self.root.minsize(900, 600)

        # COLORS

        self.primary = "#6C63FF"
        self.dark = "#24243E"
        self.pink = "#FF6584"
        self.green = "#32C48D"
        self.yellow = "#FFB703"
        self.white = "#FFFFFF"
        self.light_bg = "#F4F7FB"

        # TASK LIST

        self.tasks = []

        # MAIN FRAME

        self.main_frame = tk.Frame(
            root,
            bg=self.light_bg
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        self.create_sidebar()
        self.create_content()


    # =====================================
    # SIDEBAR
    # =====================================

    def create_sidebar(self):

        sidebar = tk.Frame(
            self.main_frame,
            bg=self.dark,
            width=250
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        sidebar.pack_propagate(False)


        # LOGO

        logo_canvas = tk.Canvas(
            sidebar,
            width=90,
            height=90,
            bg=self.dark,
            highlightthickness=0
        )

        logo_canvas.pack(
            pady=(40, 10)
        )

        logo_canvas.create_oval(
            8,
            8,
            82,
            82,
            fill=self.primary,
            outline=""
        )

        logo_canvas.create_text(
            45,
            45,
            text="T",
            font=("Arial", 32, "bold"),
            fill="white"
        )


        # APP NAME

        tk.Label(
            sidebar,
            text="TASKORA",
            font=("Arial", 24, "bold"),
            bg=self.dark,
            fg="white"
        ).pack()


        tk.Label(
            sidebar,
            text="Your Productivity Space",
            font=("Arial", 10),
            bg=self.dark,
            fg="#B5B5C8"
        ).pack(
            pady=(5, 40)
        )


        # MENU

        self.create_menu_button(
            sidebar,
            "Dashboard",
            self.primary
        )

        self.create_menu_button(
            sidebar,
            "My Tasks",
            self.dark
        )

        self.create_menu_button(
            sidebar,
            "Completed",
            self.dark
        )


        # QUOTE SECTION

        quote_frame = tk.Frame(
            sidebar,
            bg="#353550"
        )

        quote_frame.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=30
        )


        tk.Label(
            quote_frame,
            text="DAILY MOTIVATION",
            font=("Arial", 9, "bold"),
            bg="#353550",
            fg=self.yellow
        ).pack(
            pady=(15, 8)
        )


        tk.Label(
            quote_frame,
            text="Small steps every day\nlead to big results.",
            font=("Arial", 10, "bold"),
            bg="#353550",
            fg="white",
            justify="center"
        ).pack(
            pady=(0, 15)
        )


    # =====================================
    # MENU BUTTON
    # =====================================

    def create_menu_button(
            self,
            parent,
            text,
            color
    ):

        button = tk.Button(
            parent,
            text=text,
            font=("Arial", 11),
            bg=color,
            fg="white",
            activebackground=self.primary,
            activeforeground="white",
            relief="flat",
            anchor="w",
            padx=25,
            pady=12,
            cursor="hand2"
        )

        button.pack(
            fill="x",
            padx=15,
            pady=5
        )


    # =====================================
    # MAIN CONTENT
    # =====================================

    def create_content(self):

        content = tk.Frame(
            self.main_frame,
            bg=self.light_bg
        )

        content.pack(
            side="left",
            fill="both",
            expand=True
        )


        # HEADER

        header = tk.Frame(
            content,
            bg=self.light_bg
        )

        header.pack(
            fill="x",
            padx=40,
            pady=(30, 15)
        )


        tk.Label(
            header,
            text="Good Morning!",
            font=("Arial", 28, "bold"),
            bg=self.light_bg,
            fg=self.dark
        ).pack(
            anchor="w"
        )


        tk.Label(
            header,
            text="Let's make today productive and meaningful.",
            font=("Arial", 11),
            bg=self.light_bg,
            fg="#777777"
        ).pack(
            anchor="w",
            pady=5
        )


        # STATISTICS

        stats_frame = tk.Frame(
            content,
            bg=self.light_bg
        )

        stats_frame.pack(
            fill="x",
            padx=35,
            pady=10
        )


        self.total_number = self.create_stat_card(
            stats_frame,
            "TOTAL TASKS",
            "T",
            self.primary
        )


        self.pending_number = self.create_stat_card(
            stats_frame,
            "PENDING",
            "P",
            self.yellow
        )


        self.completed_number = self.create_stat_card(
            stats_frame,
            "COMPLETED",
            "C",
            self.green
        )


        # ADD TASK AREA

        self.create_add_task_section(content)


        # SEARCH SECTION

        search_frame = tk.Frame(
            content,
            bg=self.light_bg
        )

        search_frame.pack(
            fill="x",
            padx=40,
            pady=(10, 5)
        )


        self.search_var = tk.StringVar()


        self.search_var.trace_add(
            "write",
            lambda *args: self.display_tasks()
        )


        search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 11),
            bd=1,
            relief="solid",
            bg="white",
            fg="#555555"
        )

        search_entry.pack(
            fill="x",
            ipady=12
        )


        # TASK TITLE

        tk.Label(
            content,
            text="My Tasks",
            font=("Arial", 18, "bold"),
            bg=self.light_bg,
            fg=self.dark
        ).pack(
            anchor="w",
            padx=40,
            pady=(15, 10)
        )


        # TASK DISPLAY AREA

        self.task_container = tk.Frame(
            content,
            bg=self.light_bg
        )

        self.task_container.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=(0, 20)
        )


        self.display_tasks()


    # =====================================
    # STATISTICS CARD
    # =====================================

    def create_stat_card(
            self,
            parent,
            title,
            icon,
            color
    ):

        card = tk.Frame(
            parent,
            bg="white",
            width=200,
            height=110
        )

        card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=8
        )

        card.pack_propagate(False)


        icon_label = tk.Label(
            card,
            text=icon,
            font=("Arial", 20, "bold"),
            bg=color,
            fg="white",
            width=3
        )

        icon_label.place(
            x=15,
            y=20
        )


        number_label = tk.Label(
            card,
            text="0",
            font=("Arial", 24, "bold"),
            bg="white",
            fg=self.dark
        )

        number_label.place(
            x=85,
            y=18
        )


        tk.Label(
            card,
            text=title,
            font=("Arial", 9, "bold"),
            bg="white",
            fg="#888888"
        ).place(
            x=85,
            y=60
        )


        return number_label


    # =====================================
    # ADD TASK SECTION
    # =====================================

    def create_add_task_section(self, parent):

        add_card = tk.Frame(
            parent,
            bg="white",
            highlightbackground="#E5E5E5",
            highlightthickness=1
        )

        add_card.pack(
            fill="x",
            padx=40,
            pady=20
        )


        tk.Label(
            add_card,
            text="CREATE A NEW TASK",
            font=("Arial", 14, "bold"),
            bg="white",
            fg=self.dark
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )


        input_frame = tk.Frame(
            add_card,
            bg="white"
        )

        input_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )


        self.task_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            bd=1,
            relief="solid"
        )

        self.task_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=10
        )


        self.task_entry.bind(
            "<Return>",
            lambda event: self.add_task()
        )


        # PRIORITY

        self.priority = tk.StringVar()
        self.priority.set("Medium")


        priority_menu = tk.OptionMenu(
            input_frame,
            self.priority,
            "Low",
            "Medium",
            "High"
        )

        priority_menu.config(
            bg="#F0EFFF",
            fg=self.primary,
            bd=0
        )

        priority_menu.pack(
            side="left",
            padx=10
        )


        # ADD BUTTON

        add_button = tk.Button(
            input_frame,
            text="ADD TASK",
            font=("Arial", 11, "bold"),
            bg=self.primary,
            fg="white",
            activebackground="#554DCC",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.add_task
        )

        add_button.pack(
            side="right"
        )


    # =====================================
    # ADD TASK
    # =====================================

    def add_task(self):

        task_name = self.task_entry.get().strip()


        if task_name == "":

            messagebox.showwarning(
                "Taskora",
                "Please enter a task first!"
            )

            return


        new_task = {

            "name": task_name,
            "priority": self.priority.get(),
            "completed": False

        }


        self.tasks.append(new_task)


        self.task_entry.delete(
            0,
            tk.END
        )


        self.display_tasks()
        self.update_statistics()


    # =====================================
    # DISPLAY TASKS
    # =====================================

    def display_tasks(self):

        for widget in self.task_container.winfo_children():

            widget.destroy()


        search_text = self.search_var.get().lower()


        found = False


        for index, task in enumerate(self.tasks):

            if search_text not in task["name"].lower():

                continue


            found = True


            self.create_task_card(
                index,
                task
            )


        if not found:

            tk.Label(
                self.task_container,
                text="No tasks available.\nCreate your first task to begin!",
                font=("Arial", 12),
                bg=self.light_bg,
                fg="#888888",
                justify="center"
            ).pack(
                pady=30
            )


    # =====================================
    # TASK CARD
    # =====================================

    def create_task_card(
            self,
            index,
            task
    ):

        task_frame = tk.Frame(
            self.task_container,
            bg="white",
            height=70
        )

        task_frame.pack(
            fill="x",
            pady=5
        )

        task_frame.pack_propagate(False)


        colors = {

            "Low": self.green,
            "Medium": self.yellow,
            "High": self.pink

        }


        # PRIORITY STRIP

        tk.Frame(
            task_frame,
            bg=colors[task["priority"]],
            width=7
        ).pack(
            side="left",
            fill="y"
        )


        # COMPLETE BUTTON

        button_text = "DONE" if task["completed"] else "MARK"


        check_button = tk.Button(
            task_frame,
            text=button_text,
            font=("Arial", 8, "bold"),
            bg="white",
            fg=self.green,
            bd=0,
            cursor="hand2",
            command=lambda i=index: self.toggle_task(i)
        )

        check_button.pack(
            side="left",
            padx=15
        )


        # TASK TEXT

        if task["completed"]:

            task_color = "#AAAAAA"
            task_font = ("Arial", 11, "overstrike")

        else:

            task_color = self.dark
            task_font = ("Arial", 11, "bold")


        tk.Label(
            task_frame,
            text=task["name"],
            font=task_font,
            bg="white",
            fg=task_color,
            anchor="w"
        ).pack(
            side="left",
            fill="x",
            expand=True
        )


        # PRIORITY LABEL

        tk.Label(
            task_frame,
            text=task["priority"],
            font=("Arial", 9, "bold"),
            bg=colors[task["priority"]],
            fg="white",
            padx=10,
            pady=4
        ).pack(
            side="left",
            padx=10
        )


        # DELETE BUTTON

        delete_button = tk.Button(
            task_frame,
            text="DELETE",
            font=("Arial", 8, "bold"),
            bg="#FFF0F2",
            fg=self.pink,
            bd=0,
            cursor="hand2",
            command=lambda i=index: self.delete_task(i)
        )

        delete_button.pack(
            side="right",
            padx=15
        )


    # =====================================
    # COMPLETE TASK
    # =====================================

    def toggle_task(self, index):

        self.tasks[index]["completed"] = (

            not self.tasks[index]["completed"]

        )


        self.display_tasks()
        self.update_statistics()


    # =====================================
    # DELETE TASK
    # =====================================

    def delete_task(self, index):

        answer = messagebox.askyesno(
            "Delete Task",
            "Do you want to delete this task?"
        )


        if answer:

            del self.tasks[index]

            self.display_tasks()
            self.update_statistics()


    # =====================================
    # UPDATE STATISTICS
    # =====================================

    def update_statistics(self):

        total = len(self.tasks)


        completed = sum(

            task["completed"]

            for task in self.tasks

        )


        pending = total - completed


        self.total_number.config(
            text=str(total)
        )


        self.pending_number.config(
            text=str(pending)
        )


        self.completed_number.config(
            text=str(completed)
        )


# =====================================
# RUN APPLICATION
# =====================================

if __name__ == "__main__":

    root = tk.Tk()

    app = TaskoraApp(root)

    root.mainloop()