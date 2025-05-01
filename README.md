# Cybersecurity Vulnerabilities Simulation Project

This project was developed as part of my Independent Study in Computer Science at The College of Wooster. It demonstrates how various cyberattacks—such as brute-force login attempts and SQL injection—can exploit weak security practices in corporate environments. The web application includes both **vulnerable** and **hardened** versions of a login-based website, simulating how real-world attackers target systems and how proper security measures can prevent them.

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Django (Python)  
- **Database:** SQLite  
- **Automation / Attack Simulation:** Python, Selenium  
- **Other Tools:** Git, Chrome WebDriver  


## 💡 Features

### 🔐 Secure Site
- Strong password validation  
- Input sanitization to prevent SQL injection  
- Rate-limiting login attempts  
- CSRF protection  
- Secure cookie handling  

### 🔓 Insecure Site
- Minimal/no input validation  
- Weak password enforcement  
- Vulnerable to SQL injection and brute-force attacks  

### 🎯 Simulated Attacks
- **Brute-force Script:** Automates rapid login attempts to guess weak credentials  
- **SQL Injection Script:** Demonstrates database access via unsanitized input fields  
- Scripts use Selenium to automate browser behavior for realism  

## 🧪 Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/cybersecurity-sim.git](https://github.com/KFrancis25/Interactive-Diary.git)
cd my_project
```

### 2. Install Dependencies
```bash
Django>=4.0,<5.0
selenium>=4.0
python-dotenv   # if you're using environment variables
```
---
✅ Other System Requirements
Google Chrome (or another Chromium browser)

ChromeDriver (must match the version of Chrome installed)

✅ Dev Environment Assumptions
Python 3.9 or above

Git (to clone and manage the repo)

Virtualenv or venv for isolation

SQLite (default for Django, no extra install needed)

### 3. Run Django Servers
```bash
python manage.py runserver
```

### 4. Launch Attack Scripts (for testing)
Make sure WebDriver is installed and the server is running
Also, make sure you are in the right directory (/selenium_attacks) or else the program will not run correctly
```bash
python attack_scripts/brute_force.py
python attack_scripts/sql_injection.py
```

🧑‍💻 Case Studies Included
Kevin Mitnick (Social Engineering)

ShinyHunters (Credential Leaks)

Lazarus Group (Advanced Persistent Threats)

Legion of Doom (Historical Influence)

Each case study is analyzed to show how the techniques relate to the project’s simulated attacks.

⚖️ Ethical Considerations
This project was developed strictly for educational purposes. It follows ethical hacking guidelines and does not promote illegal cyber activity. All simulated attacks are contained within a safe, local environment.

📚 Acknowledgments
Django Documentation

OWASP Top 10

CodePath Cybersecurity Course

Faculty Advisor: [Dr. Heather Guarnera]

🔐 Author
Kai Francis
Computer Science Major '25, College of Wooster
