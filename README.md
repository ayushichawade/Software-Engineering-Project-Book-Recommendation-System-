# Book Recommendation System 
A book recommendation system is a software tool that suggests books to users based on their preferences, reading history, and similar users' behavior, enhancing their discovery experience. By analyzing user data and book attributes, these systems provide personalized recommendations, helping users find relevant and interesting books efficiently.<br>
Here is the UI [Book Recommendation System](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/UI/UI.pdf)<br>
Source code:<br>
[Genre.py](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/main%20code/genre.py)<br>
[Popular.py](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/main%20code/popularity.py)<br>
[Recommendation.py](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/main%20code/recommendation.py)<br>


# 1. Git 
I used GitHub to save and update all my project work. Whenever I made changes or added something new to my project, I uploaded it to GitHub. This helped me keep track of my progress and have a backup of my work<br>
![work](https://github-readme-streak-stats.herokuapp.com/?user=ayushichawade&theme=cobalt)

# 2. UML
UML diagrams are a standardized visual representation technique used in software engineering to model software systems. <br>
1. [Activity Diagram](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/UML%20Diagrams/activity_diagram.pdf)<br>
2. [Class Diagram](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/UML%20Diagrams/class_diagram.pdf)<br>
3. [Use Case](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/UML%20Diagrams/usecase_diagram.pdf)<br>



# 3. DDD
A Domain-Driven Design (DDD) diagram visually represents the domain model, its entities, their relationships, and interactions. It serves as a blueprint for developers to understand and communicate the core concepts and structure of the software system.<br>
1. [Event Storming to find domains](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/DDD/Event_Storming.pdf) <br>
2. [Core Domain Charts and](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/DDD/Core_domain_chart.pdf) <br>
3. [Domain Mappings](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/DDD/Domain_mappings.pdf) <br>


# 4. Metrics 
For measuring metrics I used Sonarcloud<br>
SonarCloud is a code quality and security analysis tool that helps developers improve their code by identifying bugs, vulnerabilities, and code smells. 
[Sonarcloud_Metrics](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/tree/main/metrics)


# 5. Clean Code Development 
1.	Readability and Understandability: The code is generally easy to read, with clear function names and variable names.<br> For example:load_books_data(), get_user_favorite_genres(), etc., have clear and descriptive names.<br>
2.	Modularity: Functions are modular, with separate components responsible for specific tasks, such as data loading, preprocessing, and model training.<br>
3.	DRY (Don't Repeat Yourself): While most functions adhere to the DRY principle by encapsulating reusable logic, the absence of the recommend_books() function, which could consolidate recommendation logic, might be considered a violation of DRY.<br>
4.	Testing: Unit tests are available in separate files, and showcase a proactive approach toward testing each function's behavior. This strategy aligns with industry best practices, fostering comprehensive validation of the code's functionality when leveraging testing frameworks like pytest or unittest.<br>
[Test files are available here](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/tree/main/test)  <br>
5.	Consistent Style: The code follows consistent style throughout. <br>
For instance: Indentation is consistent. <br>
Naming conventions are consistent.



# 6. Build Management 
Maven is a powerful automation tool probably used for Java projects, as my codes are in Python language I have built a separate code for build management.<br>
1. [Signin/Login](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/tree/main/maven/src/main/java)<br>
2. [POM.xml file](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/maven/pom.xml)<br>
3. [Output](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/tree/main/maven)<br>
4. [Output](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/maven/maven.pdf)<br>

# 7. Unit Tests
Unit tests are created to verify individual components or functions of code, ensuring they produce the expected output for given inputs, which helps identify bugs early, maintain code integrity, and facilitate code refactoring and maintenance.<br>
1. [Genre Test](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/test/genre_test.py)<br>
2. [Popularity Test](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/test/popularity_test.py)<br>
3. [Recommendation Test](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/test/recommendation_test.py)<br>


# 8. Continuous Delivery (Pipeline):
For the pipeline, I have used Jenkins, an open-source automation server used for continuous delivery(CI/CD), automating the building, testing, and deployment of software projects.<br>
[Jenkins](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/tree/main/Jenkins%20(CI-CD)) <br>


# 9. IDE
I worked with Visual Code Studio as an IDE for this project, and integrating it with GitHub enhanced efficiency and productivity.<br> 
1.	Ctrl+F: Find specific words (variables or def name) to edit or review them<br>
2.	Shift + Enter: run the current code <br> 
3.	F5 : start/end debugging <br> 
4.	 Alt+ Up/Down arrow: To move certain pieces of code to different places in the current file.<br> 
5.	Ctrl + Alt+ up/down arrow: when we want to make some edits with multiple lines, it is the efficient way.<br> 
6.	Ctrl + \: Split view / Side-by-side editing, allows you to use split view while editing your files. For me, it was very efficient for creating test files for the code.<br>
7.	Shift + Alt + down/up: copy the lineup or down.<br>


 # 10. DSL
 Domain-specific language, is a type of programming language designed for specific tasks or industries, making it easier for people in those fields to write code that directly addresses their needs without unnecessary complexity.<br>
1. [DSL code](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/DSL/DSL.py)<br>
2. [Recommendation_dsl](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/DSL/recommendation.dsl.py)<br>
3. [Recommendation_dsl_yaml](https://github.com/ayushichawade/Software-Engineering-Project-Book-Recommendation-System-/blob/main/DSL/recommendations.dsl.yaml)<br>
 




      
