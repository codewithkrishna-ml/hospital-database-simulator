#RPOJECT-Hospital Patient & Doctor Management System
class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def display_patient_details(self):
        print(f"Patient ID: {self.patient_id} | Name: {self.name} | Age: {self.age} | Gender: {self.gender} | Disease: {self.disease}")


class Doctor:
    def __init__(self, doctor_id, name, specialization, availability=True):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.availability = availability

    def display_doctor_details(self):
        status_str = "Available" if self.availability else "On Leave"
        print(f"Doctor ID: {self.doctor_id} | Name: {self.name} | Specialization: {self.specialization} | Status: {status_str}")

    def update_availability(self, status):
        self.availability = status
        if self.availability:
            print(f"Dr. {self.name} is now available.")
        else:
            print(f"Dr. {self.name} is now on leave.")


class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, appointment_date):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.status = "Scheduled"

    def display_appointment_details(self):
        print(f"Appointment ID: {self.appointment_id} | Patient ID: {self.patient_id} | Doctor ID: {self.doctor_id} | Date: {self.appointment_date} | Status: {self.status}")

    def cancel_appointment(self):
        self.status = "Cancelled"
        print(f"Appointment ID {self.appointment_id} has been cancelled successfully.")


class HospitalManagement:
    def __init__(self):
        self.patients_list = []
        self.doctors_list = []
        self.appointments_list = []

    def add_patient(self):
        print("\n--- Register New Patient ---")
        p_id = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        disease = input("Enter Disease: ")
        
        new_patient = Patient(p_id, name, age, gender, disease)
        self.patients_list.append(new_patient)
        print("Patient successfully registered.")

    def add_doctor(self):
        print("\n--- Add New Doctor ---")
        d_id = input("Enter Doctor ID: ")
        name = input("Enter Name: ")
        spec = input("Enter Specialization: ")
        
        new_doctor = Doctor(d_id, name, spec)
        self.doctors_list.append(new_doctor)
        print("Doctor successfully added to the hospital system.")

    def book_appointment(self):
        print("\n--- Book an Appointment ---")
        p_id = input("Enter Patient ID: ")
        
        patient_found = False
        for p in self.patients_list:
            if p.patient_id == p_id:
                patient_found = True
                break
        
        if not patient_found:
            print("Error: Patient ID not registered. Please register the patient first.")
            return 

        d_id = input("Enter Doctor ID: ")
        
        doctor_to_book = None
        for d in self.doctors_list:
            if d.doctor_id == d_id:
                doctor_to_book = d
                break
        
        if doctor_to_book is None:
            print("Error: Doctor ID not found in the system.")
            return
            
        if not doctor_to_book.availability:
            print(f"Sorry: Dr. {doctor_to_book.name} is on leave today.")
            return

        app_id = input("Enter a unique Appointment ID: ")
        app_date = input("Enter Date (DD-MM-YYYY): ")
        
        new_app = Appointment(app_id, p_id, d_id, app_date)
        self.appointments_list.append(new_app)
        print("Success: Appointment successfully booked.")

    def cancel_appointment_by_id(self):
        print("\n--- Cancel an Appointment ---")
        app_id = input("Enter Appointment ID to cancel: ")
        
        for app in self.appointments_list:
            if app.appointment_id == app_id:
                app.cancel_appointment()
                return
        print("Error: Appointment ID not found.")

    def update_doctor_status(self):
        print("\n--- Update Doctor Availability ---")
        d_id = input("Enter Doctor ID: ")
        
        for d in self.doctors_list:
            if d.doctor_id == d_id:
                choice = input("Is the doctor available? (yes/no): ").lower()
                status = True if choice == "yes" else False
                d.update_availability(status)
                return
        print("Error: Doctor ID not found.")

    def view_all_details(self):
        print("\n================ SYSTEM DATABASE ================")
        print("\n--- Registered Doctors ---")
        if not self.doctors_list: 
            print("No doctors registered yet.")
        for doc in self.doctors_list: 
            doc.display_doctor_details()
        
        print("\n--- Registered Patients ---")
        if not self.patients_list: 
            print("No patients registered yet.")
        for pat in self.patients_list: 
            pat.display_patient_details()
        
        print("\n--- Booked Appointments ---")
        if not self.appointments_list: 
            print("No appointments scheduled yet.")
        for app in self.appointments_list: 
            app.display_appointment_details()
        print("=================================================")


if __name__ == "__main__":
    hospital = HospitalManagement()

    while True:
        print("\n--- HOSPITAL MANAGEMENT SYSTEM MENU ---")
        print("1. Add New Doctor")
        print("2. Register New Patient")
        print("3. Book an Appointment")
        print("4. Cancel an Appointment")
        print("5. Update Doctor Leave Status")
        print("6. View Hospital Database (All Details)")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            hospital.add_doctor()
        elif choice == "2":
            hospital.add_patient()
        elif choice == "3":
            hospital.book_appointment()
        elif choice == "4":
            hospital.cancel_appointment_by_id()
        elif choice == "5":
            hospital.update_doctor_status()
        elif choice == "6":
            hospital.view_all_details()
        elif choice == "7":
            print("\nThank you for using the Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter a number between 1 and 7.")

