
import tkinter as tk

# Sample data structure to store student details
student_details = {
    "4207": {
        "Name": "Malathidevi",
        "Age": 18,
        "Branch": "Computer Science",
        "Gmail": 'tulasidevi@gmail.com',
        "Phn num":'9652780403',
        "Birthday":'26/02/2004',
        "Addres":'Markondapadu,West godavari district,1-36'
    },
    "4208": {
        "Name": "Tulasidevi",
        "Age": 19,
        "Branch": "Electrical Engineering",
        "Gmail": 'madhutammireddy@gmail.com',
        "Phn num":9392301433,
        "Birthday":'21/09/2001',
        "Addres":'Rajamundry,East godavari district,2-96'
    },
    "4209": {
        "Name": "Kumari",
        "Age": 20,
        "Branch": "Mechanical Science",
        "Gmail": 'kumari246@gmail.com',
        "Phn num":'8985989921',
        "Birthday":'15/08/2000',
        "Addres":'Kovvuru,West godavari district,9-74'
    },
     "4210": {
        "Name": "Subbarao",
        "Age": 18,
        "Branch": "Civil",
        "Gmail": 'subbarao234@gmail.com',
        "Phn num":'9493787794',
        "Birthday":'16/06/2004',
        "Addres":'Tallapudi,West godavari district,6-98'
     },
    "4211": {
        "Name": "Nagesh",
        "Age": 20,
        "Branch": "Mechine learning",
        "Gmail": 'Nagesh123@gmail.com',
        "Phn num":'9652994999',
        "Birthday":'09/02/2000',
        "Addres":'nidadavole,West godavari district,25-85'
     },
}


def display_student_details():
    student_id = entry_id.get()
    if student_id in student_details:
        details = student_details[student_id]
        output_label.config(text=f"Name: {details['Name']}\nAge: {details['Age']}\nBranch: {details['Branch']}\nGmail: {details['Gmail']}\nPhn num:{details['Phn num']}\nBirthday: {details['Birthday']}\nAddres: {details['Addres']}")
    else:
        output_label.config(text="Student not found.")

# Create the main application window
root = tk.Tk()
root.title("Student Details")

# Create input widgets
label_id = tk.Label(root, text="Enter Student ID:",width=100)
label_id.pack()

entry_id = tk.Entry(root)
entry_id.pack()

submit_button = tk.Button(root, text="Submit", command=display_student_details,width=25)
submit_button.pack()

# Create the output label
output_label = tk.Label(root, text="", justify=tk.LEFT)
output_label.pack()

# Start the application event loop
root.mainloop()