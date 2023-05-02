# Escalade

 There is a board (same as snakes and ladders) numbered from 1 to 80. Initially, the user will be at position 0. First, a die will be rolled, then the team has two options, either to re-roll, which will cost 15 points, or take a sneak peek(which will reveal whether, at the upcoming position, there is a monster or a booster), which will cost 25 points. After that, a question will appear(on a random basis), and the team has to answer that question to move forward. Answering a question correctly will reward 10 points and the player moves forward the number of places that appeared on the die. Points will not be rewarded for answering the same question multiple times. The team can take one hint per question(which will cost 10 points). If a team encounters a monster at any position, they will step down to a specified position. If the team encounters a booster, they will move up to a specific position.

## Soft Skill 
This puzzle/game is used to judge user's Perseverance.This soft skill refers to the quality of persisting in a task or goal despite obstacles or setbacks.
In this puzzle their is a setback of monster which can bring you down at any moment of the game . The user id expected to not quit abd keep answering the questions until the user wins that game. Individuals who possess this quality tend to be tenacious and determined, which can help them achieve success in their personal and professional lives. Perseverance is particularly important when faced with difficult challenges, as it can help individuals stay focused and motivated to overcome obstacles and achieve their objectives.

## Tech Stack

**Client:** HTML, CSS, JavaScript

**Server:** Python, Django

**Database:** PostgreSQL

## Run Locally

Clone the project

```bash
  git clone https://github.com/creative-computing-society/jungle-ctf.git
```

Go to the project directory

```bash
  cd jungle-ctf
```

We recommend you to use virtual environment

```bash
  python -m venv venv
```

Activate virtual environment

&emsp;&emsp;For Windows PowerShell

```bash
    env/Scripts/activate.ps1
```

&emsp;&emsp;For Linux and MacOS

```bash
    source env/bin/activate
```

Install dependencies

Note: For Windows users, replace psycopg2-binary with psycopg2 in requirements.txt

```bash
  pip install -r requirements.txt
```

Make sure you have installed PostgreSQL

Run the following commands in psql shell:  
```
psql postgres
```
Create a new database for your Django project:
```
CREATE DATABASE escalade;
```
Create a new user with a password:
```
CREATE USER username WITH PASSWORD 'your_pass';
```
Grant all privileges on the database to the user:

```
GRANT ALL PRIVILEGES ON DATABASE escalade TO username;
```
Exit the Postgres shell:
```
\q
```

Create `.env` file in base directory and place Secret-Key, Email credentials and Database credentials, as per the format given in `sample_credentials.txt`

Run Migrations

```
 python manage.py makemigrations
```

```
 python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

To add data such as questions and boards information to database, open *Admin Panel*, first go to *Questions* section, and Click on the *Import* button at top-right corner, select Format as *xlsx*, and upload file name *Question.xlsx* from *data* folder, and proceed. Repeat steps for Booster and Opposer tables.

## Endpoints

- `/` - Landing page
- `register/` - For registration of team
- `start/` - Start the game
- `play/` - Main gameplay page
- `leaderboard/` - Leaderboard
- `rulebook/` - Rulebook
- `login/` - Login
- `logout/` - Logout
- `admin/` - Admin Panel



