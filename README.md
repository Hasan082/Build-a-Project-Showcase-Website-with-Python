# Project Showcase Website

Welcome to the Project Showcase Website! This repository contains the source code for a personal portfolio website that highlights various projects and professional details. The website is built using Python and Streamlit, showcasing a collection of completed projects along with a contact form for inquiries.

## Features

- **Home Page**: Introduction and professional background.
- **Project Gallery**: Display of various projects with descriptions, images, and source code links.
- **Contact Form**: Allows visitors to send emails directly from the website.

## Technology Stack

- **Backend**: Python, Streamlit
- **Data Management**: Pandas
- **Email Service**: smtplib

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory with the following content:
        ```
        GMAIL_PASSWORD_LOCAL=your_local_gmail_password
        ```


5. **Run the application locally**:
    ```bash
    streamlit run Home.py
    ```

## Usage

### Home Page

- **Introduction**: Displays a brief introduction and professional background.
- **Image**: A profile picture to personalize the page.

### Project Gallery

- **Project Display**: A gallery of projects with titles, descriptions, images, and links to source code.

### Contact Form

- **Email Form**: Visitors can send messages directly through the website.
- **SMTP Configuration**: Emails are sent using the Gmail SMTP server.


## Contribution

Feel free to fork this repository, make improvements, and send a pull request. Contributions are always welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for more details.
