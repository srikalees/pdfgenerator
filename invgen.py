from tkinter import *
from fpdf import FPDF
window=Tk()
window.title("Invoice Generator")
medicines={
   "medicine A": 10,
   "medicine B": 20,
   "medicine C": 15,
   "medicine D": 25,
}
invoice_items =[]
total=0.0
def add_medicine():
    selected_medicine=medicine_listbox.get(ANCHOR)
    if selected_medicine:
      quantity=int(quantity_entry.get())
      price= medicines[selected_medicine]
      item_total=price*quantity
      invoice_items.append((selected_medicine,quantity,item_total))
      total_amount_entry.delete(0,END)
      total_amount_entry.insert(END,str(calculate_total()))
   # print(invoice_items)

    update_invoice_text()
def calculate_total():
    total=0.0
    for item in invoice_items:
        total=total+item[2]
    return total
def update_invoice_text():
    invoice_text.delete(1.0,END)
    for item in invoice_items:
        invoice_text.insert(END,f"medicine{item[0]},Quantity:{item[1]},Total{item[2]}\n")

def generate_invoice():
    customer_name =customer_entry.get()
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica",size=12)

    pdf.cell(0,10,text="Invoice",new_x="LMARGIN",new_y="NEXT",align="C")
    pdf.cell(0,10,text="Customer:"+customer_name,new_x="LMARGIN",new_y="NEXT",align="L")
    pdf.cell(0,10,text="",new_x="LMARGIN",new_y="NEXT")

    for item in invoice_items:
        medicine_name,quantity,item_total = item
        pdf.cell(0, 10, text=f"Medicine:{medicine_name},Quantity:{quantity}, Total:{item_total}",new_x="LMARGIN",new_y="NEXT",align="L")

        pdf.cell(0, 10, text="Total Amount"+str(calculate_total()), new_x="LMARGIN", new_y="NEXT",align="L")
        pdf.output("invoice.pdf")

medicine_label=Label(window,text="medicine:")
medicine_label.pack()

medicine_listbox=Listbox(window,selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END,medicine )
medicine_listbox.pack()

quantity_label=Label(window,text="Quantity:")
quantity_label.pack()
quantity_entry=Entry(window)
quantity_entry.pack()

add_button=Button(window,text="Add Medicine",command=add_medicine)
add_button.pack()


total_amount_label=Label(window,text="Total Amount")
total_amount_label.pack()
total_amount_entry=Entry(window)
total_amount_entry.pack()


customer_label=Label(window,text="customer Name:")
customer_label.pack()
customer_entry=Entry(window)
customer_entry.pack()

generate_button = Button(window,text="Generate Invoice",command=generate_invoice)
generate_button.pack()

invoice_text=Text(window,height=10,width=50)
invoice_text.pack()

window.mainloop()