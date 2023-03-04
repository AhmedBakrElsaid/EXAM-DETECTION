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
1. api/answers/all [GET][POST]
    - [GET] return all student answers
    - [POST] send student answers to database 
2. api/answer/int:pk/ [GET][PUT][DELETE]
    - [GET] return student answer with given id
    - [PUT] update student answer with given id
    - [DELETE] delete student answer given an id
3. [TODO: add endpoint to return answers given exam id]
4. [TODO: add endpoint to return answers given student id]
5. api/question/all [GET][POST]
    - [GET] return all questions 
    - [POST] send questions to database 
6. api/question/int:pk/ [GET][PUT][DELETE]
    - [GET] return question with given id
    - [PUT] update question with given id
    - [DELETE] delete question given an id
7. [TODO: add endpoint to return questions given exam id]
8. api/exam/all [GET][POST]
    - [GET] return all exams
    - [POST] send exam to database 
9. api/exam/int:pk/ [GET][PUT][DELETE]
    - [GET] return exam with given id
    - [PUT] update exam with given id
    - [DELETE] delete exam with given id
10. [TODO: add endpoint to return exams given classroom id]
11. [TODO: add endpoint to return exams given student id]
12. api/clasroom/all [GET][POST]
    - [GET] return all classrooms
    - [POST] send classroom to database 
13. api/clasroom/int:pk/ [GET][PUT][DELETE]
    - [GET] return classroom with given id
    - [PUT]update classroom with given id
    - [DELETE] delete classroom with given id 
14. [TODO: add endpoint to return classrooms given student id]
15. [TODO: add endpoint to return classrooms given teacher id]
16. [TODO: add endpoint for authentication]
21. [TODO: add endpoint for grading using ai model]

