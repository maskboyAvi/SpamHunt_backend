# Spamhunt Backend

Spamhunt Backend is a Django Rest Framework application designed to support the SpamHunt app. It provides two main features: detecting whether SMS or Emails are spam or not, utilizing machine learning models.

![Screenshot (225)](https://github.com/maskboyAvi/SpamHunt_backend/assets/123640350/e549017f-0cea-4470-aaaf-6d81e4613ed4)

## Features

1. **Spam Detection:** The backend integrates machine learning models to analyze SMS and Emails and determine whether they are spam.

2. **NLP for Text Input:** The repository includes a Python notebook where machine learning models were trained, especially focusing on Natural Language Processing (NLP) for text input. These models have been employed to enhance the spam detection capabilities.

## Check out the Project

- **SpamHunt:** [https://maskboyavi.github.io/SpamHunt_frontend/](https://maskboyavi.github.io/SpamHunt_frontend/)
  

## Getting Started

Follow these instructions to set up and run the Spamhunt Backend locally.

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework
- Required Python packages (specified in requirements.txt)

### Installation

```bash
git clone https://github.com/your-username/Spamhunt_backend.git
cd Spamhunt_backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Visit http://localhost:8000/ to access the locally running Spamhunt Backend.

Deployment
The Spamhunt Backend is already deployed on AWS. You can check for messages using the following links:

SMS: http://16.171.166.42/sms/
Mails: http://16.171.166.42/mails/
Usage
Provide clear instructions on how to use the Spamhunt Backend, especially how to interact with the API for spam detection.

License
This project is licensed under the MIT License.

Feel free to reach out with any questions or feedback!
