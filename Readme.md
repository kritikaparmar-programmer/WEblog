# WEblog
WEblog is a blogging website. Do give it a try for good experience.

[![Alt text for your video](https://github.com/kritikaparmar-programmer/WEblog/blob/master/video/weblog_image.png)](https://github.com/kritikaparmar-programmer/WEblog/blob/master/video/2020-12-27-19-10-49.mp4)

## Tech Stack
- **Frontend:** HTML/CSS
- **Backend:** Django

## Quick Start :

- **Fork it** :

Get your own Fork/Copy of repository by clicking `Fork` button right upper corner.<br><br>

- **Clone**:

```sh
$ git clone https://github.com/kritikaparmar-programmer/WEblog.git
$ cd WEblog/blogproject
```

- **Branching**
```
$ git checkout -b [your_branch_name]
```

- **Make Changes in Source Code**

#### Setting up Project

- Create a Virtual Environment
```
python3 -m venv env
```

- Activate the Virtual Environment
  - On Windows
    ``` 
    env\Scripts\activate
    ```
  - On Linux or MAC
    ```
    source env/bin/activate
    ```

- Install dependencies using
```
pip install -r requirements.txt
```
- Make migrations using
```
python manage.py makemigrations
```
- Migrate Database
```
python manage.py migrate
```
- Create a superuser
```
python manage.py createsuperuser
```
- Run server using
```
python manage.py runserver
```

- **Stage your Changes and Commit**
```
# For adding/Staging Changes

$ git add .


# For Commiting Changes

$ git commit -m "<your commit message>"

```

- **Push your Commit to Repo**
```
$ git push origin <branch_name>
```

