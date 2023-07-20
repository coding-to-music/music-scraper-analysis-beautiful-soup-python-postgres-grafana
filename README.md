# music-scraper-analysis-beautiful-soup-python-postgres-grafana

# 🚀 Scrape a music website with Python and Beautiful Soup and perform analysis using Postgres and Grafana 🚀

https://github.com/coding-to-music/music-scraper-analysis-beautiful-soup-python-postgres-grafana

From / By

## Environment variables:

```java

```

## GitHub

```java
git init
git add .
git remote remove origin
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:coding-to-music/music-scraper-analysis-beautiful-soup-python-postgres-grafana.git
git push -u origin main
```

## Installing Beautiful Soup

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

```java
sudo apt-get update -y

sudo apt-get install python3

sudo apt-get install python3-bs4

sudo apt-get pip

sudo pip install numpy

sudo pip install pandas

pip install ipykernel

sudo apt-get install -y ipython3

```

## Install vscode extensions

```java
python (microsoft)
jupyter (microsoft)
```

## Installing Python Dependencies locally in project

https://stackoverflow.com/questions/53925660/installing-python-dependencies-locally-in-project

The recommended way to do this is by using a virtual environment. You can install virtualenv via pip with

```java
pip install virtualenv
```

Then create a virtual environment in your project directory:

```java
apt install python3.8-venv

python -m venv env

python3 -m venv env # previously: `virtualenv env`
```

Which will create a directory called env (you can call it anything you like though) which will mirror your global python installation. Inside env/ there will be a directory called lib which will contain Python and will store your dependencies.

Then activate the environment with:

```java
source env/bin/activate
```

Then install your dependencies with pip and they will be installed in the virtual environment env/:

```java
pip install -r requirements.txt
```

Then any time you return to the project, run source env/bin/activate again so that the dependencies can be found.

When you deploy your program, if the deployed environment is a physical server, or a virtual machine, you can follow the same process on the production machine. If the deployment environment is one of a few serverless environments (e.g. GCP App Engine), supplying a requirements.txt file will be sufficient. For some other serverless environments (e.g. AWS Lambda) the dependencies will need to be included in the root directory of the project. In that case, you should use

```java
pip install -r requirements.txt -t ./.
```

## Install Jupyter and associated packages

```java
pip install jupyter
```

```java
jupyter --version
```

```java
Selected Jupyter core packages...
IPython          : 8.12.2
ipykernel        : 6.23.2
ipywidgets       : 8.0.6
jupyter_client   : 8.2.0
jupyter_core     : 5.3.0
jupyter_server   : 2.6.0
jupyterlab       : not installed
nbclient         : 0.8.0
nbconvert        : 7.5.0
nbformat         : 5.9.0
notebook         : 6.5.4
qtconsole        : 5.4.3
traitlets        : 5.9.0
```

## Test database connections to postgres

`neon-connect2.py` uses .env value `POSTGRES_URL`

```java
python3 scrapers/neon-connect.py
```

Output

```java
Connection to PostgreSQL DB successful
Query result: (datetime.date(2023, 6, 14),)
```

`neon-connect.py` uses .env value `POSTGRES_URL`

```java
python3 scrapers/neon-connect.py
```

Output

```java
Current time: 2023-06-14 20:13:14.733108+00:00
PostgreSQL version: PostgreSQL 15.2 on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
```

## Run the Jupyter notebook `connect.ipynb` from the command line

`connect.ipynb` uses .env value `FINAL_POSTGRES_URL`

`FINAL_POSTGRES_URL` is `POSTGRES_URL` with `?options=endpoint%3D<endpoint-id>` appended

`<endpoint-id>` is `ep-mute-recipe-123456` in the below URL example:

`postgres://<user>:<password>@ep-mute-recipe-123456.us-east-2.aws.neon.tech/neondb?options=endpoint%3Dep-mute-recipe-123456`

```java
jupyter nbconvert --to markdown --execute scrapers/connect.ipynb
```

Open the markdown output file `scrapers/connect.md` and preview the markdown

```
Connection to PostgreSQL DB successful
Query result: (datetime.date(2023, 6, 14),)
```
