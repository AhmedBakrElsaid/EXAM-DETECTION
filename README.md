# Examac Backend
### note: change the repo name to Examac
## Run localy:
1. First Install Python on your machine
2. clone repo  
    ```shell
    git clone https://github.com/AhmedBakrElsaid/EXAM-DETECTION.git
    ```
3. go to project folder  
    ```shell
    cd EXAM-DETECTION
    ```
4. Create virtual environment  
    ```shell
    python -m venv venv
    ```
5. activate environment  
    ```shell
    ./venv/scripts/activate.ps1 
    ```
6. Install requirements  
    ```shell
    pip install -r requirements.txt 
    ```
7. Migrate database 
    ```shell
    python manage.py migrate
    ```
8. run server
    ```shell
    python manage.py runserver
    ```

<hr>

# API Endpoints:
1. api/answers/all
    - return all student answers
2. api/answer/int:pk/
    - return student answer with given id
3. [TODO: add endpoint to return answers given exam id]
4. [TODO: add endpoint to return answers given student id]
5. api/question/all
    - return all questions
6. api/question/int:pk/
    - return question with given id
7. [TODO: add endpoint to return questions given exam id]
8. api/exam/all
    - return all exams
9. api/exam/int:pk/
    - return exam with given id
10. [TODO: add endpoint to return exams given classroom id]
11. [TODO: add endpoint to return exams given student id]
12. api/clasroom/all
    - return all classrooms
13. api/clasroom/int:pk/
    - return classroom with given id
14. [TODO: add endpoint to return classrooms given student id]
15. [TODO: add endpoint to return classrooms given teacher id]
16. [TODO: add endpoint for authentication]
17. [TODO: add endpoint for creating exams]
18. [TODO: add endpoint for creating questions]
19. [TODO: add endpoint for creating classrooms]
20. [TODO: add endpoint for sending student answers]
21. [TODO: all the above but for editing and deleting]
21. [TODO: add endpoint for grading using ai model]

