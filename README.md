# oim3640_final_project - Hanlu Ma
# 1. Project Overview
### -- Briefly describe the purpose and functionality of your web application.
This project intends to create an interactive platform that helps users to identify the validity of the email. As we embraces more data and information on a daily basis, the validity of the emails becomes an essential issue. Therefore, I developed this project that assists users to identify the correctness of the emails to avoid any potential future security risks. In the web application, the users can simply enter the emails that they want to test in the input box and they will receive the corresponding verification outcomes within secs.

# 2. Usage Guidelines
### -- Explain how users can interact with your application, including any input requirements or steps to follow.
It is pretty simple for the user interaction. Simply, the user just need to input the email in the box and click submit. They webpage will automatically return the outcome. For any other pages in addition to the homepage, there are always the input box and submit button to redo or try other email without going back to the homepage. Additionally, on any other pages in addition to the homepage, we also have the button to go back to the homepage.

# 3. Dependencies
### -- List any external libraries, APIs, tools and database that your project depends on.
I used the email validation api from the abstract website. Here is the link for more details: https://www.abstractapi.com/api/email-verification-validation-api

# 4. Project Structure
### -- Give a high-level overview of your project's structure, outlining key files and directories.
My project mainly consists of three parts: flask application, api dictionary, and html pages. HTML pages mainly serves a role for the appearances and interactions of the website with the users. In API disctionary part, I mainly extract the data from the email validation api. The Flask application part mainly connects the html pages and API dictionary parts together. Mainly, the flask application extracts data from api dictionary, filters data based on user import, generates the corresponding outcome, and reports the error page promptly based on the user input.

# 6. Acknowledgments
### -- Credit any external resources, libraries, or APIs that you used in your project.
Email Validation API from the Abstract API website: https://www.abstractapi.com/api/email-verification-validation-api

# 7. Reflection
### -- From the process point of view, what went well, what challenges that were faced and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped you succeed.

### -- From a learning perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you knew beforehand that could have helped you succeed.