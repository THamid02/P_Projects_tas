"""Python Script to automate bank reconciliation"""
# importing necessary modules
import tkinter as tk

import numpy as np
import pandas as pd
import tabula

# creating entry widget to receive info from user
window = tk.Tk()
window.geometry("800x800")
window.title("Bank Reconciliation System")

def getvals():
    """Checking the rows of the file and remarking them"""
    text_area = tk.Text(master=window, height=400, width=300)
    text_area.grid(row=4, column=2)
    print("Submitting form")
    table_file = e1.get()
    output_csv = r"H:\Python\bank_copy.csv"
    df = tabula.read_pdf(table_file, pages="all", pandas_options={"header": None})[0]
    print("The pdf file")
    print(df)
    # converting PDF into CSV
    tabula.convert_into(table_file, output_csv, output_format="csv", pages="all")
    DF = pd.read_csv(
        output_csv,
        names=[
            "Serial",
            "Cheque_No",
            "C_Issue_Date",
            "Transfer_Date",
            "Issued_Amount",
            "Bank_Paid",
        ],
    )
    print("The csv file")
    print(DF)
    # remarking the lines
    conditions = [
        DF["Issued_Amount"] == DF["Bank_Paid"],
        DF["Issued_Amount"] >= DF["Bank_Paid"],
        DF["Issued_Amount"] <= DF["Bank_Paid"],
    ]
    choices = ["Ok", "To be reconciled", "To be reconciled"]
    # DF['Remarks'] = np.select(conditions, choices, default = 'No Value')
    DF.insert(6, "Remarks", value=np.select(conditions, choices, default="No Value"))
    print("The csv file with remarks")
    print(DF)
    # calculating the totals and mismatched account
    total_issue = 0.0
    total_bank = 0.0
    reconcile_amount = []
    total_issue = DF["Issued_Amount"].sum()
    print("Total Issued Amount by company(in Tk.): ", total_issue)
    total_bank = DF["Bank_Paid"].sum()
    print("Total Paid Amount by bank(in Tk.): ", total_bank)
    print("Needs to be reconciled ")
    text_area.insert(tk.END, "Needs to be reconciled:\n")
    recon_acc = []
    for i, d in DF.iterrows():
        if pd.isna(d["Bank_Paid"]) or (d["Issued_Amount"] != d["Bank_Paid"]):
            recon_acc.append(d["Cheque_No"])
            print(d["Cheque_No"], "\t")
        if d["Remarks"] == "Ok":
            reconcile_amount.append(d["Bank_Paid"])
            ##DF.style.applymap('green', subset=['Remarks'])
        ##else: DF.style.applymap('red', subset=['Remarks'])
    text_area.insert(tk.END, recon_acc)
    print("Bank Reconciled Amount(in Tk): ", sum(reconcile_amount))
    # DF.to_csv(output_csv, index=None)
    e2 = "\n\n\nFinal Report:\n\nTotal Issued Amount by company(Tk.): {issue}\n\nTotal Paid Amount by bank(Tk.): {bank}\n\nBank Reconciled Amount(Tk): {recon}".format(
        issue=total_issue, bank=total_bank, recon=sum(reconcile_amount)
    )
    text_area.insert(tk.END, e2)
    # converting the file
    DF.to_csv(output_csv, index=None)


# showing the output in text widget
e1 = tk.StringVar()
tk.Label(window, text="File Path").grid(row=0)
e1 = tk.Entry(window)
e1.grid(row=0, column=1)
tk.Button(text="Reconcile", command=getvals).grid(row=3)
window.mainloop()

