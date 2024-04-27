# Final Project - Hanlu Ma
# 1. Project Overview
### -- Briefly describe the purpose and functionality of your web application.
This project intends to create an interactive and convinient platform to verify the correctness of the email. As we embrace more data and information on a daily basis recently, the validity of the emails becomes an essential need. With this project, users can easily determine the validity of emails, helping them avoid potential security risks. The functionality of the web application allows users to input email addresses they wish to test into the provided input box and receive verification outcomes within seconds.

# 2. Usage Guidelines
### -- Explain how users can interact with your application, including any input requirements or steps to follow.
Interacting with our application is straightforward. Users only need to input their email address into the designated box and click the submit button. The webpage will then automatically generate the outcome of the email validity. On all pages, users will find an input box and submit button to test different email addresses without returning to the homepage.

# 3. Dependencies
### -- List any external libraries, APIs, tools and database that your project depends on.
I used the email validation API from the AbstractAPI website. Here is the link for more details: https://www.abstractapi.com/api/email-verification-validation-api

# 4. Project Structure
### -- Give a high-level overview of your project's structure, outlining key files and directories.
My project mainly consists of three parts: Flask application, data source, and HTML/CSS pages. The HTML/CSS pages handle the visual appearance and user interactions of the website. The dat source originates from the information extracted from the email validation API. The Flask application acts as the intermediary, connecting the HTML/CSS pages and API dictionary components. It retrieves data from the email validation API, filters it based on the user input, generates corresponding outcomes, and promptly displays error pages if needed.

# 6. Acknowledgments
### -- Credit any external resources, libraries, or APIs that you used in your project.
Email Validation API from the Abstract API website: https://www.abstractapi.com/api/email-verification-validation-api

# 7. Reflection
### -- From the process point of view, what went well, what challenges that were faced and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped you succeed.
From a process perspective, building the overall project structure, including the front-end webpage, back-end web application, and API data extraction, proceeded smoothly. However, several challenges arose, particularly with minor bugs. For instance, after completing the CSS pages, updates did not appear on the webpage as expected. Additionally, I encountered difficulties running the code for the Flask application section. Despite having a high-level understanding of Flask, my limited hands-on experience with it led to prolonged troubleshooting to render the intended pages and content correctly.

One aspect that proved invaluable was setting up a proper test sample. Designing a few sample emails with specific outcomes allowed for quick identification of code effectiveness and helped address potential issues early in the development process. Moving forward, further improvement could be made by enhancing testing procedures and perhaps seeking additional resources or guidance for smoother Flask application implementation.

### -- From a learning perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you knew beforehand that could have helped you succeed.
In terms of learning, I found that ChatGPT works best for straightforward and unilateral tasks with limited files and project size. While attempting to debug code errors in this project using ChatGPT, I encountered limitations in its effectiveness. While it provided some general suggestions, ChatGPT struggled to offer detailed guidance for specific errors. The suggested directions often aligned with my initial assumptions, which I had already explored and tested. Despite this, I wasn't discouraged by ChatGPT's suggestions given the complexity of the project. With multiple files involved, it was challenging to provide ChatGPT with a clear and detailed prompt for optimal suggestions.

ChatGPT still proved valuable in suggesting potential expansions for the project. For instance, ChatGPT proposed incorporating input boxes on the result and error pages to prompt users to retry email verification, enhancing user experience. Overall, I view ChatGPT not as a tool dominating the entire project workflow, but rather as a helpful resource providing occasional and additive guidance throughout the way. In hindsight, I wish I had known more about "strength" and "weakness" of ChatGPT in handling complex debugging tasks and better understand what a "proper" prompt looks like, which could have helped manage my expectations and approach the project more effectively.