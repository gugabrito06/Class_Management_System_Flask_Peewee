# Class Management System (Flask & Peewee) 📚

This project consists in a full-stack web application built with Python and Flask to manage school logistics. This system simplifies the process of scheduling classes, managing users, and tracking student attendance through a dedicated role-based interface.<br><br>

Interface Preview
-

<table align="center" width="100%">
  <tr>
    <td align="center" width="33%">
      <img src="https://github.com/user-attachments/assets/abc81e74-f63f-4d85-9711-74448921f100" width="100%" />
      <br />
      <b>Login Page</b>
    </td>
    <td align="center" width="33%">
      <img src="https://github.com/user-attachments/assets/9ee3811a-081e-48d9-a73e-2943ad9d34f7" width="100%" />
      <br />
      <b>Admin Dashboard</b>
    </td>
    <td align="center" width="33%">
      <img src="https://github.com/user-attachments/assets/279b7d64-efde-43c9-9f56-8a2a18ac7af0" width="100%" />
      <br />
      <b>Teacher Dashboard</b>
    </td>
  </tr>
</table>
<br>


Key Features
-
**Administrator Dashboard:**

User Management: Create and manage Professor accounts with unique credentials.

Class Scheduling: Schedule classes and assign them to specific professors in the database.

Student Enrollment: Register students and enroll them in multiple classes simultaneously.
<br><br>


**Teacher Dashboard:**

Dynamic Access: Teachers only view the classes currently assigned to them.

Attendance Tracking: Real-time interface to mark students as present or absent.

Automatic Updates: Attendance records are synchronized with the database instantly.
<br><br>


**Technologies:**

Backend: Python, Flask

Database: SQLite (via Peewee ORM)

Frontend: HTML5, CSS3, Jinja2 Templates
<br><br>


🚀 Getting Started 
-
Follow these steps to set up and run the project locally.

**Prerequisites:**
- Ensure you have Python 3.x installed on your machine;
- Install Flask and Peewee.

**How to run the program:**
- Clone the repository;
- Run the application (app.py file) - The app will be available at: http://127.0.0.1:5000/

<div align="center">
  <figure>
    <img src="https://github.com/user-attachments/assets/12108f41-6fde-4b72-930b-b1f24d1e0a41" width="500">
    <figcaption>
      <br>
      <b>Project Structure</b>
    </figcaption>
  </figure>
</div>
<br><br>



How to Use (Step-by-Step Guide)
-
Since the database starts empty (except for the Admin), follow these steps to see the system in action:

**1. Log in as Admin**

- Login: admin@novaims.unl.pt

- Password: adminims

- *Note: This account is auto-generated if it doesn't exist.*

<div align="left">
  <figure>
    <img src="https://github.com/user-attachments/assets/ef3af49d-2a00-476a-ac77-ffe4449ce1ec" width="400">
    <figcaption>
      <br>
    </figcaption>
  </figure>
</div>
<br>


**2. Register a Teacher**

- Go to "Add Teacher".

- Create a teacher (e.g., Name: Prof. Silva, Email: silva@novaims.pt, Pass: 123).

- *Crucial: You must create a teacher before creating a class.*

<div align="left">
  <figure>
    <img src="https://github.com/user-attachments/assets/ce566875-6da6-4d5c-ad0b-12178ca54332" width="500">
    <figcaption>
      <br>
    </figcaption>
  </figure>
</div>
<br>


**3. Schedule a Class**

- Go to "Schedule Class".

- Enter details (e.g., "Information Systems", Date/Time).

- Select Prof. Silva from the dropdown menu.

<div align="left">
  <figure>
    <img src="https://github.com/user-attachments/assets/2e308a72-4cd8-45ee-b8ba-891e44cac08e" width="500">
    <figcaption>
      <br>
    </figcaption>
  </figure>
</div>
<br>


**4. Register a Student**

- Go to "Add Student".

- Enter details (e.g., Name: João Pedro, Email: joaopedro@novaims.pt, Phone Number: 911222333, Birth Date: 11/02/2006).

- Check the box for the class "Information Systems" to enroll the student.

<div align="left">
  <figure>
    <img src="https://github.com/user-attachments/assets/64400495-5937-4f6d-abae-ab65e33b5937" width="500">
    <figcaption>
      <br>
    </figcaption>
  </figure>
</div>
<br>


**5. Log in as Teacher**

- Logout from Admin.

- Log in with the teacher credentials you created in Step 2 (silva@novaims.pt / 123).

<div align="left">
  <figure>
    <img src="https://github.com/user-attachments/assets/99e73a4e-cb1b-4311-abcd-72b33e3705f5" width="400">
    <figcaption>
      <br>
    </figcaption>
  </figure>
</div>
<br


**6. Mark Attendance**

- Select the class "Information Systems" from the dropdown.

- Mark the checkbox next to "João Pedro".

- Click Submit. The attendance is now saved in the database!
<br><br>

<div align="left">
  <figure>
    <img src="https://github.com/user-attachments/assets/c62684fc-f50a-48f1-b6aa-3c2f295e4681" width="500">
    <figcaption>
      <br>
    </figcaption>
  </figure>
</div>
<br>


Database Schema (ER Logic)
-
**User:** Stores both Admins and Teachers.

**Class:** Linked to User (One Teacher has Many Classes).

**Student:** Independent entity.

**Attendance:** A junction table connecting Student and Class with a Boolean attend field. Includes a unique constraint to prevent duplicate records.
