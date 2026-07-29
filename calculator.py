import tkinter as tk


class CalculatorApp:

    def __init__(self, root):

        self.root = root

        # =========================
        # MAIN WINDOW
        # =========================

        self.root.title("All-in-One Calculator")
        self.root.geometry("430x720")
        self.root.resizable(False, False)

        # =========================
        # DISPLAY FRAME
        # =========================

        display_frame = tk.Frame(
            root,
            bd=5,
            relief="sunken"
        )

        display_frame.pack(
            fill="both",
            padx=15,
            pady=20
        )

        # Expression display
        self.display = tk.Entry(
            display_frame,
            font=("Arial", 25),
            justify="right",
            bd=0
        )

        self.display.pack(
            fill="x",
            padx=10,
            pady=(10, 0),
            ipady=5
        )

        # Live result preview
        self.result_display = tk.Label(
            display_frame,
            text="",
            font=("Arial", 20),
            anchor="e"
        )

        self.result_display.pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )

        # Whenever the user types, update the answer
        self.display.bind(
            "<KeyRelease>",
            self.live_result
        )

        # =========================
        # BUTTON FRAME
        # =========================

        button_frame = tk.Frame(root)

        button_frame.pack(
            padx=10,
            pady=5
        )

        # =========================
        # BUTTONS
        # =========================

        buttons = [

            ("AC", 0, 0),
            ("⌫", 0, 1),
            ("%", 0, 2),
            ("÷", 0, 3),

            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("×", 1, 3),

            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("−", 2, 3),

            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("+", 3, 3),

            ("0", 4, 0),
            (".", 4, 1),
            ("(", 4, 2),
            (")", 4, 3),

            ("=", 5, 0),
            ("SI", 5, 1),
            ("MENU", 5, 2),
            ("EXIT", 5, 3)
        ]

        for text, row, column in buttons:

            if text == "AC":
                command = self.clear

            elif text == "⌫":
                command = self.delete

            elif text == "=":
                command = self.calculate

            elif text == "SI":
                command = self.simple_interest

            elif text == "MENU":
                command = self.open_menu

            elif text == "EXIT":
                command = self.root.destroy

            else:
                command = lambda value=text: self.click(value)

            button = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 16, "bold"),
                width=6,
                height=2,
                command=command
            )

            button.grid(
                row=row,
                column=column,
                padx=5,
                pady=5
            )


    # =========================================================
    # MAIN CALCULATOR
    # =========================================================

    def click(self, value):

        # Convert mobile symbols to Python operators

        if value == "×":
            value = "*"

        elif value == "÷":
            value = "/"

        elif value == "−":
            value = "-"

        self.display.insert(
            tk.END,
            value
        )

        self.live_result()


    # =========================================================
    # LIVE ANSWER
    # =========================================================

    def live_result(self, event=None):

        expression = self.display.get()

        if expression == "":
            self.result_display.config(
                text=""
            )
            return

        try:

            # Calculate expression
            result = eval(
                expression,
                {
                    "__builtins__": None
                },
                {}
            )

            self.result_display.config(
                text=str(result)
            )

        except:

            # Don't show error while expression is incomplete
            self.result_display.config(
                text=""
            )


    # =========================================================
    # CLEAR
    # =========================================================

    def clear(self):

        self.display.delete(
            0,
            tk.END
        )

        self.result_display.config(
            text=""
        )


    # =========================================================
    # DELETE
    # =========================================================

    def delete(self):

        current = self.display.get()

        self.display.delete(
            0,
            tk.END
        )

        self.display.insert(
            0,
            current[:-1]
        )

        self.live_result()


    # =========================================================
    # EQUALS
    # =========================================================

    def calculate(self):

        expression = self.display.get()

        try:

            result = eval(
                expression,
                {
                    "__builtins__": None
                },
                {}
            )

            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                str(result)
            )

            self.result_display.config(
                text=""
            )

        except:

            self.result_display.config(
                text="Error"
            )


    # =========================================================
    # MENU
    # =========================================================

    def open_menu(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Calculator Menu"
        )

        window.geometry(
            "400x620"
        )

        window.resizable(
            False,
            False
        )

        tk.Label(
            window,
            text="Calculator Menu",
            font=("Arial", 22, "bold")
        ).pack(
            pady=20
        )

        menu_items = [

            (
                "Arithmetic Operators",
                self.arithmetic_window
            ),

            (
                "Assignment Operators",
                self.assignment_window
            ),

            (
                "Comparison Operators",
                self.comparison_window
            ),

            (
                "Logical Operators",
                self.logical_window
            ),

            (
                "Bitwise Operators",
                self.bitwise_window
            ),

            (
                "Number System Conversion",
                self.number_system_window
            ),

            (
                "1's & 2's Complement",
                self.complement_window
            ),

            (
                "Simple Interest",
                self.simple_interest
            )
        ]

        for text, command in menu_items:

            tk.Button(
                window,
                text=text,
                font=("Arial", 14, "bold"),
                width=28,
                height=2,
                command=command
            ).pack(
                pady=5
            )


    # =========================================================
    # ARITHMETIC OPERATORS
    # =========================================================

    def arithmetic_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Arithmetic Operators"
        )

        window.geometry(
            "400x450"
        )

        tk.Label(
            window,
            text="Arithmetic Operators",
            font=("Arial", 20, "bold")
        ).pack(
            pady=20
        )

        tk.Label(
            window,
            text="Enter Expression\nExample: 10 + 5 * 2",
            font=("Arial", 13)
        ).pack()

        entry = tk.Entry(
            window,
            font=("Arial", 20),
            width=20
        )

        entry.pack(
            pady=15
        )

        result_label = tk.Label(
            window,
            text="Result:",
            font=("Arial", 16)
        )

        result_label.pack(
            pady=10
        )


        def calculate_arithmetic():

            try:

                result = eval(
                    entry.get(),
                    {
                        "__builtins__": None
                    },
                    {}
                )

                result_label.config(
                    text=f"Result: {result}"
                )

            except:

                result_label.config(
                    text="Invalid Expression"
                )


        tk.Button(
            window,
            text="Calculate",
            font=("Arial", 14, "bold"),
            command=calculate_arithmetic
        ).pack(
            pady=10
        )

        tk.Label(
            window,
            text="+ Addition\n"
                 "- Subtraction\n"
                 "* Multiplication\n"
                 "/ Division\n"
                 "% Modulus\n"
                 "// Floor Division\n"
                 "** Exponent",
            font=("Arial", 12)
        ).pack(
            pady=10
        )


    # =========================================================
    # ASSIGNMENT OPERATORS
    # =========================================================

    def assignment_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Assignment Operators"
        )

        window.geometry(
            "400x500"
        )

        tk.Label(
            window,
            text="Assignment Operators",
            font=("Arial", 20, "bold")
        ).pack(
            pady=20
        )

        tk.Label(
            window,
            text="First Value"
        ).pack()

        first = tk.Entry(
            window,
            font=("Arial", 16)
        )

        first.pack(
            pady=8
        )

        tk.Label(
            window,
            text="Select Operator"
        ).pack()

        operator_var = tk.StringVar()

        operator_var.set(
            "+="
        )

        operators = [
            "+=",
            "-=",
            "*=",
            "/=",
            "%=",
            "**=",
            "//="
        ]

        tk.OptionMenu(
            window,
            operator_var,
            *operators
        ).pack(
            pady=10
        )

        tk.Label(
            window,
            text="Second Value"
        ).pack()

        second = tk.Entry(
            window,
            font=("Arial", 16)
        )

        second.pack(
            pady=8
        )

        result_label = tk.Label(
            window,
            text="Result:",
            font=("Arial", 16)
        )

        result_label.pack(
            pady=15
        )


        def calculate_assignment():

            try:

                a = float(
                    first.get()
                )

                b = float(
                    second.get()
                )

                op = operator_var.get()

                if op == "+=":
                    result = a + b

                elif op == "-=":
                    result = a - b

                elif op == "*=":
                    result = a * b

                elif op == "/=":
                    result = a / b

                elif op == "%=":
                    result = a % b

                elif op == "**=":
                    result = a ** b

                elif op == "//=":
                    result = a // b

                result_label.config(
                    text=f"Result: {result}"
                )

            except:

                result_label.config(
                    text="Invalid Input"
                )


        tk.Button(
            window,
            text="Calculate",
            font=("Arial", 14, "bold"),
            command=calculate_assignment
        ).pack()


    # =========================================================
    # COMPARISON OPERATORS
    # =========================================================

    def comparison_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Comparison Operators"
        )

        window.geometry(
            "400x450"
        )

        tk.Label(
            window,
            text="Comparison Operators",
            font=("Arial", 20, "bold")
        ).pack(
            pady=20
        )

        first = tk.Entry(
            window,
            font=("Arial", 16)
        )

        first.pack(
            pady=10
        )

        operator_var = tk.StringVar()

        operator_var.set(
            "=="
        )

        operators = [
            "==",
            "!=",
            ">",
            "<",
            ">=",
            "<="
        ]

        tk.OptionMenu(
            window,
            operator_var,
            *operators
        ).pack(
            pady=10
        )

        second = tk.Entry(
            window,
            font=("Arial", 16)
        )

        second.pack(
            pady=10
        )

        result_label = tk.Label(
            window,
            text="Result:",
            font=("Arial", 16)
        )

        result_label.pack(
            pady=15
        )


        def compare():

            try:

                a = float(
                    first.get()
                )

                b = float(
                    second.get()
                )

                op = operator_var.get()

                if op == "==":
                    result = a == b

                elif op == "!=":
                    result = a != b

                elif op == ">":
                    result = a > b

                elif op == "<":
                    result = a < b

                elif op == ">=":
                    result = a >= b

                elif op == "<=":
                    result = a <= b

                result_label.config(
                    text=f"Result: {result}"
                )

            except:

                result_label.config(
                    text="Invalid Input"
                )


        tk.Button(
            window,
            text="Compare",
            font=("Arial", 14, "bold"),
            command=compare
        ).pack()


    # =========================================================
    # LOGICAL OPERATORS
    # =========================================================

    def logical_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Logical Operators"
        )

        window.geometry(
            "400x450"
        )

        tk.Label(
            window,
            text="Logical Operators",
            font=("Arial", 20, "bold")
        ).pack(
            pady=20
        )

        tk.Label(
            window,
            text="Enter 0 or 1"
        ).pack()

        first = tk.Entry(
            window,
            font=("Arial", 16)
        )

        first.pack(
            pady=10
        )

        operator_var = tk.StringVar()

        operator_var.set(
            "and"
        )

        operators = [
            "and",
            "or"
        ]

        tk.OptionMenu(
            window,
            operator_var,
            *operators
        ).pack(
            pady=10
        )

        second = tk.Entry(
            window,
            font=("Arial", 16)
        )

        second.pack(
            pady=10
        )

        result_label = tk.Label(
            window,
            text="Result:",
            font=("Arial", 16)
        )

        result_label.pack(
            pady=15
        )


        def logical():

            try:

                a = bool(
                    int(first.get())
                )

                b = bool(
                    int(second.get())
                )

                op = operator_var.get()

                if op == "and":
                    result = a and b

                else:
                    result = a or b

                result_label.config(
                    text=f"Result: {result}"
                )

            except:

                result_label.config(
                    text="Enter only 0 or 1"
                )


        tk.Button(
            window,
            text="Calculate",
            font=("Arial", 14, "bold"),
            command=logical
        ).pack()


    # =========================================================
    # BITWISE OPERATORS
    # =========================================================

    def bitwise_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Bitwise Operators"
        )

        window.geometry(
            "400x500"
        )

        tk.Label(
            window,
            text="Bitwise Operators",
            font=("Arial", 20, "bold")
        ).pack(
            pady=20
        )

        first = tk.Entry(
            window,
            font=("Arial", 16)
        )

        first.pack(
            pady=10
        )

        operator_var = tk.StringVar()

        operator_var.set(
            "&"
        )

        operators = [
            "&",
            "|",
            "^",
            "<<",
            ">>"
        ]

        tk.OptionMenu(
            window,
            operator_var,
            *operators
        ).pack(
            pady=10
        )

        second = tk.Entry(
            window,
            font=("Arial", 16)
        )

        second.pack(
            pady=10
        )

        result_label = tk.Label(
            window,
            text="Result:",
            font=("Arial", 16)
        )

        result_label.pack(
            pady=15
        )


        def bitwise():

            try:

                a = int(
                    first.get()
                )

                b = int(
                    second.get()
                )

                op = operator_var.get()

                if op == "&":
                    result = a & b

                elif op == "|":
                    result = a | b

                elif op == "^":
                    result = a ^ b

                elif op == "<<":
                    result = a << b

                elif op == ">>":
                    result = a >> b

                result_label.config(
                    text=f"Result: {result}"
                )

            except:

                result_label.config(
                    text="Invalid Input"
                )


        tk.Button(
            window,
            text="Calculate",
            font=("Arial", 14, "bold"),
            command=bitwise
        ).pack()


    # =========================================================
    # NUMBER SYSTEM
    # =========================================================

    def number_system_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Number System Conversion"
        )

        window.geometry(
            "450x550"
        )

        tk.Label(
            window,
            text="Number System Conversion",
            font=("Arial", 20, "bold")
        ).pack(
            pady=20
        )

        tk.Label(
            window,
            text="Enter Number",
            font=("Arial", 13)
        ).pack()

        number_entry = tk.Entry(
            window,
            font=("Arial", 18)
        )

        number_entry.pack(
            pady=10
        )

        base_var = tk.StringVar()

        base_var.set(
            "Decimal"
        )

        bases = [
            "Decimal",
            "Binary",
            "Octal",
            "Hexadecimal"
        ]

        tk.OptionMenu(
            window,
            base_var,
            *bases
        ).pack(
            pady=10
        )

        result_label = tk.Label(
            window,
            text="",
            font=("Arial", 14),
            justify="left"
        )

        result_label.pack(
            pady=20
        )


        def convert():

            try:

                number = number_entry.get()

                base = base_var.get()

                if base == "Decimal":

                    decimal = int(
                        number,
                        10
                    )

                elif base == "Binary":

                    decimal = int(
                        number,
                        2
                    )

                elif base == "Octal":

                    decimal = int(
                        number,
                        8
                    )

                else:

                    decimal = int(
                        number,
                        16
                    )

                result = (
                    f"Decimal: {decimal}\n\n"
                    f"Binary: {bin(decimal)}\n\n"
                    f"Octal: {oct(decimal)}\n\n"
                    f"Hexadecimal: {hex(decimal)}"
                )

                result_label.config(
                    text=result
                )

            except:

                result_label.config(
                    text="Invalid Number"
                )


        tk.Button(
            window,
            text="Convert",
            font=("Arial", 14, "bold"),
            command=convert
        ).pack()


    # =========================================================
    # 1'S AND 2'S COMPLEMENT
    # =========================================================

    def complement_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "1's & 2's Complement"
        )

        window.geometry(
            "450x500"
        )

        tk.Label(
            window,
            text="1's & 2's Complement",
            font=("Arial", 20, "bold")
        ).pack(
            pady=20
        )

        tk.Label(
            window,
            text="Enter Binary Number",
            font=("Arial", 13)
        ).pack()

        binary_entry = tk.Entry(
            window,
            font=("Arial", 18)
        )

        binary_entry.pack(
            pady=15
        )

        result_label = tk.Label(
            window,
            text="",
            font=("Arial", 14),
            justify="left"
        )

        result_label.pack(
            pady=20
        )


        def calculate_complement():

            try:

                binary = binary_entry.get()

                if not binary:

                    raise ValueError

                if not all(
                    bit in "01"
                    for bit in binary
                ):

                    raise ValueError

                # 1's complement

                ones = ""

                for bit in binary:

                    if bit == "0":

                        ones += "1"

                    else:

                        ones += "0"


                # 2's complement

                twos_value = (
                    int(ones, 2) + 1
                )

                twos = bin(
                    twos_value
                )[2:]

                twos = twos.zfill(
                    len(binary)
                )


                result_label.config(
                    text=(
                        f"Original: {binary}\n\n"
                        f"1's Complement: {ones}\n\n"
                        f"2's Complement: {twos}"
                    )
                )

            except:

                result_label.config(
                    text="Enter a valid binary number"
                )


        tk.Button(
            window,
            text="Calculate",
            font=("Arial", 14, "bold"),
            command=calculate_complement
        ).pack()


    # =========================================================
    # SIMPLE INTEREST
    # =========================================================

    def simple_interest(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Simple Interest"
        )

        window.geometry(
            "450x550"
        )

        tk.Label(
            window,
            text="Simple Interest Calculator",
            font=("Arial", 20, "bold")
        ).pack(
            pady=20
        )

        tk.Label(
            window,
            text="Principal Amount (P)"
        ).pack()

        principal = tk.Entry(
            window,
            font=("Arial", 16)
        )

        principal.pack(
            pady=10
        )

        tk.Label(
            window,
            text="Rate of Interest (R%)"
        ).pack()

        rate = tk.Entry(
            window,
            font=("Arial", 16)
        )

        rate.pack(
            pady=10
        )

        tk.Label(
            window,
            text="Time in Years (T)"
        ).pack()

        time = tk.Entry(
            window,
            font=("Arial", 16)
        )

        time.pack(
            pady=10
        )

        result_label = tk.Label(
            window,
            text="",
            font=("Arial", 15),
            justify="left"
        )

        result_label.pack(
            pady=20
        )


        def calculate_interest():

            try:

                p = float(
                    principal.get()
                )

                r = float(
                    rate.get()
                )

                t = float(
                    time.get()
                )

                # Simple Interest Formula

                si = (
                    p * r * t
                ) / 100

                # Total Amount

                total = (
                    p + si
                )

                result_label.config(
                    text=(
                        f"Simple Interest = {si}\n\n"
                        f"Total Amount = {total}"
                    )
                )

            except:

                result_label.config(
                    text="Enter valid numbers"
                )


        tk.Button(
            window,
            text="Calculate",
            font=("Arial", 14, "bold"),
            command=calculate_interest
        ).pack()


# =============================================================
# START APPLICATION
# =============================================================

root = tk.Tk()

app = CalculatorApp(
    root
)

root.mainloop()