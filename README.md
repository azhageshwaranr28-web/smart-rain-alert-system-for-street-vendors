# Smart Rain Alert System for Street Vendors

A final-year Bachelor of Engineering project that combines weather prediction, air-quality classification, online weather data, and configurable alert delivery to help street vendors and other outdoor workers prepare for changing environmental conditions.

The project report describes an approach that combines offline prediction from historical datasets with online weather measurements and multi-channel notifications. The supplied implementation is a Flask web application with bundled machine-learning models, HTML templates, static assets, datasets, and custom fuzzy-logic layers. [1]

## Project Information

| Item | Details |
|---|---|
| Project title | Smart Rain Alert System for Street Vendors |
| Authors | R. Azhageshwaran and S. Sanjay |
| Department | Computer Science and Engineering |
| Institution | University College of Engineering Pattukkottai, Rajadam – 614701 |
| University | Anna University, Chennai |
| Academic year | 2025–2026 |
| Primary language | Python |
| Web framework | Flask |
| Machine-learning components | scikit-learn, TensorFlow/Keras, custom fuzzy layers |
| External weather service | Open-Meteo current-weather endpoint |

## Features

The application provides separate interfaces for manual and online weather prediction, air-quality classification, and result display through the included HTML templates. It loads pre-trained model artifacts from the `predict/` and project-root model files, uses the supplied weather and air-quality datasets for the training scripts, and includes custom `FuzzyLayer` and `DefuzzyLayer` implementations for the neural-network workflow.

Alert delivery is configurable. SMS and email notifications are disabled by default in this repository and can be enabled only after the required environment variables are supplied. This prevents credentials from being stored in source control.

## Repository Structure

```text
.
├── App.py                         # Flask application entry point
├── AModel.py                      # Air-quality model workflow
├── WModel.py                      # Weather model workflow
├── fuzzy_layer.py                 # Custom fuzzy neural-network layer
├── defuzzy_layer.py               # Custom defuzzification layer
├── fuss.py                        # Saved-model prediction example
├── text.py                        # Open-Meteo request example
├── Data/AirQuality.csv            # Air-quality dataset
├── Dataset/Newweather.csv         # Weather dataset
├── Model/                         # Model artifact directory
├── predict/                       # Weather saved-model artifacts
├── Templates/                     # Flask HTML templates
├── static/                        # CSS, JavaScript, images, and fonts
└── docs/SRASREPORTFINAL.pdf       # Final-year project report
```

The original Windows `.venv` and IDE metadata were intentionally not committed because they are machine-specific generated files. A clean environment can be recreated with the instructions below.

## Prerequisites

Use Python 3.10, matching the Python version recorded in the supplied project environment. Python 3.11 may also work, but TensorFlow/Keras compatibility should be checked if the training scripts are used.

## Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/<your-github-username>/smart-rain-alert-system-for-street-vendors.git
cd smart-rain-alert-system-for-street-vendors
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows Command Prompt
.venv\Scripts\activate.bat

# Linux/macOS
source .venv/bin/activate
```

Install the Python dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and replace the placeholder values only when alert notifications are required. Do not commit `.env`.

```bash
# Linux/macOS
cp .env.example .env

# Windows PowerShell
Copy-Item .env.example .env
```

The Flask application reads the following optional settings:

| Variable | Purpose |
|---|---|
| `FLASK_SECRET_KEY` | Flask session secret |
| `FLASK_DEBUG` | Enables Flask debug mode when set to `true` |
| `FLASK_HOST` / `FLASK_PORT` | Local server binding |
| `ALERT_MOBILE_NUMBER` | Destination number for SMS alerts |
| `SMS_API_KEY` | SMS provider credential |
| `SMS_API_URL`, `SMS_ROUTE`, `SMS_SENDER` | SMS provider configuration |
| `ALERT_EMAIL` | Destination email address |
| `SMTP_FROM`, `SMTP_PASSWORD` | SMTP sender credentials |
| `SMTP_HOST`, `SMTP_PORT` | SMTP server configuration |

If `SMS_API_KEY`, `SMTP_FROM`, or `SMTP_PASSWORD` is missing, the corresponding alert function returns without sending a message.

## Running the Web Application

From the project root, run:

```bash
python App.py
```

Open `http://127.0.0.1:5000/` in a browser. The online prediction routes call the Open-Meteo service and therefore require internet access. The manual prediction and air-quality workflows use the bundled model files and form inputs.

## Model and Data Workflows

The supplied scripts are retained in their original project structure. `WModel.py` reads `Dataset/Newweather.csv` and constructs the weather-model workflow using TensorFlow/Keras and the custom fuzzy layers. `AModel.py` reads `Data/AirQuality.csv` for the air-quality workflow. Because model artifacts are already included, most users can start by running the Flask application rather than retraining the models.

Pickle and TensorFlow model files should be loaded only from trusted sources. If the model artifacts are replaced, verify their provenance before using them.

## Academic Report

The complete final-year project report is available at [`docs/SRASREPORTFINAL.pdf`](docs/SRASREPORTFINAL.pdf). It contains the abstract, literature survey, system analysis, design, implementation, testing, results, conclusion, and future-scope sections.

## Security and Responsible Use

The source archive contained embedded notification credentials and recipient details. Before publication, those values were removed from `App.py` and replaced with environment-variable configuration. If the original credentials are still active, revoke or rotate them with the relevant service provider. Never commit passwords, API keys, private tokens, or personal secrets to GitHub.

This repository is an academic project and should be reviewed, tested, and secured before any production deployment. In particular, debug mode should remain disabled in production, input validation should be strengthened, outbound API calls should use appropriate authentication and error handling, and model artifacts should be managed as trusted files.

## License

No explicit license was provided with the supplied project materials. All rights remain with the project authors and their institution unless a license is added by the maintainers.

## Reference

[1]: docs/SRASREPORTFINAL.pdf "Smart Rain Alert System for Street Vendors — final-year project report"
