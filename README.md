# Hospital Patient & Doctor Management System 🏥🩺

A robust, fully object-oriented console application built in Python to simulate a comprehensive hospital administration database. This system seamlessly orchestrates interactions between Patient registration, Doctor profiles, active Availability statuses, and dynamic Appointment logistics through an interactive command-line menu.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Dynamic Doctor Registry:** Log medical consultants along with their specialized departments and monitor their deployment status (`Available` vs `On Leave`) in real-time.
*   **Patient Registration:** Easily build new tracking profiles recording demographic fields alongside specific diagnosed diseases.
*   **Smart Appointment Engine:** Implements cross-reference relational validation checks:
    *   Rejects bookings if the target **Patient ID does not exist**.
    *   Blocks scheduling if the chosen **Doctor ID is missing or currently On Leave**.
*   **Stateful Cancellations:** Safely flip active scheduling workflows to a `Cancelled` state by identifying unique transaction records.
*   **Unified System Database Dashboard:** Features an overview matrix compiling aggregated records of all doctors, active patients, and upcoming bookings side by side.

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This codebase focuses on modularity, high cohesion, and scalable system interactions:
*   **Classes & Blueprints:** Modeled distinct physical entities using independent structural units: `Patient`, `Doctor`, `Appointment`, and `HospitalManagement`.
*   **Composition & Aggregation:** The master controller class (`HospitalManagement`) holds active internal object arrays (`patients_list`, `doctors_list`, `appointments_list`), beautifully illustrating how multiple runtime systems interact.
*   **Encapsulation & State Management:** Protects entity values and alters sensitive data paths (like a doctor's availability toggles or booking statuses) through specific, validated class methods rather than modifying properties blindly from the outside.

---

## 🚀 How to Run and Test

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd hospital-management-oop
    ```
3.  **Run the interactive menu script:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   Python 3.x installed on your machine.
